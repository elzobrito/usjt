"""Aplicação Flask com CRUD de usuários armazenados em SQLite.

A aplicação disponibiliza:

1. Uma interface HTML para:
   - listar usuários;
   - cadastrar usuários;
   - editar usuários;
   - excluir usuários.

2. Uma API JSON para:
   - listar usuários;
   - buscar um usuário pelo ID;
   - cadastrar usuários;
   - atualizar usuários;
   - excluir usuários.

Os dados são armazenados no arquivo usuarios.db. Diferentemente de uma
lista em memória, os cadastros permanecem disponíveis depois que o servidor
é encerrado ou reiniciado.
"""

# Biblioteca nativa utilizada para acessar bancos de dados SQLite.
import sqlite3

# closing() garante que a conexão com o banco seja fechada corretamente
# depois de cada operação.
from contextlib import closing

# Path facilita a construção do caminho para o arquivo do banco de dados.
from pathlib import Path

# Recursos utilizados do Flask:
#
# Flask:
#   cria e configura a aplicação web;
#
# jsonify:
#   transforma dicionários e listas Python em respostas JSON;
#
# redirect:
#   redireciona o navegador para outra rota;
#
# render_template:
#   combina um arquivo HTML com dados enviados pelo Python;
#
# request:
#   permite acessar formulários, parâmetros da URL e conteúdos JSON;
#
# url_for:
#   gera URLs a partir do nome das funções das rotas.
from flask import Flask, jsonify, redirect, render_template, request, url_for


# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DA APLICAÇÃO
# ---------------------------------------------------------------------------

# Cria a aplicação Flask.
#
# __name__ informa ao Flask o nome do módulo atual e ajuda o framework
# a localizar os recursos da aplicação.
#
# template_folder="." informa que o arquivo crud_usuarios.html está na
# mesma pasta deste arquivo Python.
#
# Em projetos maiores, recomenda-se usar uma pasta chamada "templates".
app = Flask(__name__, template_folder=".")


# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DO BANCO DE DADOS
# ---------------------------------------------------------------------------

# Define o caminho completo do arquivo SQLite.
#
# __file__ representa o arquivo Python atual.
# with_name("usuarios.db") cria o caminho para usuarios.db na mesma pasta.
#
# O SQLite criará esse arquivo automaticamente caso ele ainda não exista.
BANCO = Path(__file__).with_name("usuarios.db")


def abrir_conexao():
    """Abre e devolve uma conexão com o banco de dados SQLite."""

    # Cria uma conexão com o arquivo usuarios.db.
    conexao = sqlite3.connect(BANCO)

    # Faz com que as linhas retornadas pelo SQLite possam ser acessadas
    # pelo nome das colunas.
    #
    # Exemplo:
    #     usuario["nome"]
    #
    # Sem row_factory, seria necessário acessar por posição:
    #     usuario[1]
    conexao.row_factory = sqlite3.Row

    return conexao


def inicializar_banco():
    """Cria a tabela de usuários caso ela ainda não exista."""

    # closing() fecha a conexão automaticamente ao final do bloco.
    with closing(abrir_conexao()) as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
            """
        )

        # Confirma a criação da tabela no banco de dados.
        conexao.commit()


def converter_usuario_para_dicionario(usuario):
    """Converte uma linha do SQLite em um dicionário Python."""

    # Uma linha sqlite3.Row precisa ser convertida antes de ser enviada
    # diretamente como JSON.
    return {
        "id": usuario["id"],
        "nome": usuario["nome"],
    }


# Inicializa o banco assim que este módulo é carregado.
#
# Isso garante que a tabela exista tanto quando o arquivo for executado
# diretamente quanto quando a aplicação for iniciada pelo comando flask.
inicializar_banco()


# ---------------------------------------------------------------------------
# ROTAS DA INTERFACE HTML
# ---------------------------------------------------------------------------

@app.get("/")
def inicio():
    """Renderiza a interface HTML com os usuários cadastrados."""

    try:
        with closing(abrir_conexao()) as conexao:
            # Seleciona todos os usuários.
            #
            # ORDER BY id organiza os usuários pelo identificador em ordem
            # crescente.
            usuarios = conexao.execute(
                """
                SELECT id, nome
                FROM usuarios
                ORDER BY id
                """
            ).fetchall()

    except sqlite3.Error as erro:
        # Se houver erro no banco, a página ainda será carregada, mas sem
        # usuários e com uma mensagem informando o problema.
        usuarios = []
        mensagem_erro = f"Erro ao consultar usuários: {erro}"

    else:
        # request.args lê valores presentes na URL.
        #
        # Exemplo:
        #     /?mensagem=Usuário+cadastrado
        mensagem_erro = request.args.get("erro")

    # Recupera uma possível mensagem de sucesso enviada por redirecionamento.
    mensagem = request.args.get("mensagem")

    # Envia os dados para o arquivo crud_usuarios.html.
    return render_template(
        "crud_usuarios.html",
        usuarios=usuarios,
        mensagem=mensagem,
        erro=mensagem_erro,
    )


@app.post("/usuarios")
def cadastrar_usuario():
    """Cadastra um usuário enviado por formulário HTML."""

    # request.form acessa os campos enviados pelo formulário.
    #
    # get("nome", "") devolve uma string vazia caso o campo não exista.
    # strip() remove espaços em branco do início e do final.
    nome = request.form.get("nome", "").strip()

    # O nome é obrigatório.
    if not nome:
        return redirect(
            url_for("inicio", erro="O campo nome é obrigatório"),
            code=303,
        )

    try:
        with closing(abrir_conexao()) as conexao:
            # O caractere ? representa um parâmetro SQL.
            #
            # Essa forma evita concatenar o nome diretamente no comando SQL
            # e protege a aplicação contra injeção de SQL.
            conexao.execute(
                """
                INSERT INTO usuarios (nome)
                VALUES (?)
                """,
                (nome,),
            )

            conexao.commit()

    except sqlite3.Error as erro:
        return redirect(
            url_for(
                "inicio",
                erro=f"Erro ao cadastrar usuário: {erro}",
            ),
            code=303,
        )

    return redirect(
        url_for("inicio", mensagem="Usuário cadastrado com sucesso"),
        code=303,
    )


@app.post("/usuarios/<int:usuario_id>/editar")
def editar_usuario_com_post(usuario_id):
    """Atualiza um usuário por meio de um formulário HTML."""

    nome = request.form.get("nome", "").strip()

    if not nome:
        return redirect(
            url_for("inicio", erro="O campo nome é obrigatório"),
            code=303,
        )

    try:
        with closing(abrir_conexao()) as conexao:
            cursor = conexao.execute(
                """
                UPDATE usuarios
                SET nome = ?
                WHERE id = ?
                """,
                (nome, usuario_id),
            )

            # rowcount informa quantas linhas foram alteradas.
            #
            # Se rowcount for zero, nenhum usuário com esse ID foi encontrado.
            if cursor.rowcount == 0:
                return redirect(
                    url_for(
                        "inicio",
                        erro="Usuário não encontrado",
                    ),
                    code=303,
                )

            conexao.commit()

    except sqlite3.Error as erro:
        return redirect(
            url_for(
                "inicio",
                erro=f"Erro ao atualizar usuário: {erro}",
            ),
            code=303,
        )

    return redirect(
        url_for("inicio", mensagem="Usuário atualizado com sucesso"),
        code=303,
    )


@app.post("/usuarios/<int:usuario_id>/excluir")
def excluir_usuario_com_post(usuario_id):
    """Exclui um usuário por meio de um formulário HTML."""

    try:
        with closing(abrir_conexao()) as conexao:
            cursor = conexao.execute(
                """
                DELETE FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,),
            )

            if cursor.rowcount == 0:
                return redirect(
                    url_for(
                        "inicio",
                        erro="Usuário não encontrado",
                    ),
                    code=303,
                )

            conexao.commit()

    except sqlite3.Error as erro:
        return redirect(
            url_for(
                "inicio",
                erro=f"Erro ao excluir usuário: {erro}",
            ),
            code=303,
        )

    return redirect(
        url_for("inicio", mensagem="Usuário excluído com sucesso"),
        code=303,
    )


# ---------------------------------------------------------------------------
# ROTAS DA API JSON
# ---------------------------------------------------------------------------

@app.get("/api")
def verificar_api():
    """Informa que a API está em funcionamento."""

    return jsonify(mensagem="API funcionando"), 200


@app.get("/api/usuarios")
def listar_usuarios():
    """Retorna em JSON todos os usuários cadastrados no SQLite."""

    try:
        with closing(abrir_conexao()) as conexao:
            usuarios = conexao.execute(
                """
                SELECT id, nome
                FROM usuarios
                ORDER BY id
                """
            ).fetchall()

    except sqlite3.Error as erro:
        return jsonify(
            erro="Não foi possível consultar os usuários",
            detalhes=str(erro),
        ), 500

    # Converte cada sqlite3.Row para um dicionário antes de produzir o JSON.
    usuarios_convertidos = [
        converter_usuario_para_dicionario(usuario)
        for usuario in usuarios
    ]

    return jsonify(usuarios_convertidos), 200


@app.get("/api/usuarios/<int:usuario_id>")
def buscar_usuario(usuario_id):
    """Busca e retorna um usuário pelo identificador."""

    try:
        with closing(abrir_conexao()) as conexao:
            # fetchone() devolve a primeira linha encontrada ou None.
            usuario = conexao.execute(
                """
                SELECT id, nome
                FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,),
            ).fetchone()

    except sqlite3.Error as erro:
        return jsonify(
            erro="Não foi possível consultar o usuário",
            detalhes=str(erro),
        ), 500

    if usuario is None:
        return jsonify(erro="Usuário não encontrado"), 404

    return jsonify(converter_usuario_para_dicionario(usuario)), 200


@app.post("/api/usuarios")
def cadastrar_usuario_api():
    """Cadastra um usuário utilizando um objeto JSON."""

    # silent=True evita uma exceção automática caso o corpo não seja
    # um JSON válido.
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify(
            erro="Envie um objeto JSON válido",
        ), 400

    nome = dados.get("nome")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify(
            erro="O campo nome é obrigatório",
        ), 400

    nome = nome.strip()

    try:
        with closing(abrir_conexao()) as conexao:
            cursor = conexao.execute(
                """
                INSERT INTO usuarios (nome)
                VALUES (?)
                """,
                (nome,),
            )

            conexao.commit()

            # lastrowid contém o ID gerado automaticamente pelo SQLite.
            usuario_id = cursor.lastrowid

    except sqlite3.Error as erro:
        return jsonify(
            erro="Não foi possível cadastrar o usuário",
            detalhes=str(erro),
        ), 500

    usuario = {
        "id": usuario_id,
        "nome": nome,
    }

    # O status 201 Created indica que um novo recurso foi criado.
    return jsonify(
        mensagem="Usuário cadastrado com sucesso",
        usuario=usuario,
    ), 201


@app.put("/api/usuarios/<int:usuario_id>")
def atualizar_usuario(usuario_id):
    """Atualiza o nome de um usuário utilizando um objeto JSON."""

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify(
            erro="Envie um objeto JSON válido",
        ), 400

    nome = dados.get("nome")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify(
            erro="O campo nome é obrigatório",
        ), 400

    nome = nome.strip()

    try:
        with closing(abrir_conexao()) as conexao:
            cursor = conexao.execute(
                """
                UPDATE usuarios
                SET nome = ?
                WHERE id = ?
                """,
                (nome, usuario_id),
            )

            if cursor.rowcount == 0:
                return jsonify(
                    erro="Usuário não encontrado",
                ), 404

            conexao.commit()

    except sqlite3.Error as erro:
        return jsonify(
            erro="Não foi possível atualizar o usuário",
            detalhes=str(erro),
        ), 500

    usuario_atualizado = {
        "id": usuario_id,
        "nome": nome,
    }

    return jsonify(
        mensagem="Usuário atualizado com sucesso",
        usuario=usuario_atualizado,
    ), 200


@app.delete("/api/usuarios/<int:usuario_id>")
def excluir_usuario(usuario_id):
    """Exclui um usuário do banco de dados."""

    try:
        with closing(abrir_conexao()) as conexao:
            cursor = conexao.execute(
                """
                DELETE FROM usuarios
                WHERE id = ?
                """,
                (usuario_id,),
            )

            if cursor.rowcount == 0:
                return jsonify(
                    erro="Usuário não encontrado",
                ), 404

            conexao.commit()

    except sqlite3.Error as erro:
        return jsonify(
            erro="Não foi possível excluir o usuário",
            detalhes=str(erro),
        ), 500

    return jsonify(
        mensagem="Usuário excluído com sucesso",
    ), 200


# ---------------------------------------------------------------------------
# TRATAMENTO DE ERROS HTTP
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def rota_nao_encontrada(erro):
    """Retorna uma resposta apropriada para rotas inexistentes."""

    # Se a rota solicitada começar com /api/, o erro será devolvido em JSON.
    if request.path.startswith("/api/"):
        return jsonify(erro="Rota não encontrada"), 404

    # Para rotas da interface HTML, redireciona para a página inicial.
    return redirect(
        url_for("inicio", erro="Página não encontrada"),
        code=303,
    )


@app.errorhandler(405)
def metodo_nao_permitido(erro):
    """Retorna uma resposta para métodos HTTP não permitidos."""

    if request.path.startswith("/api/"):
        return jsonify(
            erro="Método HTTP não permitido para esta rota",
        ), 405

    return redirect(
        url_for(
            "inicio",
            erro="Operação não permitida",
        ),
        code=303,
    )


# ---------------------------------------------------------------------------
# INICIALIZAÇÃO DO SERVIDOR
# ---------------------------------------------------------------------------

# Este bloco será executado somente quando o arquivo for iniciado diretamente:
#
#     python conexao.py
#
# Se o arquivo for importado por outro programa, o servidor não será iniciado
# automaticamente.
if __name__ == "__main__":
    # debug=True ativa recursos úteis durante o desenvolvimento:
    #
    # 1. recarrega o servidor quando o código é alterado;
    # 2. mostra informações detalhadas sobre erros;
    # 3. facilita o desenvolvimento e os testes.
    #
    # O modo debug não deve ser utilizado em produção.
    app.run(debug=True)