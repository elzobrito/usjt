# 21/09 — CRUD de usuários com Flask e SQLite

É o mesmo cadastro de usuários da [aula de 31/08](../3108/), mas agora os dados ficam gravados num arquivo **SQLite** (`usuarios.db`). Você pode parar e reiniciar o servidor que os cadastros continuam lá.

## Arquivos

| Arquivo | O que é |
|---|---|
| `conexao.py` | Primeiro passo: abre e fecha uma conexão com o SQLite e mostra a versão. Cria `usuarios.db` **nesta pasta** (`2109/`) |
| `criar_tabela.py` | Cria a tabela `usuarios`, insere Alice, Bob e Charlie e lista o resultado. Usa outro arquivo de banco: `conexao.db` |
| `site/main.py` | **A aplicação:** CRUD completo, com página HTML e API JSON, gravando em `site/usuarios.db` |
| `site/crud_usuarios.html` | Template da página: formulário, mensagens e tabela com editar e excluir |
| `site/usuarios.db` | Banco gerado ao rodar o app (não vai para o GitHub; o app cria outro sozinho) |

## Como executar

Precisa do Python 3 com Flask (`pip install flask`). O `sqlite3` já vem com o Python.

**1. Testar a conexão**

```bash
cd usabilidade-web-mobile-jogos/2026-2/atividades/2109
python conexao.py
python criar_tabela.py
```

> Atenção: a coluna `nome` não é `UNIQUE`, então o `INSERT OR IGNORE` não impede repetição. Cada vez que você roda `criar_tabela.py`, Alice, Bob e Charlie são inseridos de novo.

**2. Rodar o site**

```bash
cd site
python main.py
```

Abra `http://127.0.0.1:5000/`. A tabela `usuarios` é criada automaticamente na primeira execução.

## Rotas (`site/main.py`)

Página HTML:

| Método | Rota | O que faz |
|---|---|---|
| GET | `/` | Lista os usuários do banco |
| POST | `/usuarios` | Cadastra |
| POST | `/usuarios/<id>/editar` | Edita |
| POST | `/usuarios/<id>/excluir` | Exclui |

API JSON:

| Método | Rota | O que faz |
|---|---|---|
| GET | `/api` | Confirma que a API está no ar |
| GET | `/api/usuarios` | Lista todos |
| GET | `/api/usuarios/<id>` | Busca um |
| POST | `/api/usuarios` | Cadastra (corpo JSON) |
| PUT | `/api/usuarios/<id>` | Atualiza (corpo JSON) |
| DELETE | `/api/usuarios/<id>` | Remove |

## O que estudar no código

- `abrir_conexao()` e `row_factory = sqlite3.Row`: acessar a coluna pelo nome (`usuario["nome"]`).
- `with closing(...)`: a conexão sempre é fechada.
- Consultas com `?` (parâmetros), nunca com o texto do usuário colado no SQL.
- `try/except sqlite3.Error`: o que a página mostra quando o banco falha.

Esta aula é a referência das próximas: a [22/09](../2209/) (produtos do seu site) e a [28/09](../2809/) (SOS Usabilidade).
