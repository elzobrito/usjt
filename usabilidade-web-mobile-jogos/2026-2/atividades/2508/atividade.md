
## Parte 1 — A tabela de correlação (10 min)

Três colunas. Na coluna da direita, copie o código da rota (`R1`…`R6`) **ou** escreva `nenhuma`.

Rotas já registradas no servidor **didático** (não é o GitHub Pages):

```text
R1  GET    /                     home
R2  GET    /contato              página do formulário
R3  GET    /servico              página do serviço
R4  POST   /api/orcamentos       criar pedido de orçamento
R5  GET    /api/orcamentos       listar pedidos (se autorizado)
R6  GET    /api/orcamentos/{id}  consultar um protocolo
```

O que chega:

| # | Na tela / no código | Pedido HTTP que o navegador monta | Rota |
|---|---|---|---|
| 1 | Menu: `href="contato.html"` no site do Pages | | |
| 2 | Menu: `href="servico.html"` no site do Pages | | |
| 3 | Demo da aula: abrir `http://127.0.0.1:8000/` | | |
| 4 | Demo: `fetch('/api/solicitacoes', { method: 'POST', ... })` | | |
| 5 | Botão **Enviar pedido** do site de ontem: `<form action="contato.html" method="get">` | | |
| 6 | Mesmo botão, se o servidor tivesse a rota de criar orçamento | | |
| 7 | Pessoa cola na barra: `.../api/orcamentos/DEMO-0007` | | |
| 8 | Pessoa abre `.../contato#formulario` | | |
| 9 | `POST /contato` (alguém inventou no Postman) | | |
| 10 | `GET /api/orcamentos?status=aberta` | | |
| 11 | `DELETE /api/orcamentos/DEMO-0007` | | |
| 12 | `GET /enviarFormulario` | | |

