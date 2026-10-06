"""
app.py — Carrinho de e-commerce Flask + SQLite
UC 0011109 · USJT 2026-2

Versão consolidada (Partes 1–6).
Rode com:  flask --app app run
           http://127.0.0.1:5000/
"""

import uuid
from pathlib import Path

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from db import connect, init_db

# ─── Configuração ─────────────────────────────────────────────────────────────

BASE    = Path(__file__).resolve().parent
DB_PATH = BASE / "loja.db"

app = Flask(
    __name__,
    template_folder=str(BASE / "templates"),
    static_folder=str(BASE / "static"),
)
app.secret_key = "usjt-carrinho-sqlite-aula-nao-usar-em-producao"

# Garante schema + seed ao iniciar (e no test_client)
init_db(DB_PATH)


# ─── Helpers de sessão e banco ────────────────────────────────────────────────

def get_cart_id() -> str:
    """A session guarda APENAS o identificador do carrinho — não os itens."""
    if "cart_id" not in session:
        session["cart_id"] = str(uuid.uuid4())
    return session["cart_id"]


def contar_itens(cart_id: str) -> int:
    """Retorna a soma total de unidades no carrinho via SUM SQL."""
    with connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT COALESCE(SUM(quantidade), 0) AS n "
            "FROM itens_carrinho WHERE cart_id = ?",
            (cart_id,),
        ).fetchone()
    return int(row["n"])


def listar_itens(cart_id: str) -> list:
    """Retorna os itens do carrinho com JOIN em produtos."""
    with connect(DB_PATH) as conn:
        return conn.execute(
            """
            SELECT
                i.produto_id,
                i.quantidade,
                p.nome,
                p.preco,
                ROUND(p.preco * i.quantidade, 2) AS subtotal
            FROM itens_carrinho AS i
            JOIN produtos       AS p ON p.id = i.produto_id
            WHERE i.cart_id = ?
            ORDER BY p.nome
            """,
            (cart_id,),
        ).fetchall()


def calcular_total(cart_id: str) -> float:
    """Calcula o total do carrinho com SUM diretamente no banco."""
    with connect(DB_PATH) as conn:
        row = conn.execute(
            """
            SELECT COALESCE(SUM(p.preco * i.quantidade), 0) AS total
            FROM itens_carrinho AS i
            JOIN produtos       AS p ON p.id = i.produto_id
            WHERE i.cart_id = ?
            """,
            (cart_id,),
        ).fetchone()
    return float(row["total"])


# ─── Rotas ────────────────────────────────────────────────────────────────────

@app.get("/")
def vitrine():
    """Página principal: lista produtos do banco."""
    cart_id = get_cart_id()
    with connect(DB_PATH) as conn:
        produtos = conn.execute(
            "SELECT id, nome, preco FROM produtos ORDER BY nome"
        ).fetchall()
    return render_template(
        "vitrine.html",
        produtos=produtos,
        qtd=contar_itens(cart_id),
    )


@app.post("/add")
def add():
    """
    Adiciona produto ao carrinho.
    UPSERT: se já existe, incrementa quantidade.
    SQL injection: produto_id nunca é concatenado — sempre via ?.
    """
    cart_id    = get_cart_id()
    produto_id = request.form.get("produto_id", "").strip()

    if not produto_id:
        flash("Produto inválido.", "erro")
        return redirect(url_for("vitrine"))

    # Verifica existência do produto no banco
    with connect(DB_PATH) as conn:
        prod = conn.execute(
            "SELECT id, nome FROM produtos WHERE id = ?", (produto_id,)
        ).fetchone()

    if not prod:
        flash("Produto não encontrado.", "erro")
        return redirect(url_for("vitrine"))

    # UPSERT: insere ou soma 1 à quantidade existente
    with connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO itens_carrinho (cart_id, produto_id, quantidade)
            VALUES (?, ?, 1)
            ON CONFLICT(cart_id, produto_id)
            DO UPDATE SET quantidade = quantidade + 1
            """,
            (cart_id, produto_id),
        )

    flash(f'"{prod["nome"]}" adicionado ao carrinho.', "ok")
    return redirect(url_for("vitrine"))


@app.get("/carrinho")
def ver_carrinho():
    """Página do carrinho: lista itens com JOIN e exibe total via SUM."""
    cart_id = get_cart_id()
    itens   = listar_itens(cart_id)
    total   = calcular_total(cart_id)
    return render_template(
        "carrinho.html",
        itens=itens,
        total=total,
        qtd=contar_itens(cart_id),
    )


@app.post("/update")
def update():
    """
    Altera quantidade de um item.
    Se nova quantidade <= 0, remove a linha (DELETE).
    """
    cart_id    = get_cart_id()
    produto_id = request.form.get("produto_id", "").strip()
    nova_qtd   = request.form.get("quantidade", "0").strip()

    try:
        nova_qtd = int(nova_qtd)
    except ValueError:
        flash("Quantidade inválida.", "erro")
        return redirect(url_for("ver_carrinho"))

    with connect(DB_PATH) as conn:
        if nova_qtd <= 0:
            # Remove a linha — quantidade zero viola o CHECK constraint
            conn.execute(
                "DELETE FROM itens_carrinho "
                "WHERE cart_id = ? AND produto_id = ?",
                (cart_id, produto_id),
            )
            flash("Item removido do carrinho.", "ok")
        else:
            conn.execute(
                "UPDATE itens_carrinho SET quantidade = ? "
                "WHERE cart_id = ? AND produto_id = ?",
                (nova_qtd, cart_id, produto_id),
            )

    return redirect(url_for("ver_carrinho"))


@app.post("/delete")
def delete():
    """Remove completamente um item do carrinho."""
    cart_id    = get_cart_id()
    produto_id = request.form.get("produto_id", "").strip()

    with connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM itens_carrinho "
            "WHERE cart_id = ? AND produto_id = ?",
            (cart_id, produto_id),
        )

    flash("Item removido do carrinho.", "ok")
    return redirect(url_for("ver_carrinho"))


@app.post("/esvaziar")
def esvaziar():
    """Remove todos os itens do carrinho atual."""
    cart_id = get_cart_id()
    with connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM itens_carrinho WHERE cart_id = ?",
            (cart_id,),
        )
    flash("Carrinho esvaziado.", "ok")
    return redirect(url_for("ver_carrinho"))


# ─── Entrypoint ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
