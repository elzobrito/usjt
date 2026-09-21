import sqlite3
from contextlib import closing
from pathlib import Path

BANCO = Path(__file__).with_name("usuarios.db")


def abrir_conexao():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


if __name__ == "__main__":
    with closing(abrir_conexao()) as conexao:
        versao = conexao.execute("SELECT sqlite_version()").fetchone()[0]
        print(f"Conexão aberta em: {BANCO}")
        print(f"SQLite: {versao}")
    print("Conexão fechada.")
