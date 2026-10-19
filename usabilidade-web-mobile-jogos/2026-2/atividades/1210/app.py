"""Pong em Pygame — parte 5/5 — parte-05-ia-variacao
Sem assets externos: tudo desenhado com pygame.draw e fonte padrão.
Rode com:  python main.py
"""
import random
import pygame

LARGURA, ALTURA = 800, 500
FPS = 60
COR_FUNDO = (15, 15, 25)
COR_OBJ = (235, 235, 235)
VEL_RAQUETE = 380  # pixels por segundo
VEL_BOLA = 300
PONTOS_VITORIA = 5

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 64)
fonte_peq = pygame.font.Font(None, 28)

esquerda = pygame.Rect(30, ALTURA // 2 - 45, 12, 90)
direita = pygame.Rect(LARGURA - 42, ALTURA // 2 - 45, 12, 90)
bola = pygame.Rect(LARGURA // 2 - 8, ALTURA // 2 - 8, 16, 16)
vx, vy = VEL_BOLA, VEL_BOLA * 0.6
bx, by = float(bola.x), float(bola.y)  # posição real em float (precisão com dt)
placar = [0, 0]
vencedor = None
contra_ia = True  # tecla 1 = contra IA, tecla 2 = dois jogadores


def sacar(direcao):
    """Recoloca a bola no centro e lança para a direção (+1 direita, -1 esquerda)."""
    global vx, vy, bx, by
    bx, by = LARGURA / 2 - 8, ALTURA / 2 - 8
    vx = VEL_BOLA * direcao
    vy = VEL_BOLA * random.uniform(-0.7, 0.7)


def mover_raquete(r, cima, baixo, dt):
    teclas = pygame.key.get_pressed()
    if teclas[cima]:
        r.y -= int(VEL_RAQUETE * dt)
    if teclas[baixo]:
        r.y += int(VEL_RAQUETE * dt)
    r.clamp_ip(tela.get_rect())  # não deixa sair da tela


def mover_ia(r, dt):
    """IA simples: segue a bola com velocidade limitada (dá para vencer)."""
    alvo = bola.centery
    passo = int(VEL_RAQUETE * 0.75 * dt)
    if r.centery < alvo - 10:
        r.y += passo
    elif r.centery > alvo + 10:
        r.y -= passo
    r.clamp_ip(tela.get_rect())


rodando = True
while rodando:
    dt = relogio.tick(FPS) / 1000  # segundos desde o último quadro

    # 1) EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r and vencedor:
            placar, vencedor = [0, 0], None
            sacar(random.choice((-1, 1)))
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_1:
            contra_ia = True
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_2:
            contra_ia = False

    # 2) ATUALIZAR
    mover_raquete(esquerda, pygame.K_w, pygame.K_s, dt)
    if contra_ia:
        mover_ia(direita, dt)
    else:
        mover_raquete(direita, pygame.K_UP, pygame.K_DOWN, dt)

    if vencedor is None:
        bx += vx * dt
        by += vy * dt
        bola.topleft = (round(bx), round(by))
        # rebate no topo e no fundo
        if bola.top <= 0 or bola.bottom >= ALTURA:
            vy = -vy
            by = min(max(by, 0), ALTURA - bola.height)
        # rebate nas raquetes: inverte E reposiciona (senão a bola "gruda")
        if bola.colliderect(esquerda) and vx < 0:
            vx = -vx
            bx = esquerda.right
            vx *= 1.05  # cada rebatida acelera um pouco
        if bola.colliderect(direita) and vx > 0:
            vx = -vx
            bx = direita.left - bola.width
            vx *= 1.05
        # saiu pela lateral
        if bola.right < 0:
            placar[1] += 1
            sacar(1)
        if bola.left > LARGURA:
            placar[0] += 1
            sacar(-1)
        if max(placar) >= PONTOS_VITORIA:
            vencedor = "Esquerda" if placar[0] > placar[1] else "Direita"

    # 3) DESENHAR
    tela.fill(COR_FUNDO)
    pygame.draw.line(tela, (70, 70, 90), (LARGURA // 2, 0), (LARGURA // 2, ALTURA), 2)
    pygame.draw.rect(tela, COR_OBJ, esquerda)
    pygame.draw.rect(tela, COR_OBJ, direita)
    pygame.draw.ellipse(tela, COR_OBJ, bola)
    txt = fonte.render(f"{placar[0]}   {placar[1]}", True, COR_OBJ)
    tela.blit(txt, txt.get_rect(midtop=(LARGURA // 2, 15)))
    if vencedor:
        msg = fonte_peq.render(f"{vencedor} venceu! R para reiniciar", True, COR_OBJ)
        tela.blit(msg, msg.get_rect(center=(LARGURA // 2, ALTURA // 2)))
    modo = "1: contra IA" if contra_ia else "2: dois jogadores"
    tela.blit(fonte_peq.render(modo, True, (150, 150, 170)), (10, ALTURA - 28))
    pygame.display.flip()

pygame.quit()
