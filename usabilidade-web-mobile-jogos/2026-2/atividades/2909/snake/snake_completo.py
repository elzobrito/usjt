import pygame
import sys
import random

# =============================================================================
# SNAKE EM PYTHON — GABARITO COMPLETO (Etapas 1–14)
# Instalação: python -m pip install pygame-ce
# Execução:   python snake_gabarito.py
# =============================================================================

# --- Inicialização ---
pygame.init()

# --- Constantes ---
LARGURA = 800
ALTURA  = 600
TAMANHO = 20

PRETO   = (20,  20,  20)
VERDE   = (50,  205, 50)
VERMELHO= (220, 50,  50)
BRANCO  = (255, 255, 255)

# --- Tela ---
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake em Python")

# --- Fontes ---
fonte = pygame.font.SysFont("arial", 28)
fonte_grande= pygame.font.SysFont("arial", 50, bold=True)

# --- Relógio ---
relogio = pygame.time.Clock()


# =============================================================================
# FUNÇÕES  (Etapa 14 — Refatoração)
# =============================================================================

def gerar_comida():
    """Retorna uma posição aleatória alinhada à grade."""
    return [
        random.randrange(0, LARGURA, TAMANHO),
        random.randrange(0, ALTURA,  TAMANHO)
    ]


def desenhar_cobra(cobra):
    """Desenha cada bloco da cobra na tela."""
    for bloco in cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            (bloco[0], bloco[1], TAMANHO, TAMANHO)
        )


def desenhar_comida(comida):
    """Desenha o item de comida na tela."""
    pygame.draw.rect(
        tela,
        VERMELHO,
        (comida[0], comida[1], TAMANHO, TAMANHO)
    )


def desenhar_pontos(pontos):
    """Renderiza o placar no canto superior esquerdo."""
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (20, 20))


def game_over(pontos):
    """Exibe a tela de Game Over e aguarda o jogador fechar."""
    while True:
        tela.fill(PRETO)

        msg = fonte_grande.render("GAME OVER", True, VERMELHO)
        tela.blit(msg, (280, 220))

        pts = fonte.render(f"Pontos: {pontos}", True, BRANCO)
        tela.blit(pts, (330, 300))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# =============================================================================
# ESTADO INICIAL
# =============================================================================

# Etapa 5 — cobra representada como lista de posições [x, y]
cobra = [
    [400, 300],   # cabeça
    [380, 300],   # corpo
    [360, 300],   # cauda
]

# Etapa 3 — velocidade inicial (move para a direita)
velocidade_x = TAMANHO
velocidade_y = 0

# Etapa 6 — comida gerada aleatoriamente
comida = gerar_comida()

# Etapa 11 — pontuação
pontos = 0

# Etapa 12 — dificuldade progressiva (frames por segundo)
velocidade = 8

# Etapa 8 — controle do loop principal
rodando = True


# =============================================================================
# GAME LOOP
# =============================================================================

while rodando:

    # -------------------------------------------------------------------------
    # Etapa 4 / 10 — Eventos de teclado (com proteção contra inversão 180°)
    # -------------------------------------------------------------------------
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            # Só muda para vertical se está indo horizontal (velocidade_y == 0)
            if evento.key == pygame.K_UP and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = -TAMANHO

            elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = TAMANHO

            # Só muda para horizontal se está indo vertical (velocidade_x == 0)
            elif evento.key == pygame.K_LEFT and velocidade_x == 0:
                velocidade_x = -TAMANHO
                velocidade_y = 0

            elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                velocidade_x = TAMANHO
                velocidade_y = 0

    # -------------------------------------------------------------------------
    # Etapa 5 — Calcular nova posição da cabeça
    # -------------------------------------------------------------------------
    cabeca = cobra[0]
    nova_cabeca = [
        cabeca[0] + velocidade_x,
        cabeca[1] + velocidade_y
    ]

    # -------------------------------------------------------------------------
    # Etapa 8 — Colisão com a parede
    # -------------------------------------------------------------------------
    if (
        nova_cabeca[0] < 0
        or nova_cabeca[0] >= LARGURA
        or nova_cabeca[1] < 0
        or nova_cabeca[1] >= ALTURA
    ):
        rodando = False

    # -------------------------------------------------------------------------
    # Etapa 9 — Colisão com o próprio corpo (slicing: ignora a cabeça atual)
    # -------------------------------------------------------------------------
    if nova_cabeca in cobra[1:]:
        rodando = False

    # Insere nova cabeça no início da lista
    cobra.insert(0, nova_cabeca)

    # -------------------------------------------------------------------------
    # Etapa 7 — Detectar colisão com a comida
    # -------------------------------------------------------------------------
    if nova_cabeca == comida:
        comida     = gerar_comida()   # reposiciona a comida
        pontos    += 10               # Etapa 11 — pontuação
        velocidade += 0.5             # Etapa 12 — aumenta dificuldade
    else:
        cobra.pop()                   # remove a cauda (cobra não cresce)

    # -------------------------------------------------------------------------
    # Desenho
    # -------------------------------------------------------------------------
    tela.fill(PRETO)
    desenhar_cobra(cobra)
    desenhar_comida(comida)
    desenhar_pontos(pontos)
    pygame.display.update()

    # Etapa 12 — controla a velocidade do loop
    relogio.tick(velocidade)


# =============================================================================
# Etapa 13 — Tela de Game Over
# =============================================================================
game_over(pontos)
