# 05/10 — Carrinho de compras com Flask + SQLite

Nesta aula você monta o carrinho de uma loja virtual: a **vitrine** lê os produtos do banco, o botão **Adicionar** grava o item no SQLite e a página do **carrinho** mostra quantidades, subtotais e o total, tudo calculado com SQL.

A sessão do Flask guarda **só o código do seu carrinho** (`cart_id`). Os produtos e os itens ficam nas tabelas `produtos` e `itens_carrinho`.

## Estrutura

```text
0510/
├── carrinho-flask/                 ← projeto completo da aula (comece aqui)
│   ├── app.py                      rotas da loja
│   ├── db.py                       schema, produtos iniciais e conexão
│   ├── templates/                  base, vitrine, carrinho, cadastrar
│   └── atividades-carrinho-flask-sqlite.pdf   3 atividades de extensão (fora do GitHub)
└── partes/
    └── parte-01-schema-vitrine/
        └── app.py                  Parte 1 isolada: só a vitrine lendo do banco
```

| Pasta | Para que serve |
|---|---|
| [carrinho-flask/](carrinho-flask/) | O projeto da aula. Tem o próprio [README](carrinho-flask/README.md), com como rodar, as rotas e as atividades |
| [partes/parte-01-schema-vitrine/](partes/parte-01-schema-vitrine/) | O `app.py` da **Parte 1**: cria as tabelas, cadastra os produtos iniciais e mostra a vitrine, ainda sem carrinho |

### Sobre a pasta `partes/`

Por enquanto só a Parte 1 está no repositório, e a pasta tem **apenas o `app.py`**. Ele importa `db.py` e usa uma pasta `templates/` que não estão ali. Mesmo copiando os de `carrinho-flask/`, não funciona direto: o `base.html` atual tem links para o carrinho e para o cadastro, rotas que a Parte 1 ainda não tem. Use esse arquivo para **ler e comparar** com o `app.py` completo: o que existe só na versão final?

> O PDF de atividades e o banco `loja.db` não vão para o GitHub (estão no `.gitignore`). O banco é recriado sozinho quando o app roda; o PDF fica com o professor e no Drive.

## Como executar

Veja o [README do carrinho-flask](carrinho-flask/README.md#como-executar).
