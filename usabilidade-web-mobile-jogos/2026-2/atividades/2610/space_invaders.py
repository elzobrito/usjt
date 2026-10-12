"""Space Invaders em Pygame — parte 5/5 — parte-05-ondas-variacao
Fechamento da trilha Pong -> Breakout -> Invaders. Sem assets externos.
Rode com:  python main.py
"""
import random
import pygame

LARGURA, ALTURA = 800, 600
FPS = 60
COR_FUNDO = (10, 10, 20)
COR_NAVE = (90, 220, 120)
COR_TIRO = (240, 240, 240)
COR_INVASOR = (230, 90, 200)
COR_TIRO_INIMIGO = (250, 120, 80)
COR_ESCUDO = (60, 160, 90)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Invaders")
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 32)
fonte_grande = pygame.font.Font(None, 64)


class Nave:
    def __init__(self):
        self.rect = pygame.Rect(LARGURA // 2 - 25, ALTURA - 50, 50, 20)
        self.vel = 360
        self.recarga = 0.0  # segundos até poder atirar de novo

    def atualizar(self, dt, tiros):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= int(self.vel * dt)
        if teclas[pygame.K_RIGHT]:
            self.rect.x += int(self.vel * dt)
        self.rect.clamp_ip(tela.get_rect())
        self.recarga -= dt
        if teclas[pygame.K_SPACE] and self.recarga <= 0:
            tiros.append(Tiro(self.rect.centerx, self.rect.top, -520))
            self.recarga = 0.35

    def desenhar(self):
        pygame.draw.rect(tela, COR_NAVE, self.rect)
        canhao = pygame.Rect(0, 0, 8, 10)
        canhao.midbottom = self.rect.midtop
        pygame.draw.rect(tela, COR_NAVE, canhao)


class Tiro:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x - 2, y - 12, 4, 12)
        self.y = float(self.rect.y)
        self.vel = vel  # negativo sobe, positivo desce

    def atualizar(self, dt):
        self.y += self.vel * dt
        self.rect.y = round(self.y)

    def fora(self):
        return self.rect.bottom < 0 or self.rect.top > ALTURA


class Formacao:
    """Todos os invasores andam juntos; se UM toca a borda, TODOS descem."""
    def __init__(self, velocidade=60):
        self.invasores = [pygame.Rect(90 + c * 60, 70 + l * 45, 36, 24)
                          for l in range(5) for c in range(10)]
        self.dx = velocidade
        self.x_acum = 0.0

    def atualizar(self, dt):
        self.x_acum += self.dx * dt
        passo = int(self.x_acum)
        self.x_acum -= passo
        for inv in self.invasores:
            inv.x += passo
        if any(inv.left <= 10 or inv.right >= LARGURA - 10 for inv in self.invasores):
            self.dx = -max(-400, min(400, self.dx * 1.04))  # vira e acelera (com teto)
            for inv in self.invasores:
                inv.y = min(inv.y + 18, ALTURA)
                inv.x += 4 if self.dx > 0 else -4  # sai da borda

    def desenhar(self):
        for inv in self.invasores:
            pygame.draw.rect(tela, COR_INVASOR, inv, border_radius=4)
            olho = pygame.Rect(0, 0, 6, 6)
            for ox in (-8, 8):
                olho.center = (inv.centerx + ox, inv.centery - 2)
                pygame.draw.rect(tela, COR_FUNDO, olho)


def criar_escudos():
    blocos = []
    for e in range(4):
        x0 = 110 + e * 170
        for l in range(3):
            for c in range(8):
                blocos.append(pygame.Rect(x0 + c * 10, ALTURA - 140 + l * 10, 10, 10))
    return blocos


def nova_partida():
    global nave, tiros, formacao, pontos, vidas, tiros_inimigos, escudos, estado, recarga_inimiga
    nave, tiros, formacao = Nave(), [], Formacao()
    pontos, vidas, tiros_inimigos, escudos = 0, 3, [], criar_escudos()
    estado, recarga_inimiga = "JOGANDO", 1.0
    onda = 1
    globals()["onda"] = onda


nave = Nave()
tiros = []
formacao = Formacao()
pontos = 0
nova_partida()

rodando = True
while rodando:
    dt = relogio.tick(FPS) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r and estado != "JOGANDO":
            nova_partida()

    if estado == "JOGANDO":
        nave.atualizar(dt, tiros)
        for t in tiros:
            t.atualizar(dt)
        formacao.atualizar(dt)

        # colisão tiro x invasor: monta listas NOVAS em vez de remover durante o for
        acertados = set()
        tiros_vivos = []
        for t in tiros:
            i = t.rect.collidelist(formacao.invasores)
            if i != -1 and i not in acertados:
                acertados.add(i)
                pontos += 10
            else:
                tiros_vivos.append(t)
        tiros = tiros_vivos
        formacao.invasores = [inv for i, inv in enumerate(formacao.invasores) if i not in acertados]

        # inimigos atiram a partir de um invasor aleatório
        recarga_inimiga -= dt
        if recarga_inimiga <= 0 and formacao.invasores:
            atirador = random.choice(formacao.invasores)
            tiros_inimigos.append(Tiro(atirador.centerx, atirador.bottom + 12, 300))
            recarga_inimiga = random.uniform(0.5, 1.3)
        for t in tiros_inimigos:
            t.atualizar(dt)
        # escudos absorvem tiros dos dois lados
        for lista in (tiros, tiros_inimigos):
            for t in lista[:]:  # iterar sobre CÓPIA permite remover
                j = t.rect.collidelist(escudos)
                if j != -1:
                    escudos.pop(j)
                    lista.remove(t)
        for t in tiros_inimigos[:]:
            if t.rect.colliderect(nave.rect):
                tiros_inimigos.remove(t)
                vidas -= 1
        tiros_inimigos = [t for t in tiros_inimigos if not t.fora()]
        if vidas <= 0 or any(inv.bottom >= nave.rect.top for inv in formacao.invasores):
            estado = "GAME_OVER"
        if not formacao.invasores:  # nova onda, mais rápida
            onda += 1
            formacao = Formacao(velocidade=60 + 25 * (onda - 1))
            tiros_inimigos.clear()

        tiros = [t for t in tiros if not t.fora()]

    tela.fill(COR_FUNDO)
    nave.desenhar()
    for t in tiros:
        pygame.draw.rect(tela, COR_TIRO, t.rect)
    formacao.desenhar()
    for t in tiros_inimigos:
        pygame.draw.rect(tela, COR_TIRO_INIMIGO, t.rect)
    for b in escudos:
        pygame.draw.rect(tela, COR_ESCUDO, b)
    tela.blit(fonte.render(f"Pontos: {pontos}", True, COR_TIRO), (12, 12))
    tela.blit(fonte.render(f"Vidas: {vidas}", True, COR_TIRO), (LARGURA - 110, 12))
    tela.blit(fonte.render(f"Onda: {onda}", True, COR_TIRO), (LARGURA // 2 - 40, 12))
    if estado != "JOGANDO":
        msg = "VOCÊ VENCEU!" if estado == "VITORIA" else "GAME OVER"
        txt = fonte_grande.render(msg, True, COR_TIRO)
        tela.blit(txt, txt.get_rect(center=(LARGURA // 2, ALTURA // 2)))
        dica = fonte.render("R para jogar de novo", True, COR_TIRO)
        tela.blit(dica, dica.get_rect(center=(LARGURA // 2, ALTURA // 2 + 50)))
    pygame.display.flip()

pygame.quit()