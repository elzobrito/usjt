from flask import Flask, render_template

app = Flask(__name__, template_folder=".")


@app.get("/")
def inicio():
    return render_template("crud_usuarios.html")

@app.get("/home")
def home():
    return render_template("crud_usuarios.html")

if __name__ == "__main__":
    app.run(debug=True)