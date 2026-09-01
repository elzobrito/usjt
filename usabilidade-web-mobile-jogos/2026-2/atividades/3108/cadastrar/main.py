from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder=".")

usuarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
]


@app.get("/")
def inicio():
    mensagem = request.args.get("mensagem")
    erro = request.args.get("erro")
    return render_template(
        "crud_usuarios.html",
        usuarios=usuarios,
        mensagem=mensagem,
        erro=erro,
    )


@app.post("/usuarios")
def cadastrar_usuario():
    nome = request.form.get("nome", "").strip()
    if not nome:
        return redirect(
            url_for("inicio", erro="O campo nome é obrigatório"),
            code=303,
        )

    proximo_id = max((usuario["id"] for usuario in usuarios), default=0) + 1
    usuarios.append({"id": proximo_id, "nome": nome})
    return redirect(
        url_for("inicio", mensagem="Usuário cadastrado"),
        code=303,
    )


if __name__ == "__main__":
    app.run(debug=True)