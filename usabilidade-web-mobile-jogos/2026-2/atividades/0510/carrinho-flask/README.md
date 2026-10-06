# Carrinho Flask + SQLite

Projeto da aula de 05/10: uma lojinha de material escolar com **vitrine**, **carrinho** e **cadastro de produtos**, feita com Flask e SQLite (só a biblioteca padrão `sqlite3`, sem ORM).

## Como funciona, em uma frase

A sessão do Flask guarda **apenas o código do carrinho** (`cart_id`, um UUID). Tudo o mais fica no banco `loja.db`:

```text
produtos                          itens_carrinho
─────────────────────             ────────────────────────────────────
id     TEXT  PK  ("p1")           cart_id     TEXT ─┐ PK (cart_id, produto_id)
nome   TEXT                       produto_id  TEXT ─┘ FK → produtos.id
preco  REAL                       quantidade  INTEGER  CHECK (quantidade > 0)
```

Cada navegador recebe um `cart_id` diferente, então cada aluno tem o seu carrinho.

## Arquivos

| Arquivo | O que é |
|---|---|
| `app.py` | O app Flask: rotas e funções auxiliares (`get_cart_id`, `contar_itens`, `listar_itens`, `calcular_total`) |
| `db.py` | `SCHEMA` (as duas tabelas), `SEED` (12 produtos, de `p1` a `p12`), `connect()` e `init_db()` |
| `templates/base.html` | Layout comum: cabeçalho com Vitrine, Cadastrar, o contador do carrinho e as mensagens `flash` |
| `templates/vitrine.html` | Cards dos produtos com o botão Adicionar |
| `templates/carrinho.html` | Tabela com −, +, OK e Remover, total, Esvaziar e o estado de carrinho vazio |
| `templates/cadastrar.html` | Formulário de novo produto (código, nome e preço) e a tabela de produtos |
| `atividades-carrinho-flask-sqlite.pdf` | As 3 atividades de extensão (só na cópia local e no Drive; não vai para o GitHub) |
| `loja.db` | Banco gerado automaticamente (não vai para o GitHub) |

## Como executar

Precisa do Python 3 com Flask.

```bash
cd usabilidade-web-mobile-jogos/2026-2/atividades/0510/carrinho-flask
python -m venv .venv
# Windows:      .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate
pip install flask
flask --app app run        # ou: python app.py
```

Abra `http://127.0.0.1:5000/`.

Ao iniciar, o `init_db()` cria `loja.db` com as tabelas e os 12 produtos, se ainda não existirem. Pode rodar várias vezes: o `INSERT OR IGNORE` não duplica, porque `id` é a chave primária. Quer começar do zero? Pare o servidor, apague `loja.db` e rode de novo.

## Rotas

| Método | Rota | O que faz | SQL principal |
|---|---|---|---|
| GET | `/` | Vitrine com todos os produtos | `SELECT … FROM produtos ORDER BY nome` |
| POST | `/add` | Adiciona 1 unidade (ou soma 1 se o produto já estiver no carrinho) | `INSERT … ON CONFLICT … DO UPDATE` (UPSERT) |
| GET | `/carrinho` | Itens com nome, preço, subtotal e total | `JOIN` + `SUM(preco * quantidade)` |
| POST | `/update` | Botões −, + e OK; quantidade 0 remove o item | `UPDATE` ou `DELETE` |
| POST | `/delete` | Remove um item | `DELETE … WHERE cart_id = ? AND produto_id = ?` |
| POST | `/esvaziar` | Esvazia o carrinho | `DELETE … WHERE cart_id = ?` |
| GET/POST | `/cadastrar` | Formulário de novo produto (**em construção**, ver abaixo) | — |

### `/cadastrar` está em construção

A página e o formulário já aparecem, mas a função `cadastrar()` em `app.py` ainda **não grava** o produto: enviar o formulário só mostra a página de novo. A tabela à direita também aparece vazia, porque a rota ainda não envia a lista `produtos` para o template. Completar essa rota (ler `request.form`, validar, fazer `INSERT` com `?` e listar os produtos) é o próximo passo do projeto.

O botão **Finalizar compra** do carrinho aparece desabilitado de propósito: pagamento e finalização estão fora do escopo desta aula (veja a Atividade 3).

## Conceitos que aparecem no código

- **Consultas parametrizadas:** todo valor vindo do usuário entra com `?`, nunca colado na string SQL. É isso que evita *SQL injection*.
- **`row_factory = sqlite3.Row`:** acessar colunas pelo nome (`p["preco"]`).
- **`PRAGMA foreign_keys = ON`:** o SQLite passa a conferir a chave estrangeira.
- **`COALESCE(SUM(...), 0)`:** um carrinho vazio dá total 0, e não `None`.
- **Sessão + `uuid4`:** identifica o carrinho sem precisar de login.
- **`flash(...)`:** mensagens de confirmação e de erro depois de cada ação.
- **Usabilidade:** contador no menu, confirmação antes de remover ou esvaziar, carrinho vazio com convite para voltar à vitrine e rótulo acessível (`aria-label`) no campo de quantidade.

## Atividades de extensão (PDF)

O PDF `atividades-carrinho-flask-sqlite.pdf` traz três atividades independentes. Todas partem deste projeto, e nenhuma vem com código-solução:

| Atividade | Nível | Tempo | O que você constrói |
|---|---|---|---|
| 1 — Buscador de produtos | Fácil | ~30 min | Campo de busca na vitrine com `WHERE nome LIKE ?` e mensagem quando nada é encontrado |
| 2 — Página de detalhes | Média | ~45 min | Coluna `descricao`, rota `GET /produto/<produto_id>`, `abort(404)` e link a partir da vitrine |
| 3 — Histórico de pedidos | Avançada | ~60 min | Tabelas `pedidos` e `itens_pedido`, rotas `POST /finalizar` e `GET /historico`, transação e o botão Finalizar habilitado |

Cada atividade tem passo a passo, *checkpoint* e uma lista do que entregar, com uma resposta escrita.

## Aviso

A `secret_key` do app é fixa e serve só para a aula (`…-nao-usar-em-producao`). Num site de verdade, ela precisa ser secreta e ficar fora do código.
