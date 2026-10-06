# 29/09 — Jogo Snake em Python

Primeiro jogo da disciplina: a cobrinha clássica feita com **Pygame**. Você constrói o jogo em etapas e, no caminho, vê os elementos de qualquer jogo: o **loop principal**, os **eventos de teclado**, o **estado** (posições e velocidade), a **colisão** e o **desenho** de cada quadro.

## Arquivos

| Arquivo | O que é |
|---|---|
| `snake/snake.py` | Versão da aula, escrita em sequência e bem comentada: movimento com as setas, comida aleatória, a cobra cresce ao comer, pontos na tela e fim do jogo ao bater na parede |
| `snake/snake_completo.py` | Versão completa, organizada pelas **Etapas 1 a 14** (está marcada como gabarito no próprio arquivo) |
| [link.md](link.md) | Link para a pasta do Drive com os materiais da aula |

O que a versão completa acrescenta à da aula:

- não deixa a cobra virar 180° de uma vez (Etapa 10);
- colisão com o próprio corpo (Etapa 9);
- a velocidade aumenta a cada comida (Etapa 12);
- tela de **GAME OVER** com a pontuação;
- código refatorado em funções: `gerar_comida`, `desenhar_cobra`, `desenhar_comida`, `desenhar_pontos`, `game_over` (Etapa 14).

## Como executar

Precisa do Python 3 e do pacote **pygame-ce**. O código faz `import pygame`, e o `pygame-ce` fornece esse módulo.

```bash
pip install pygame-ce
cd usabilidade-web-mobile-jogos/2026-2/atividades/2909/snake
python snake.py
```

Para a versão completa: `python snake_completo.py`.

**Controles:** setas ↑ ↓ ← → para mudar de direção; feche a janela para sair.

## Números do jogo

A janela tem 800 × 600 pixels, e cada bloco da cobra mede 20 pixels. Na versão da aula, o jogo roda a 8 quadros por segundo (`relogio.tick(8)`). Na versão completa, começa em 8 e sobe 0,5 a cada comida. Cada comida vale 10 pontos.
