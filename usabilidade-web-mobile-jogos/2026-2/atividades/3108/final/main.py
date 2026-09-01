"""API HTTP simples para demonstrar rotas com Flask.

Os usuários são mantidos em uma lista na memória. Portanto, os cadastros
realizados durante a execução serão perdidos quando o servidor for reiniciado.
Esse comportamento é intencional para evitar o uso de banco de dados neste
exemplo introdutório.
"""

# Importa os recursos do Flask usados pela aplicação:
#
# Flask:
#   cria a aplicação web e permite registrar as rotas HTTP;
#
# request:
#   representa a requisição HTTP recebida e permite acessar os dados enviados
#   pelo formulário ou em formato JSON;
#
# jsonify:
#   transforma listas e dicionários Python em respostas JSON e define o
#   cabeçalho Content-Type como application/json;
#
# render_template:
#   combina o arquivo HTML com os dados enviados pelo Python;
#
# redirect e url_for:
#   redirecionam o navegador para outra rota depois de um formulário POST.
from flask import Flask, jsonify, redirect, render_template, request, url_for


# Cria a aplicação Flask.
#
# __name__ informa ao Flask o nome do módulo atual. Essa informação ajuda o
# framework a localizar os recursos relacionados à aplicação.
# template_folder="." informa que o arquivo HTML está na mesma pasta deste
# programa. Em projetos maiores, normalmente seria usada a pasta "templates".
app = Flask(__name__, template_folder=".")


# Lista usada como armazenamento temporário dos usuários.
#
# Em Python, cada item da lista é um dicionário com duas propriedades:
#   id: identificador numérico e único;
#   nome: nome do usuário.
#
# Como não existe um banco de dados, qualquer alteração feita nesta lista
# permanece disponível somente enquanto o programa estiver em execução.
usuarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
]


# Registra a rota da interface web.
#
# Método: GET
# Caminho: /
# Exemplo: GET http://localhost:5000/
#
# Quando essa URL for acessada, o Flask combinará a lista de usuários com o
# arquivo crud_usuarios.html.
@app.get("/")
def inicio():
    """Renderiza a interface HTML com os usuários cadastrados."""

    # request.args acessa parâmetros presentes na URL. As mensagens são
    # recebidas depois dos redirecionamentos realizados pelas rotas POST.
    mensagem = request.args.get("mensagem")
    erro = request.args.get("erro")

    # render_template() abre o arquivo HTML e entrega a ele três valores:
    # a lista de usuários e as possíveis mensagens de sucesso ou erro.
    return render_template(
        "crud_usuarios.html",
        usuarios=usuarios,
        mensagem=mensagem,
        erro=erro,
    )


# Disponibiliza uma rota simples para verificar o funcionamento da API sem
# substituir a página HTML apresentada na rota principal.
@app.get("/api")
def verificar_api():
    """Informa que a API está em funcionamento."""

    return jsonify(mensagem="API funcionando"), 200


# Registra a rota responsável por listar todos os usuários.
#
# Método: GET
# Caminho: /usuarios
# Exemplo: GET http://localhost:5000/usuarios
@app.get("/usuarios")
def listar_usuarios():
    """Retorna todos os usuários armazenados na lista."""

    # jsonify() converte a lista completa para JSON.
    # O segundo valor da tupla é o status HTTP 200 OK, indicando sucesso.
    return jsonify(usuarios), 200


# Registra uma rota com um parâmetro dinâmico.
#
# Método: GET
# Caminho: /usuarios/<int:usuario_id>
# Exemplos:
#   GET http://localhost:5000/usuarios/1
#   GET http://localhost:5000/usuarios/2
#
# O conversor "int" exige que o valor presente na URL seja um número inteiro.
# O valor será entregue à função pelo parâmetro usuario_id.
@app.get("/usuarios/<int:usuario_id>")
def buscar_usuario(usuario_id):
    """Busca um usuário pelo seu identificador."""

    # A expressão geradora percorre a lista e seleciona os usuários cujo ID
    # é igual ao recebido pela URL.
    #
    # next() devolve o primeiro usuário encontrado. Se nenhum usuário atender
    # à condição, o valor padrão None será devolvido.
    usuario = next(
        (item for item in usuarios if item["id"] == usuario_id),
        None,
    )

    # Se a busca não encontrou um usuário, devolve uma mensagem de erro com
    # o status HTTP 404 Not Found.
    if usuario is None:
        return jsonify(erro="Usuário não encontrado"), 404

    # Se o usuário foi encontrado, devolve seus dados e o status 200 OK.
    return jsonify(usuario), 200


# Registra a rota responsável pelo cadastro de usuários.
#
# Método: POST
# Caminho: /usuarios
# O formulário HTML enviará um campo chamado "nome".
@app.post("/usuarios")
def cadastrar_usuario():
    """Valida e adiciona um novo usuário à lista em memória."""

    # request.form acessa os campos enviados por um formulário HTML.
    # get("nome", "") devolve uma string vazia se o campo não existir.
    nome = request.form.get("nome", "").strip()

    # Se o nome estiver vazio, volta à página inicial com uma mensagem de erro.
    if not nome:
        return redirect(
            url_for("inicio", erro="O campo nome é obrigatório"),
            code=303,
        )

    # Localiza o maior ID existente e acrescenta 1 para formar o próximo ID.
    # O valor default=0 permite que o cálculo funcione mesmo se a lista estiver
    # vazia: nesse caso, o primeiro ID gerado será 1.
    proximo_id = max(
        (usuario["id"] for usuario in usuarios),
        default=0,
    ) + 1

    # Monta o dicionário que representa o novo usuário.
    # O nome é armazenado sem espaços desnecessários nas extremidades.
    novo_usuario = {
        "id": proximo_id,
        "nome": nome,
    }

    # Adiciona efetivamente o novo usuário ao final da lista.
    # A partir deste momento, ele aparecerá nas consultas GET /usuarios.
    usuarios.append(novo_usuario)

    # Depois do POST, redireciona o navegador para a página inicial.
    # O status 303 orienta o navegador a realizar uma nova requisição GET,
    # evitando o reenvio do formulário se a página for atualizada.
    return redirect(
        url_for("inicio", mensagem="Usuário cadastrado"),
        code=303,
    )


# Esta rota atualiza um usuário utilizando somente um formulário HTML.
#
# Embora a operação represente uma atualização, o HTML puro não consegue
# enviar PUT. Por isso, o formulário utiliza POST e uma rota específica.
@app.post("/usuarios/<int:usuario_id>/editar")
def editar_usuario_com_post(usuario_id):
    """Atualiza um usuário por meio de um formulário POST."""

    usuario = next(
        (item for item in usuarios if item["id"] == usuario_id),
        None,
    )

    if usuario is None:
        return redirect(
            url_for("inicio", erro="Usuário não encontrado"),
            code=303,
        )

    nome = request.form.get("nome", "").strip()

    if not nome:
        return redirect(
            url_for("inicio", erro="O campo nome é obrigatório"),
            code=303,
        )

    usuario["nome"] = nome

    return redirect(
        url_for("inicio", mensagem="Usuário atualizado"),
        code=303,
    )


# Esta rota exclui um usuário utilizando um formulário HTML.
#
# O HTML puro não consegue enviar DELETE. Portanto, o formulário usa POST e
# informa o usuário a ser excluído por meio do endereço da rota.
@app.post("/usuarios/<int:usuario_id>/excluir")
def excluir_usuario_com_post(usuario_id):
    """Exclui um usuário por meio de um formulário POST."""

    usuario = next(
        (item for item in usuarios if item["id"] == usuario_id),
        None,
    )

    if usuario is None:
        return redirect(
            url_for("inicio", erro="Usuário não encontrado"),
            code=303,
        )

    usuarios.remove(usuario)

    return redirect(
        url_for("inicio", mensagem="Usuário excluído"),
        code=303,
    )


# Registra a rota responsável pela atualização de um usuário.
#
# Método: PUT
# Caminho: /usuarios/<int:usuario_id>
# Exemplo: PUT http://localhost:5000/usuarios/1
# Corpo JSON: {"nome": "Ana Maria"}
@app.put("/usuarios/<int:usuario_id>")
def atualizar_usuario(usuario_id):
    """Atualiza o nome de um usuário existente."""

    # Procura o usuário que será atualizado.
    usuario = next(
        (item for item in usuarios if item["id"] == usuario_id),
        None,
    )

    # Não é possível atualizar um recurso que não existe.
    if usuario is None:
        return jsonify(erro="Usuário não encontrado"), 404

    # Obtém e valida o objeto JSON enviado pelo navegador.
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify(erro="Envie um objeto JSON válido"), 400

    nome = dados.get("nome")
    if not isinstance(nome, str) or not nome.strip():
        return jsonify(erro="O campo nome é obrigatório"), 400

    # Altera o nome no próprio dicionário armazenado na lista.
    usuario["nome"] = nome.strip()

    # Retorna o usuário atualizado e o status 200 OK.
    return jsonify(
        mensagem="Usuário atualizado",
        usuario=usuario,
    ), 200


# Registra a rota responsável pela exclusão de um usuário.
#
# Método: DELETE
# Caminho: /usuarios/<int:usuario_id>
# Exemplo: DELETE http://localhost:5000/usuarios/1
@app.delete("/usuarios/<int:usuario_id>")
def excluir_usuario(usuario_id):
    """Remove um usuário da lista em memória."""

    # Procura o usuário que será excluído.
    usuario = next(
        (item for item in usuarios if item["id"] == usuario_id),
        None,
    )

    if usuario is None:
        return jsonify(erro="Usuário não encontrado"), 404

    # remove() exclui da lista o dicionário encontrado.
    usuarios.remove(usuario)

    # O status 200 permite devolver uma mensagem JSON confirmando a exclusão.
    return jsonify(mensagem="Usuário excluído"), 200


# Registra um tratador global para erros HTTP 404.
#
# Essa função será executada quando o cliente solicitar uma rota que não foi
# definida, como GET /produtos. Ela garante que o erro também seja devolvido
# em JSON, mantendo o padrão das demais respostas da API.
@app.errorhandler(404)
def rota_nao_encontrada(erro):
    """Retorna uma resposta JSON para rotas inexistentes."""

    # O Flask entrega o objeto do erro como argumento. Ele não é necessário
    # neste exemplo porque foi definida uma mensagem simples e padronizada.
    return jsonify(erro="Rota não encontrada"), 404


# Executa o servidor somente quando este arquivo é iniciado diretamente com:
#
#   python "Código colado.py"
#
# Se o arquivo for importado por outro programa, este bloco não será executado.
if __name__ == "__main__":
    # debug=True ativa recursos úteis durante o desenvolvimento:
    #   recarregamento automático quando o arquivo é alterado;
    #   apresentação detalhada de erros no navegador.
    #
    # O modo de depuração não deve ser utilizado em produção, pois pode
    # revelar informações internas da aplicação.
    app.run(debug=True)
