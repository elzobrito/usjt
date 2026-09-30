import pygame
import sys
import random

pygame.init()

LARGURA = 800
ALTURA = 600
TAMANHO = 20

VERMELHO = (255, 0, 0)
PRETO = (20, 20, 20)
VERDE = (0, 255, 0)


# Cria a janela
tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)

pygame.display.set_caption(
    "Snake em Python"
)

relogio = pygame.time.Clock()


# Cobra
cobra = [
    [400, 300],  # cabeça
    [380, 300],  # corpo
    [360, 300]   # cauda
]


# Direção inicial
velocidade_x = TAMANHO
velocidade_y = 0


# Comida
comida = [
    random.randrange(0, LARGURA, TAMANHO),
    random.randrange(0, ALTURA, TAMANHO)
]


rodando = True


while rodando:

    # --------------------------------
    # EVENTOS
    # --------------------------------

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -TAMANHO

            elif evento.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = TAMANHO

            elif evento.key == pygame.K_LEFT:
                velocidade_x = -TAMANHO
                velocidade_y = 0

            elif evento.key == pygame.K_RIGHT:
                velocidade_x = TAMANHO
                velocidade_y = 0


    # --------------------------------
    # MOVIMENTO DA COBRA
    # --------------------------------

    cabeca = cobra[0]

    nova_cabeca = [
        cabeca[0] + velocidade_x,
        cabeca[1] + velocidade_y
    ]


    # --------------------------------
    # COLISÃO COM AS PAREDES
    # --------------------------------

    if (
        nova_cabeca[0] < 0
        or nova_cabeca[0] >= LARGURA
        or nova_cabeca[1] < 0
        or nova_cabeca[1] >= ALTURA
    ):
        rodando = False
        continue


    # --------------------------------
    # ADICIONA NOVA CABEÇA
    # --------------------------------

    cobra.insert(0, nova_cabeca)


    # --------------------------------
    # VERIFICA SE COMEU
    # --------------------------------

    if nova_cabeca == comida:

        # Gera uma nova comida
        comida = [
            random.randrange(
                0,
                LARGURA,
                TAMANHO
            ),
            random.randrange(
                0,
                ALTURA,
                TAMANHO
            )
        ]

        # IMPORTANTE:
        #
        # Não fazemos cobra.pop()
        #
        # Portanto a cobra fica
        # com um bloco a mais.

    else:

        # Se não comeu,
        # remove a cauda.
        cobra.pop()


    # --------------------------------
    # DESENHO
    # --------------------------------

    tela.fill(PRETO)


    # Desenha comida
    pygame.draw.rect(
        tela,
        VERMELHO,
        (
            comida[0],
            comida[1],
            TAMANHO,
            TAMANHO
        )
    )


    # Desenha todos os blocos da cobra
    for bloco in cobra:

        pygame.draw.rect(
            tela,
            VERDE,
            (
                bloco[0],
                bloco[1],
                TAMANHO,
                TAMANHO
            )
        )


    pygame.display.update()

    relogio.tick(8)


pygame.quit()
sys.exit()