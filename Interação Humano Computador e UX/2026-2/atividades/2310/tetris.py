"""Protótipo jogável de Tetris em Pygame, baseado em wireframe de IHC/UX.

Execução:
    python -m pip install pygame-ce
    python tetris_prototipo.py

Teclado:
    ← / →      mover a peça
    ↓          acelerar a descida
    ↑          girar a peça
    ESPAÇO     queda instantânea
    C          guardar/trocar peça (HOLD)
    ENTER      iniciar / retomar
    P ou ESC   pausar / retomar
    R          reiniciar

Também é possível usar os botões da interface com o mouse.
O protótipo usa apenas Pygame e a biblioteca padrão do Python.
"""

from __future__ import annotations

from dataclasses import dataclass
import random
import sys

import pygame


# -----------------------------------------------------------------------------
# 1. CONFIGURAÇÃO VISUAL (wireframe em tons de cinza)
# -----------------------------------------------------------------------------
LARGURA, ALTURA = 1120, 820
FPS = 60
COLUNAS, LINHAS = 10, 20
CELULA = 30
CAMPO_X, CAMPO_Y = 410, 100
CAMPO_LARGURA = COLUNAS * CELULA
CAMPO_ALTURA = LINHAS * CELULA

ESQUERDA_X, ESQUERDA_LARGURA = 34, 330
DIREITA_X, DIREITA_LARGURA = 756, 330

FUNDO = (244, 244, 244)
PAINEL = (252, 252, 252)
BRANCO = (255, 255, 255)
TEXTO = (35, 35, 35)
TEXTO_SUAVE = (102, 102, 102)
BORDA = (47, 47, 47)
GRADE = (218, 218, 218)
DESTACADO = (85, 85, 85)

# Peças continuam monocromáticas, mas possuem tons distintos para identificação.
CORES_PECAS = {
    "I": (120, 120, 120),
    "O": (163, 163, 163),
    "T": (101, 101, 101),
    "S": (144, 144, 144),
    "Z": (126, 126, 126),
    "J": (178, 178, 178),
    "L": (91, 91, 91),
}

# Matrizes 4x4: X é uma célula ocupada e ponto é vazio.
FORMATOS = {
    "I": ("....", "XXXX", "....", "...."),
    "O": (".XX.", ".XX.", "....", "...."),
    "T": (".X..", "XXX.", "....", "...."),
    "S": (".XX.", "XX..", "....", "...."),
    "Z": ("XX..", ".XX.", "....", "...."),
    "J": ("X...", "XXX.", "....", "...."),
    "L": ("..X.", "XXX.", "....", "...."),
}


@dataclass
class Peca:
    tipo: str
    x: int = 3
    y: int = -1
    rotacao: int = 0


def celulas_peca(tipo: str, rotacao: int = 0) -> list[tuple[int, int]]:
    """Retorna as quatro células de um tetraminó em coordenadas locais."""
    coords = [
        (col, lin)
        for lin, linha in enumerate(FORMATOS[tipo])
        for col, caractere in enumerate(linha)
        if caractere == "X"
    ]
    if tipo == "O":
        return coords  # Quadrado não altera a forma quando gira.
    for _ in range(rotacao % 4):
        coords = [(3 - lin, col) for col, lin in coords]
    return coords


class Tetris:
    """Estado e regras do jogo, separados do desenho da interface."""

    def __init__(self) -> None:
        self.aleatorio = random.Random()
        self.saco: list[str] = []
        self.fila: list[str] = []
        self.novo_jogo(iniciar=False)

    def proxima_do_saco(self) -> str:
        """Sistema 7-bag: embaralha as sete peças para reduzir repetições."""
        if not self.saco:
            self.saco = list(FORMATOS)
            self.aleatorio.shuffle(self.saco)
        return self.saco.pop()

    def abastecer_fila(self) -> None:
        while len(self.fila) < 5:
            self.fila.append(self.proxima_do_saco())

    def novo_jogo(self, iniciar: bool = True) -> None:
        self.tabuleiro: list[list[str | None]] = [
            [None for _ in range(COLUNAS)] for _ in range(LINHAS)
        ]
        self.pontos = 0
        self.linhas_feitas = 0
        self.nivel = 1
        self.hold: str | None = None
        self.hold_disponivel = True
        self.saco = []
        self.fila = []
        self.abastecer_fila()
        self.peca = Peca(self.fila.pop(0))
        self.abastecer_fila()
        self.estado = "jogando" if iniciar else "pronto"
        self.tempo_queda = 0.0

    @property
    def intervalo_queda(self) -> float:
        """Aumenta gradualmente a dificuldade a cada dez linhas."""
        return max(0.085, 0.75 * (0.83 ** (self.nivel - 1)))

    def posicoes(
        self, peca: Peca | None = None, *, dx: int = 0, dy: int = 0,
        rotacao: int | None = None,
    ) -> list[tuple[int, int]]:
        p = peca if peca is not None else self.peca
        r = p.rotacao if rotacao is None else rotacao
        return [(p.x + col + dx, p.y + lin + dy)
                for col, lin in celulas_peca(p.tipo, r)]

    def valido(
        self, *, dx: int = 0, dy: int = 0, rotacao: int | None = None,
    ) -> bool:
        for x, y in self.posicoes(dx=dx, dy=dy, rotacao=rotacao):
            if x < 0 or x >= COLUNAS or y >= LINHAS:
                return False
            if y >= 0 and self.tabuleiro[y][x] is not None:
                return False
        return True

    def mover(self, dx: int, dy: int = 0, *, manual: bool = False) -> bool:
        if self.estado != "jogando":
            return False
        if self.valido(dx=dx, dy=dy):
            self.peca.x += dx
            self.peca.y += dy
            if manual and dy > 0:
                self.pontos += dy  # Pontos por descida manual.
            return True
        if dy > 0:
            self.fixar_peca()
        return False

    def girar(self) -> None:
        if self.estado != "jogando" or self.peca.tipo == "O":
            return
        nova_rotacao = (self.peca.rotacao + 1) % 4
        # Tentativas pequenas de deslocamento para permitir girar perto de bordas.
        for dx, dy in ((0, 0), (-1, 0), (1, 0), (-2, 0), (2, 0),
                       (0, -1), (-1, -1), (1, -1)):
            if self.valido(dx=dx, dy=dy, rotacao=nova_rotacao):
                self.peca.x += dx
                self.peca.y += dy
                self.peca.rotacao = nova_rotacao
                break

    def queda_rapida(self) -> None:
        if self.estado != "jogando":
            return
        distancia = 0
        while self.valido(dy=1):
            self.peca.y += 1
            distancia += 1
        self.pontos += 2 * distancia
        self.fixar_peca()

    def guardar(self) -> None:
        if self.estado != "jogando" or not self.hold_disponivel:
            return
        atual = self.peca.tipo
        if self.hold is None:
            self.hold = atual
            self.criar_proxima_peca()
        else:
            self.peca = Peca(self.hold)
            self.hold = atual
            if not self.valido():
                self.estado = "fim"
        self.hold_disponivel = False
        self.tempo_queda = 0

    def criar_proxima_peca(self) -> None:
        self.peca = Peca(self.fila.pop(0))
        self.abastecer_fila()
        if not self.valido():
            self.estado = "fim"

    def fixar_peca(self) -> None:
        for x, y in self.posicoes():
            if y < 0:
                self.estado = "fim"
                return
            self.tabuleiro[y][x] = self.peca.tipo

        restantes = [linha for linha in self.tabuleiro if not all(linha)]
        eliminadas = LINHAS - len(restantes)
        if eliminadas:
            self.tabuleiro = [[None] * COLUNAS for _ in range(eliminadas)] + restantes
            # Pontuação clássica aproximada para 1, 2, 3 ou 4 linhas.
            self.pontos += (0, 100, 300, 500, 800)[eliminadas] * self.nivel
            self.linhas_feitas += eliminadas
            self.nivel = 1 + self.linhas_feitas // 10

        self.hold_disponivel = True
        self.criar_proxima_peca()
        self.tempo_queda = 0

    def atualizar(self, dt: float) -> None:
        if self.estado != "jogando":
            return
        self.tempo_queda += dt
        if self.tempo_queda >= self.intervalo_queda:
            self.tempo_queda = 0
            self.mover(0, 1)

    def alternar_pausa(self) -> None:
        if self.estado == "jogando":
            self.estado = "pausado"
        elif self.estado == "pausado":
            self.estado = "jogando"
            self.tempo_queda = 0

    def iniciar_ou_retomar(self) -> None:
        if self.estado in ("pronto", "fim"):
            self.novo_jogo(iniciar=True)
        elif self.estado == "pausado":
            self.alternar_pausa()


# -----------------------------------------------------------------------------
# 2. INTERFACE: quadros, cartões, botões, controles e tabuleiro
# -----------------------------------------------------------------------------
class Interface:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Tetris — Protótipo Wireframe em Pygame")
        # Usa uma superfície lógica fixa e reduz a janela em monitores pequenos.
        # Assim, o layout permanece proporcional (útil em laboratórios).
        monitor = pygame.display.Info()
        largura_util = max(640, monitor.current_w - 80)
        altura_util = max(480, monitor.current_h - 110)
        escala = min(1.0, largura_util / LARGURA, altura_util / ALTURA)
        janela_tamanho = (round(LARGURA * escala), round(ALTURA * escala))
        self.janela = pygame.display.set_mode(janela_tamanho)
        self.tela = pygame.Surface((LARGURA, ALTURA)).convert()
        self.relogio = pygame.time.Clock()
        self.titulo = pygame.font.SysFont("dejavusans", 26, bold=True)
        self.subtitulo = pygame.font.SysFont("dejavusans", 20, bold=True)
        self.valor = pygame.font.SysFont("dejavusans", 40, bold=True)
        self.normal = pygame.font.SysFont("dejavusans", 18)
        self.pequena = pygame.font.SysFont("dejavusans", 15)
        self.botao_fonte = pygame.font.SysFont("dejavusans", 21, bold=True)
        self.jogo = Tetris()
        self.botoes = {
            "iniciar": pygame.Rect(ESQUERDA_X, 310, ESQUERDA_LARGURA, 56),
            "pausar": pygame.Rect(ESQUERDA_X, 379, ESQUERDA_LARGURA, 56),
            "reiniciar": pygame.Rect(ESQUERDA_X, 448, ESQUERDA_LARGURA, 56),
        }
        self.teclas_interface = {
            "esquerda": pygame.Rect(62, 587, 55, 42),
            "direita": pygame.Rect(132, 587, 55, 42),
            "baixo": pygame.Rect(62, 639, 55, 42),
            "cima": pygame.Rect(62, 691, 55, 42),
            "espaco": pygame.Rect(145, 691, 116, 42),
        }
        self.proximo_movimento: dict[int, float] = {}

    def coordenadas_logicas(self, posicao: tuple[int, int]) -> tuple[int, int]:
        largura, altura = self.janela.get_size()
        return (round(posicao[0] * LARGURA / largura),
                round(posicao[1] * ALTURA / altura))

    def escrever(
        self, texto: str, x: int, y: int, fonte: pygame.font.Font,
        *, cor: tuple[int, int, int] = TEXTO, centro: bool = False,
    ) -> None:
        superficie = fonte.render(texto, True, cor)
        destino = superficie.get_rect()
        if centro:
            destino.center = (x, y)
        else:
            destino.topleft = (x, y)
        self.tela.blit(superficie, destino)

    def painel(self, area: pygame.Rect, borda: int = 2) -> None:
        pygame.draw.rect(self.tela, PAINEL, area, border_radius=7)
        pygame.draw.rect(self.tela, BORDA, area, borda, border_radius=7)

    def desenhar_bloco(self, x: int, y: int, tamanho: int, tipo: str,
                      *, fantasma: bool = False) -> None:
        area = pygame.Rect(x, y, tamanho, tamanho)
        if fantasma:
            pygame.draw.rect(self.tela, (231, 231, 231), area.inflate(-5, -5))
            pygame.draw.rect(self.tela, (169, 169, 169), area.inflate(-5, -5), 1)
            return
        pygame.draw.rect(self.tela, CORES_PECAS[tipo], area.inflate(-2, -2))
        pygame.draw.rect(self.tela, (56, 56, 56), area.inflate(-2, -2), 2)

    def miniatura(self, tipo: str | None, area: pygame.Rect, tamanho: int = 26) -> None:
        if tipo is None:
            self.escrever("Sem peça guardada", area.centerx, area.centery,
                          self.normal, cor=TEXTO_SUAVE, centro=True)
            return
        coords = celulas_peca(tipo)
        xs, ys = [p[0] for p in coords], [p[1] for p in coords]
        largura = (max(xs) - min(xs) + 1) * tamanho
        altura = (max(ys) - min(ys) + 1) * tamanho
        x0 = area.centerx - largura // 2
        y0 = area.centery - altura // 2
        for x, y in coords:
            self.desenhar_bloco(x0 + (x - min(xs)) * tamanho,
                               y0 + (y - min(ys)) * tamanho, tamanho, tipo)

    def desenhar_lateral_esquerda(self) -> None:
        area_hold = pygame.Rect(ESQUERDA_X, 100, ESQUERDA_LARGURA, 190)
        self.painel(area_hold)
        self.escrever("HOLD", 57, 115, self.titulo)
        caixa = pygame.Rect(54, 156, 290, 118)
        pygame.draw.rect(self.tela, (248, 248, 248), caixa, border_radius=5)
        # Borda tracejada simples para representar a área de armazenamento.
        for x in range(caixa.left, caixa.right, 18):
            pygame.draw.line(self.tela, (155, 155, 155), (x, caixa.top),
                             (min(x + 9, caixa.right), caixa.top))
            pygame.draw.line(self.tela, (155, 155, 155), (x, caixa.bottom),
                             (min(x + 9, caixa.right), caixa.bottom))
        for y in range(caixa.top, caixa.bottom, 18):
            pygame.draw.line(self.tela, (155, 155, 155), (caixa.left, y),
                             (caixa.left, min(y + 9, caixa.bottom)))
            pygame.draw.line(self.tela, (155, 155, 155), (caixa.right, y),
                             (caixa.right, min(y + 9, caixa.bottom)))
        self.miniatura(self.jogo.hold, caixa)

        mouse = self.coordenadas_logicas(pygame.mouse.get_pos())
        for id_botao, area in self.botoes.items():
            ativo = not (id_botao == "pausar" and
                         self.jogo.estado in ("pronto", "fim"))
            principal = id_botao == "iniciar"
            cor = DESTACADO if principal else (235, 235, 235)
            if not ativo:
                cor = (241, 241, 241)
            elif area.collidepoint(mouse):
                cor = (60, 60, 60) if principal else (209, 209, 209)
            pygame.draw.rect(self.tela, cor, area, border_radius=6)
            pygame.draw.rect(self.tela, BORDA if ativo else (170, 170, 170),
                             area, 2, border_radius=6)
            texto = {
                "iniciar": "RETOMAR" if self.jogo.estado == "pausado" else "INICIAR",
                "pausar": "RETOMAR" if self.jogo.estado == "pausado" else "PAUSAR",
                "reiniciar": "REINICIAR",
            }[id_botao]
            self.escrever(texto, area.centerx, area.centery,
                          self.botao_fonte,
                          cor=BRANCO if principal else (TEXTO if ativo else (145, 145, 145)),
                          centro=True)

        painel_teclas = pygame.Rect(ESQUERDA_X, 521, ESQUERDA_LARGURA, 257)
        self.painel(painel_teclas)
        self.escrever("CONTROLES", 57, 535, self.subtitulo)
        mouse = self.coordenadas_logicas(pygame.mouse.get_pos())
        simbolos = {"esquerda": "←", "direita": "→", "baixo": "↓",
                    "cima": "↑", "espaco": "ESPAÇO"}
        for nome, area in self.teclas_interface.items():
            cor = (220, 220, 220) if area.collidepoint(mouse) else (248, 248, 248)
            pygame.draw.rect(self.tela, cor, area, border_radius=5)
            pygame.draw.rect(self.tela, BORDA, area, 2, border_radius=5)
            fonte = self.pequena if nome == "espaco" else self.subtitulo
            self.escrever(simbolos[nome], area.centerx, area.centery,
                          fonte, centro=True)
        self.escrever("Mover", 210, 597, self.normal)
        self.escrever("Descer", 134, 648, self.normal)
        self.escrever("Girar", 134, 699, self.normal)
        self.escrever("Queda", 267, 688, self.pequena)
        self.escrever("rápida", 267, 709, self.pequena)
        self.escrever("C = guardar peça", 62, 747, self.pequena,
                      cor=TEXTO_SUAVE)

    def cartao_estatistica(self, titulo: str, valor: int, y: int) -> None:
        area = pygame.Rect(DIREITA_X, y, DIREITA_LARGURA, 128)
        self.painel(area)
        self.escrever(titulo, area.left + 25, area.top + 13, self.subtitulo)
        self.escrever(str(valor), area.left + 25, area.top + 49, self.valor)

    def desenhar_lateral_direita(self) -> None:
        area = pygame.Rect(DIREITA_X, 100, DIREITA_LARGURA, 208)
        self.painel(area)
        self.escrever("PRÓXIMA PEÇA", area.left + 24, area.top + 15, self.subtitulo)
        caixa = pygame.Rect(area.left + 22, area.top + 58, area.width - 44, 130)
        pygame.draw.rect(self.tela, (247, 247, 247), caixa, border_radius=4)
        pygame.draw.rect(self.tela, (198, 198, 198), caixa, 1, border_radius=4)
        self.miniatura(self.jogo.fila[0], caixa, tamanho=33)

        self.cartao_estatistica("SCORE", self.jogo.pontos, 328)
        self.cartao_estatistica("LINHAS", self.jogo.linhas_feitas, 474)
        self.cartao_estatistica("NÍVEL", self.jogo.nivel, 620)

    def demo_tabuleiro(self) -> list[list[str | None]]:
        """Pilhas ilustrativas visíveis antes do primeiro clique em INICIAR."""
        exemplo: list[list[str | None]] = [[None] * COLUNAS for _ in range(LINHAS)]
        # Apenas uma composição visual do wireframe, não usada nas regras do jogo.
        desenho = {
            19: "JJLTT..LLS",
            18: "JJ.TT.LLSS",
            17: ".J.T..L.S.",
            16: ".J.....S..",
            15: "........S.",
        }
        for y, linha in desenho.items():
            for x, char in enumerate(linha):
                if char != ".":
                    exemplo[y][x] = char
        return exemplo

    def desenhar_tabuleiro(self) -> None:
        moldura = pygame.Rect(CAMPO_X - 4, CAMPO_Y - 4,
                              CAMPO_LARGURA + 8, CAMPO_ALTURA + 8)
        pygame.draw.rect(self.tela, BORDA, moldura, border_radius=2)
        area = pygame.Rect(CAMPO_X, CAMPO_Y, CAMPO_LARGURA, CAMPO_ALTURA)
        pygame.draw.rect(self.tela, (250, 250, 250), area)
        tabuleiro_visivel = (self.demo_tabuleiro() if self.jogo.estado == "pronto"
                             else self.jogo.tabuleiro)
        for y in range(LINHAS):
            for x in range(COLUNAS):
                px, py = CAMPO_X + x * CELULA, CAMPO_Y + y * CELULA
                pygame.draw.rect(self.tela, GRADE,
                                 (px, py, CELULA, CELULA), 1)
                tipo = tabuleiro_visivel[y][x]
                if tipo:
                    self.desenhar_bloco(px, py, CELULA, tipo)

        if self.jogo.estado == "pronto":
            # Peça em trânsito, apenas para dar aparência de jogo ao wireframe.
            demonstracao = Peca("L", x=3, y=3)
            for x, y in self.jogo.posicoes(demonstracao):
                self.desenhar_bloco(CAMPO_X + x * CELULA,
                                   CAMPO_Y + y * CELULA, CELULA, "L")
        elif self.jogo.estado != "fim":
            # Projeção da aterrissagem (ghost piece).
            distancia = 0
            while self.jogo.valido(dy=distancia + 1):
                distancia += 1
            if distancia > 0:
                for x, y in self.jogo.posicoes(dy=distancia):
                    if y >= 0:
                        self.desenhar_bloco(CAMPO_X + x * CELULA,
                                           CAMPO_Y + y * CELULA, CELULA,
                                           self.jogo.peca.tipo, fantasma=True)
            for x, y in self.jogo.posicoes():
                if y >= 0:
                    self.desenhar_bloco(CAMPO_X + x * CELULA,
                                       CAMPO_Y + y * CELULA, CELULA,
                                       self.jogo.peca.tipo)

        if self.jogo.estado in ("pronto", "pausado", "fim"):
            mensagens = {
                "pronto": ("PRONTO PARA JOGAR", "Clique em INICIAR ou ENTER"),
                "pausado": ("JOGO PAUSADO", "Pressione P para retomar"),
                "fim": ("FIM DE JOGO", "Clique em REINICIAR"),
            }
            linha_1, linha_2 = mensagens[self.jogo.estado]
            cartao = pygame.Rect(CAMPO_X + 12, CAMPO_Y + 248,
                                  CAMPO_LARGURA - 24, 98)
            pygame.draw.rect(self.tela, (252, 252, 252), cartao, border_radius=7)
            pygame.draw.rect(self.tela, BORDA, cartao, 2, border_radius=7)
            self.escrever(linha_1, cartao.centerx, cartao.top + 31,
                          self.pequena, centro=True)
            self.escrever(linha_2, cartao.centerx, cartao.top + 66,
                          self.pequena, cor=TEXTO_SUAVE, centro=True)

        self.escrever("TABULEIRO 10 × 20", CAMPO_X + CAMPO_LARGURA // 2,
                      CAMPO_Y + CAMPO_ALTURA + 22,
                      self.pequena, centro=True, cor=TEXTO_SUAVE)

    def desenhar(self) -> None:
        self.tela.fill(FUNDO)
        self.escrever("TETRIS", ESQUERDA_X, 32, self.titulo)
        self.escrever("protótipo de interface  •  Pygame", ESQUERDA_X + 126,
                      39, self.pequena, cor=TEXTO_SUAVE)
        self.escrever("ENTER iniciar    P pausar    R reiniciar", DIREITA_X,
                      42, self.pequena, cor=TEXTO_SUAVE)
        self.desenhar_lateral_esquerda()
        self.desenhar_lateral_direita()
        self.desenhar_tabuleiro()
        pygame.transform.smoothscale(self.tela, self.janela.get_size(), self.janela)
        pygame.display.flip()

    def acionar_controle(self, nome: str) -> None:
        if nome == "esquerda":
            self.jogo.mover(-1)
        elif nome == "direita":
            self.jogo.mover(1)
        elif nome == "baixo":
            self.jogo.mover(0, 1, manual=True)
        elif nome == "cima":
            self.jogo.girar()
        elif nome == "espaco":
            self.jogo.queda_rapida()

    def clique(self, posicao: tuple[int, int]) -> None:
        for nome, area in self.botoes.items():
            if area.collidepoint(posicao):
                if nome == "iniciar":
                    self.jogo.iniciar_ou_retomar()
                elif nome == "pausar":
                    self.jogo.alternar_pausa()
                else:
                    self.jogo.novo_jogo()
                return
        for nome, area in self.teclas_interface.items():
            if area.collidepoint(posicao):
                self.acionar_controle(nome)
                return

    def tecla(self, key: int) -> None:
        if key == pygame.K_RETURN:
            self.jogo.iniciar_ou_retomar()
        elif key in (pygame.K_p, pygame.K_ESCAPE):
            self.jogo.alternar_pausa()
        elif key == pygame.K_r:
            self.jogo.novo_jogo()
        elif self.jogo.estado == "jogando":
            if key == pygame.K_LEFT:
                self.acionar_controle("esquerda")
            elif key == pygame.K_RIGHT:
                self.acionar_controle("direita")
            elif key == pygame.K_DOWN:
                self.acionar_controle("baixo")
            elif key == pygame.K_UP:
                self.acionar_controle("cima")
            elif key == pygame.K_SPACE:
                self.acionar_controle("espaco")
            elif key in (pygame.K_c, pygame.K_LSHIFT, pygame.K_RSHIFT):
                self.jogo.guardar()

        if key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
            self.proximo_movimento[key] = pygame.time.get_ticks() / 1000 + 0.17

    def repetir_movimento(self) -> None:
        if self.jogo.estado != "jogando":
            return
        agora = pygame.time.get_ticks() / 1000
        pressionadas = pygame.key.get_pressed()
        for key, nome in ((pygame.K_LEFT, "esquerda"),
                          (pygame.K_RIGHT, "direita"),
                          (pygame.K_DOWN, "baixo")):
            if pressionadas[key] and key in self.proximo_movimento:
                if agora >= self.proximo_movimento[key]:
                    self.acionar_controle(nome)
                    self.proximo_movimento[key] = agora + (0.050 if key == pygame.K_DOWN else 0.085)

    def executar(self) -> None:
        while True:
            dt = min(self.relogio.tick(FPS) / 1000, 0.10)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.KEYDOWN:
                    self.tecla(evento.key)
                elif evento.type == pygame.KEYUP:
                    self.proximo_movimento.pop(evento.key, None)
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    self.clique(self.coordenadas_logicas(evento.pos))
            self.repetir_movimento()
            self.jogo.atualizar(dt)
            self.desenhar()


def main() -> None:
    try:
        Interface().executar()
    except pygame.error as erro:
        print(f"Não foi possível abrir a janela do Pygame: {erro}", file=sys.stderr)
        raise SystemExit(1) from erro


if __name__ == "__main__":
    main()