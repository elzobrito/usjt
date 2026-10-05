from pathlib import Path
from flask import Flask, render_template

from db import connect, init_db

BASE  = Path(__file__).resolve().parent
DB_PATH = BASE / "loja.db"

app = Flask(__name__, template_folder=str(BASE / "templates"), static_folder=str(BASE / "static"))
app.secret_key = "4ce58595-da24-4fac-a8ad-08ffa776d9b9"

init_db(DB_PATH)

@app.get("/")
def vitrine():
    with connect(DB_PATH) as conn:
        produtos =  conn.execute("SELECT id, nome, preco FROM produtos ORDER BY nome").fetchall()
    return render_template(
        "vitrine.html", 
        titulo = "Vitrine",
        produtos=produtos,
        show_add = false,
        cart_endpoint = none,
        qnt = 0
    )

if __name__ == "__main__":
    app.run(debug=True)