import pygame
import sys
import random
pygame.init()
LARGURA = 800
ALTURA = 600
TAMANHO = 20
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

tela = pygame.display.set_mode(
    (LARGURA, ALTURA))

pygame.display.set_caption
("Jogo da Cobrinha")

relogio = pygame.time.Clock()

cobra =[
    [400.300], #caebeç
    [380.300], # corpo
    [360.300] # auda
]
# direlção inicial da cobra
velocidade_x = TAMANHO
velocidade_y = 0

# POTAÇAO INICIAL DA MAÇA
fonte = pygame.font.SysFont(
    "comicsans", 35)
comida = [
    random.randrange(
        0, LARGURA - TAMANHO, 
        TAMANHO
        ),
    random.randrange(
        0, ALTURA - TAMANHO, TAMANHO
        )
]

rodando = True


while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = -TAMANHO
            elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = TAMANHO
            elif evento.key == pygame.K_LEFT and velocidade_x == 0:
                velocidade_x = -TAMANHO
                velocidade_y = 0
            elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                velocidade_x = TAMANHO
                velocidade_y = 0

    # Atualiza a posição da cobra
    nova_cabeca = [
        cobra[0][0] + velocidade_x,
        cobra[0][1] + velocidade_y
    ]
    cobra.insert(0, nova_cabeca)

    # Verifica se a cobra comeu a comida
    if (cobra[0][0] == comida[0] and 
        cobra[0][1] == comida[1]):
        comida = [
            random.randrange(
                0, LARGURA - TAMANHO, 
                TAMANHO
            ),
            random.randrange(
                0, ALTURA - TAMANHO, 
                TAMANHO
            )
        ]
    else:
        cobra.pop()

    # Verifica colisão com as bordas ou consigo mesma
    if (cobra[0][0] < 0 or 
        cobra[0][0] >= LARGURA or 
        cobra[0][1] < 0 or 
        cobra[0][1] >= ALTURA or 
        cobra[0] in cobra[1:]):
        rodando = False

    # Desenha tudo na tela
    tela.fill(PRETO)
    for segmento in cobra:
        pygame.draw.rect(tela, VERDE, 
                         (segmento[0], segmento[1], TAMANHO, TAMANHO))
    pygame.draw.rect(tela, VERMELHO, 
                     (comida[0], comida[1], TAMANHO, TAMANHO))

    pygame.display.update()
    relogio.tick(10)