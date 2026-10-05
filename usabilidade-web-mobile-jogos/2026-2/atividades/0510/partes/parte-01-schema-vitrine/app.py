"""Parte 1: schema + seed + vitrine lida do SQLite."""
from pathlib import Path

from flask import Flask, render_template

from db import connect, init_db

BASE = Path(__file__).resolve().parent
DB_PATH = BASE / "loja.db"

app = Flask(__name__, template_folder=str(BASE / "templates"), static_folder=str(BASE / "static"))
app.secret_key = "usjt-carrinho-sqlite-aula-nao-usar-em-producao"

# Garante schema+seed ao importar (útil no test_client e no flask run)
init_db(DB_PATH)


@app.get("/")
def vitrine():
    with connect(DB_PATH) as conn:
        # SELECT simples do catálogo — ainda sem WHERE; padrão ? entra nas próximas partes
        produtos = conn.execute("SELECT id, nome, preco FROM produtos ORDER BY nome").fetchall()
    return render_template(
        "vitrine.html",
        title="Vitrine (SQLite)",
        produtos=produtos,
        show_add=False,
        cart_endpoint=None,
        qtd=0,
    )


if __name__ == "__main__":
    app.run(debug=True)
