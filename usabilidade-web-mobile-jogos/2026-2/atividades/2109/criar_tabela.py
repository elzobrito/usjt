import sqlite3
from contextlib import closing
from pathlib import Path

BANCO = Path(__file__).parent / "conexao.db"

def abri_banco():
    """Abre a conexão com o banco de dados."""
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

def fechar_banco(conexao):
    """Fecha a conexão com o banco de dados."""
    conexao.close()

def inicializar_banco():
    """Inicializa o banco de dados, criando as tabelas necessárias."""
    with closing(abri_banco()) as conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );
        """)
        conexao.executemany("INSERT OR IGNORE INTO usuarios (nome) VALUES (?)", [("Alice",), ("Bob",), ("Charlie",)])
        conexao.commit()

if __name__ == "__main__":
    inicializar_banco()
    with closing(abri_banco()) as conexao:
        for usuario in conexao.execute("SELECT id, nome FROM usuarios ORDER BY id"):
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}")
