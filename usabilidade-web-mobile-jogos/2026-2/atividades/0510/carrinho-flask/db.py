"""
db.py — Acesso SQLite didático (stdlib).
Queries SEMPRE parametrizadas com ?.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

# ─── Schema ───────────────────────────────────────────────────────────────────

SCHEMA = """
CREATE TABLE IF NOT EXISTS produtos (
    id     TEXT PRIMARY KEY,
    nome   TEXT NOT NULL,
    preco  REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS itens_carrinho (
    cart_id    TEXT    NOT NULL,
    produto_id TEXT    NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    PRIMARY KEY (cart_id, produto_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
"""

# ─── Seed ─────────────────────────────────────────────────────────────────────

SEED = [
    ("p1", "Caderno universitário",  24.90),
    ("p2", "Caneta esferográfica",    3.50),
    ("p3", "Mochila escolar",       119.00),
    ("p4", "Estojo duplo",           18.50),
    ("p5", "Régua 30 cm",             4.90),
    ("p6", "Lápis de cor 12 cores",    9.90),
    ("p7", "Borracha macia",            2.50),
    ("p8", "Apontador com depósito",     5.90),
    ("p9", "Marcador de texto",          6.90),
    ("p10", "Agenda 2024",              29.90),
    ("p11", "Mochila de rodinhas",      149.00),
    ("p12", "Caderno de desenho",        19.90),
]

# ─── Funções ──────────────────────────────────────────────────────────────────

def connect(db_path: Path) -> sqlite3.Connection:
    """
    Abre a conexão com o SQLite.
    row_factory = sqlite3.Row → acesso por nome: row["coluna"].
    PRAGMA foreign_keys = ON  → valida as FKs em runtime.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: Path, *, seed: bool = True) -> None:
    """
    Cria o schema e popula o catálogo (se ainda não existir).
    Seguro chamar mais de uma vez — INSERT OR IGNORE não duplica.
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with connect(db_path) as conn:
        conn.executescript(SCHEMA)

        if seed:
            conn.executemany(
                "INSERT OR IGNORE INTO produtos (id, nome, preco) VALUES (?, ?, ?)",
                SEED,
            )
