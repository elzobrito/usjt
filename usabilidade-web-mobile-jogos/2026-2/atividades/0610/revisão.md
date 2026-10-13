# Revisão A1: Usabilidade, Desenvolvimento Web, Mobile e Jogos

## Bloco 1: Interação humano-computador (IHC) e qualidades de uso

1. Pense num aplicativo de banco ou de entrega que você usa. Descreva uma situação em que ele "funciona", mas é ruim de usar. O que exatamente aparece na tela que causa o problema?
2. Explique a diferença entre usabilidade e acessibilidade, dando um exemplo de interface que tem uma dessas qualidades e não tem a outra.
3. O que é comunicabilidade? Mostre um ícone ou uma mensagem de erro que "não conversa" com o usuário e reescreva de um jeito que comunique melhor.
4. O que significa design universal? Proponha uma mudança num formulário de cadastro que beneficie ao mesmo tempo uma pessoa idosa, uma pessoa com baixa visão e alguém usando o celular na rua.

## Bloco 2: Eventos, estado e retorno ao usuário (Swing e Pygame)

5. No Dashboard em Swing, o que acontece entre o clique no botão "Relatórios" e a janela aparecer? Use a sequência: evento, o que o código faz, o que muda no estado, o que o usuário vê.
6. No Snake, o que muda no estado do jogo quando a cobra come a comida? E como o jogador percebe essa mudança?
7. Dê um exemplo de ação que deve pedir confirmação e outro que não deve, e justifique pelo custo do erro. Por que confirmação demais também atrapalha?

## Bloco 3: Web, formulário, GET e POST

8. Um formulário com `method="get"` envia os dados de que forma? Onde eles aparecem? Por que isso é um problema para dados como senha ou CPF?
9. Um site estático no GitHub Pages consegue salvar uma reserva? Explique o que falta para que o pedido do cliente seja realmente registrado.
10. Monte a tabela de rotas (método, caminho, intenção) para um sistema de agendamento de consultas, com as operações criar, consultar, remarcar e cancelar. Explique por que `/consultas` é um caminho melhor que `/salvarDados`.

## Bloco 4: Snake
- Altere o jogo para que, a cada 5 maçãs comidas, a cobra fique mais rápida. Mostre também na tela o nível atual ao lado da pontuação, por exemplo "Pontos: 7 | Nível: 2".

Dicas:

- A velocidade vem do valor passado para relogio.tick(10). Troque esse 10 por uma variável.
- Use a variável pontos para calcular o nível.
- Defina um limite de velocidade para o jogo não ficar impossível.
- Para entregar, explique em duas frases qual variável de estado mudou e como o jogador percebe essa mudança na tela.