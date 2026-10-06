# 31/08 — CRUD de usuários em Flask, passo a passo

Nesta aula o cadastro de usuários é construído **em etapas**. Cada pasta é um passo completo, que funciona sozinho e começa de onde o anterior parou. Os dados ficam numa **lista em memória**: ao reiniciar o servidor, os cadastros novos se perdem. Isso é de propósito, para não precisar de banco nesta primeira versão. O banco entra na [aula de 21/09](../2109/).

## As etapas

| Ordem | Pasta | O que acrescenta | Rotas |
|---|---|---|---|
| 0 | [logica/](logica/) | Aquecimento: duas variáveis em Python (`titulo` e `idade`). Não é Flask | — |
| 1 | [inicio/](inicio/) | Primeiro app Flask: `render_template` mostra uma tabela vazia | `GET /`, `GET /home` |
| 2 | [lista/](lista/) | A lista `usuarios` em Python aparece na tabela com `{% for %}` / `{% else %}` do Jinja | `GET /` |
| 3 | [cadastrar/](cadastrar/) | Formulário com `<label>`, `POST /usuarios`, validação do nome vazio, mensagens de sucesso/erro e redirect 303 | `GET /`, `POST /usuarios` |
| 4 | [final/](final/) | CRUD completo comentado: editar e excluir pela página e uma API JSON | ver abaixo |

Cada pasta tem um `main.py` e, a partir da etapa 1, um `crud_usuarios.html`. O app usa `template_folder="."`, ou seja, o HTML fica **na mesma pasta** do `main.py`, e não numa pasta `templates/`.

## Como executar

Precisa do Python 3 com Flask (`pip install flask`).

```bash
cd usabilidade-web-mobile-jogos/2026-2/atividades/3108/inicio   # troque pela etapa desejada
python main.py
```

Abra `http://127.0.0.1:5000/`. Para parar, use `Ctrl+C`.

## Rotas da versão final (`final/main.py`)

Página HTML:

| Método | Rota | O que faz |
|---|---|---|
| GET | `/` | Lista os usuários e mostra o formulário |
| POST | `/usuarios` | Cadastra (formulário) |
| POST | `/usuarios/<id>/editar` | Edita o nome |
| POST | `/usuarios/<id>/excluir` | Exclui |

API JSON (teste com Postman, Insomnia ou `curl`). Nesta versão o cadastro é só pelo formulário; a API lista, busca, atualiza e remove:

| Método | Rota | O que faz |
|---|---|---|
| GET | `/api` | Confirma que a API está no ar |
| GET | `/usuarios` | Lista todos em JSON |
| GET | `/usuarios/<id>` | Busca um usuário |
| PUT | `/usuarios/<id>` | Atualiza |
| DELETE | `/usuarios/<id>` | Remove |

Exemplo:

```bash
curl http://127.0.0.1:5000/usuarios
```

## Dicas de estudo

- Compare o `main.py` de uma etapa com o da seguinte: o que foi acrescentado?
- Na etapa 3, envie o formulário vazio (apague o `required` pelo DevTools) e veja a mensagem de erro do servidor.
- Reinicie o servidor depois de cadastrar alguém: o que acontece com o cadastro? Por quê?
