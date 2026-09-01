from flask import Flask, render_template

app = Flask(__name__, template_folder=".")

usuarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
    {"id": 3, "nome": "Mariana"},
]


@app.get("/")
def inicio():
    return render_template("crud_usuarios.html", usuarios=usuarios)


if __name__ == "__main__":
    app.run(debug=True)