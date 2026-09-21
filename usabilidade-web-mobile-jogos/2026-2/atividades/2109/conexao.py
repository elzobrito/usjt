import sqlite3
from contextlib import closing
from pathlib import Path

BANCO = Path(__file__).parent / "conexao.db"

def abri_banco():
    """Abre a conexão com o banco de dados."""
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

if __name__ == "__main__":
    with closing(abri_banco()) as conexao:
        cursor = conexao.cursor()
        versao = cursor.execute("SELECT sqlite_version();").fetchone()[0]
        print(f"conexao com o banco de dados estabelecida com sucesso! Versão do SQLite: {BANCO}")
        print(f"Versão do SQLite: {versao}")
    print("Conexão com o banco de dados encerrada.")
