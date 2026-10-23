"""Snake em Pygame — protótipo com menu, jogo e tela de fim.

Instalação: python -m pip install pygame
Execução:   python snake_prototipo_setas.py

Controles:
  Menu / fim de jogo: clique no botão ou pressione Enter/Espaço.
  Durante o jogo:    setas direcionais.
"""

import random
import sys

import pygame

pygame.init()

# ------------------------------------------------------------
# CONFIGURAÇÃO
# ------------------------------------------------------------
LARGURA = 800
ALTURA = 600
TAMANHO = 20
ALTURA_CABECALHO = 60
FPS = 8

# A área de jogo começa abaixo do cabeçalho e ocupa toda a largura.
# 540 pixels / 20 = 27 linhas; 800 / 20 = 40 colunas.
AREA_JOGO = pygame.Rect(0, ALTURA_CABECALHO, LARGURA, ALTURA - ALTURA_CABECALHO)

FUNDO = (12, 16, 22)
FUNDO_TABULEIRO = (18, 24, 32)
GRADE = (34, 42, 52)
BRANCO = (242, 245, 248)
CINZA = (156, 168, 180)
VERDE = (73, 214, 132)
VERDE_CABECA = (32, 179, 103)
VERMELHO = (239, 88, 91)
BORDA = (53, 66, 78)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake em Python")
relogio = pygame.time.Clock()

fonte_titulo = pygame.font.SysFont("arial", 64, bold=True)
fonte_subtitulo = pygame.font.SysFont("arial", 34, bold=True)
fonte_normal = pygame.font.SysFont("arial", 25)
fonte_pequena = pygame.font.SysFont("arial", 20)
fonte_cabecalho = pygame.font.SysFont("arial", 26, bold=True)

BOTAO_INICIAR = pygame.Rect(285, 447, 230, 58)
BOTAO_REINICIAR = pygame.Rect(265, 402, 270, 60)


# ------------------------------------------------------------
# FUNÇÕES DE INTERFACE
# ------------------------------------------------------------
def escrever(texto, fonte, cor, centro=None, canto=None):
    """Escreve um texto centralizado ou a partir de uma posição."""
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect()
    if centro is not None:
        retangulo.center = centro
    elif canto is not None:
        retangulo.topleft = canto
    tela.blit(superficie, retangulo)


def desenhar_botao(retangulo, legenda):
    """Botão visual; retorna True se o mouse estiver sobre ele."""
    sobre = retangulo.collidepoint(pygame.mouse.get_pos())
    cor = (94, 233, 155) if sobre else VERDE
    pygame.draw.rect(tela, cor, retangulo, border_radius=12)
    escrever(legenda, fonte_normal, FUNDO, centro=retangulo.center)
    return sobre


def desenhar_seta(x, y, direcao, cor=BRANCO):
    """Desenha uma seta com linhas e um triângulo, sem depender de fonte Unicode."""
    direcoes = {
        "cima": (0, -1),
        "baixo": (0, 1),
        "esquerda": (-1, 0),
        "direita": (1, 0),
    }
    dx, dy = direcoes[direcao]
    ponta = (x + dx * 12, y + dy * 12)
    inicio = (x - dx * 11, y - dy * 11)
    base = (x + dx * 3, y + dy * 3)
    perpendicular = (-dy, dx)

    pygame.draw.line(tela, cor, inicio, base, width=3)
    pygame.draw.polygon(tela, cor, [
        ponta,
        (base[0] + perpendicular[0] * 6, base[1] + perpendicular[1] * 6),
        (base[0] - perpendicular[0] * 6, base[1] - perpendicular[1] * 6),
    ])


def desenhar_menu():
    """Tela inicial: instruções e o único botão Iniciar Jogo."""
    tela.fill(FUNDO)
    escrever("SNAKE", fonte_titulo, BRANCO, centro=(LARGURA // 2, 125))
    escrever("Use as setas para controlar a cobra", fonte_normal, CINZA,
             centro=(LARGURA // 2, 185))

    painel = pygame.Rect(185, 232, 430, 182)
    pygame.draw.rect(tela, FUNDO_TABULEIRO, painel, border_radius=14)
    pygame.draw.rect(tela, BORDA, painel, width=2, border_radius=14)

    escrever("CONTROLES", fonte_pequena, VERDE, centro=(400, 268))

    # Ícones vetoriais compatíveis com qualquer fonte/sistema operacional.
    desenhar_seta(222, 321, "cima")
    escrever("Cima", fonte_normal, BRANCO, canto=(247, 305))
    desenhar_seta(439, 321, "baixo")
    escrever("Baixo", fonte_normal, BRANCO, canto=(464, 305))

    desenhar_seta(222, 369, "esquerda")
    escrever("Esquerda", fonte_normal, BRANCO, canto=(247, 353))
    desenhar_seta(439, 369, "direita")
    escrever("Direita", fonte_normal, BRANCO, canto=(464, 353))

    desenhar_botao(BOTAO_INICIAR, "Iniciar jogo")
    escrever("Pressione Enter ou clique no botão", fonte_pequena, CINZA,
             centro=(400, 543))


def desenhar_jogo(cobra, comida, pontos):
    """Tabuleiro quase inteiro, com uma única pontuação no cabeçalho."""
    tela.fill(FUNDO)
    escrever("SNAKE", fonte_cabecalho, BRANCO, canto=(20, 15))

    marcador = fonte_cabecalho.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(marcador, (LARGURA - marcador.get_width() - 20, 15))

    pygame.draw.line(tela, BORDA, (0, ALTURA_CABECALHO - 1),
                     (LARGURA, ALTURA_CABECALHO - 1), 2)
    pygame.draw.rect(tela, FUNDO_TABULEIRO, AREA_JOGO)

    # Grade de 20x20 pixels, alinhada aos movimentos da cobra.
    for x in range(0, LARGURA + 1, TAMANHO):
        pygame.draw.line(tela, GRADE, (x, ALTURA_CABECALHO), (x, ALTURA))
    for y in range(ALTURA_CABECALHO, ALTURA + 1, TAMANHO):
        pygame.draw.line(tela, GRADE, (0, y), (LARGURA, y))

    pygame.draw.rect(tela, VERMELHO,
                     pygame.Rect(comida[0] + 2, comida[1] + 2,
                                 TAMANHO - 4, TAMANHO - 4),
                     border_radius=4)

    for indice, bloco in enumerate(cobra):
        cor = VERDE_CABECA if indice == 0 else VERDE
        pygame.draw.rect(tela, cor,
                         pygame.Rect(bloco[0] + 1, bloco[1] + 1,
                                     TAMANHO - 2, TAMANHO - 2),
                         border_radius=4)


def desenhar_fim(pontos, motivo):
    """Tela de encerramento separada do tabuleiro."""
    tela.fill(FUNDO)
    escrever("FIM DE JOGO", fonte_titulo, BRANCO, centro=(400, 184))
    escrever(motivo, fonte_normal, CINZA, centro=(400, 253))
    escrever(f"Pontos: {pontos}", fonte_subtitulo, VERDE,
             centro=(400, 325))
    desenhar_botao(BOTAO_REINICIAR, "Jogar novamente")
    escrever("Pressione Enter ou clique no botão", fonte_pequena, CINZA,
             centro=(400, 510))


# ------------------------------------------------------------
# REGRAS DO SNAKE
# ------------------------------------------------------------
def gerar_comida(cobra):
    """Escolhe uma célula livre; nunca coloca comida dentro da cobra."""
    ocupadas = {tuple(bloco) for bloco in cobra}
    livres = [
        (x, y)
        for y in range(ALTURA_CABECALHO, ALTURA, TAMANHO)
        for x in range(0, LARGURA, TAMANHO)
        if (x, y) not in ocupadas
    ]
    return list(random.choice(livres)) if livres else None


def iniciar_partida():
    """Reinicia cobra, velocidade, pontos e comida."""
    cobra = [[400, 300], [380, 300], [360, 300]]
    velocidade_x = TAMANHO
    velocidade_y = 0
    pontos = 0
    comida = gerar_comida(cobra)
    return cobra, velocidade_x, velocidade_y, pontos, comida


# ------------------------------------------------------------
# LOOP PRINCIPAL E ESTADOS
# ------------------------------------------------------------
estado = "menu"  # menu -> jogando -> fim
cobra, velocidade_x, velocidade_y, pontos, comida = iniciar_partida()
motivo_fim = ""
rodando = True

# Desenha a primeira tela ANTES de entrar no loop de eventos.
# Assim, o menu aparece mesmo que haja alguma dificuldade no loop.
desenhar_menu()
pygame.display.flip()
print(
    f"Snake: menu inicial desenhado; "
    f"SDL video driver = {pygame.display.get_driver()!r}; "
    f"resolucao = {tela.get_size()}",
    flush=True,
)

while rodando:
    mudou_direcao = False  # aceita apenas uma curva por movimento da cobra
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado == "menu" and BOTAO_INICIAR.collidepoint(evento.pos):
                cobra, velocidade_x, velocidade_y, pontos, comida = iniciar_partida()
                estado = "jogando"
            elif estado == "fim" and BOTAO_REINICIAR.collidepoint(evento.pos):
                cobra, velocidade_x, velocidade_y, pontos, comida = iniciar_partida()
                estado = "jogando"

        elif evento.type == pygame.KEYDOWN:
            if estado in ("menu", "fim") and evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                cobra, velocidade_x, velocidade_y, pontos, comida = iniciar_partida()
                estado = "jogando"

            elif estado == "jogando" and not mudou_direcao:
                # Não é permitido inverter a direção diretamente.
                direcao_anterior = (velocidade_x, velocidade_y)
                if evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_x, velocidade_y = 0, -TAMANHO
                elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_x, velocidade_y = 0, TAMANHO
                elif evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x, velocidade_y = -TAMANHO, 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x, velocidade_y = TAMANHO, 0
                mudou_direcao = (velocidade_x, velocidade_y) != direcao_anterior

    if estado == "jogando":
        cabeca = cobra[0]
        nova_cabeca = [cabeca[0] + velocidade_x, cabeca[1] + velocidade_y]

        # Colisão com bordas da área de jogo, sem invadir o cabeçalho.
        bateu_parede = not AREA_JOGO.collidepoint(nova_cabeca)
        comeu = nova_cabeca == comida

        # Se não comeu, a cauda se move neste turno; é permitido entrar
        # exatamente na posição que ela está deixando.
        corpo_que_colide = cobra if comeu else cobra[:-1]
        bateu_corpo = nova_cabeca in corpo_que_colide

        if bateu_parede or bateu_corpo:
            motivo_fim = "A cobra bateu na parede!" if bateu_parede else "A cobra bateu no próprio corpo!"
            estado = "fim"
        else:
            cobra.insert(0, nova_cabeca)
            if comeu:
                pontos += 10
                comida = gerar_comida(cobra)
                if comida is None:
                    motivo_fim = "Você ocupou todo o tabuleiro!"
                    estado = "fim"
            else:
                cobra.pop()

    if estado == "menu":
        desenhar_menu()
    elif estado == "jogando":
        desenhar_jogo(cobra, comida, pontos)
    else:
        desenhar_fim(pontos, motivo_fim)

    pygame.display.flip()
    relogio.tick(FPS if estado == "jogando" else 30)

pygame.quit()
sys.exit()
