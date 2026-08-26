# Parte 1 — Três coisas que não são a mesma (5 min)

No caderno, copie e complete com o seu site:

Arquivo da tela:     contato.html
Pedido de página:    GET  /contato
Criação no sistema:  POST /api/_______________

Depois escreva uma frase para cada:

1. O arquivo HTML serve para quê?
2. O GET serve para quê?
3. O POST serve para quê?

Erro a evitar: chamar tudo de “página” ou escrever /enviarFormulario.

───

Parte 2 — A ação que o botão promete (5 min)

┌──────────────────────────────────────────┬────────────────────────────────────────────────┐
│ Campo                                    │ Você escreve                                   │
├──────────────────────────────────────────┼────────────────────────────────────────────────┤
│ Negócio do site                          │                                                │
├──────────────────────────────────────────┼────────────────────────────────────────────────┤
│ Pessoa                                   │                                                │
├──────────────────────────────────────────┼────────────────────────────────────────────────┤
│ O que ela tenta concluir                 │                                                │
├──────────────────────────────────────────┼────────────────────────────────────────────────┤
│ Frase ou botão que cria essa expectativa │                                                │
└──────────────────────────────────────────┴────────────────────────────────────────────────┘

Complete:

A pessoa acredita que __________, mas nesta versão o site apenas __________.

───

Parte 3 — Tabela de rotas (10 min)

Desenhe esta tabela. São quatro rotas, no máximo. Foco da aula: GET e POST.

┌───┬────────┬──────────────────┬──────────────────────────────────────────────┬─────────────────────────────────────────────────┐
│ # │ Método │ Caminho          │ Intenção                                     │ Quem chama (tela)                               │
├───┼────────┼──────────────────┼──────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ 1 │ GET    │                  │                                              │ menu Início                                     │
├───┼────────┼──────────────────┼──────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ 2 │ GET    │                  │                                              │ menu Contato                                    │
├───┼────────┼──────────────────┼──────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ 3 │ POST   │                  │                                              │ botão Enviar                                    │
├───┼────────┼──────────────────┼──────────────────────────────────────────────┼─────────────────────────────────────────────────┤
│ 4 │ GET    │                  │                                              │ “acompanhar pedido” — só se o site promete isso │
└───┴────────┴──────────────────┴──────────────────────────────────────────────┴─────────────────────────────────────────────────┘

Regras do caminho:

• substantivo do domínio: /encomendas, /orcamentos, /agendamentos, /reservas, /passeios
• não use verbo de tela: /enviar, /salvarFormulario, /mandaWhats
• GET e POST no mesmo recurso podem coexistir: consultar coleção ≠ criar item

Dado que você decide não coletar, e por quê (obrigatório):