"""Tetris colorido para aulas de IHC e UX — Pygame.

Instalar: python -m pip install pygame-ce
Executar: python tetris.py

Setas: movimentar, descer e girar | Espaço: queda rápida
C/Shift: guardar peça | Enter: iniciar/retomar | P/Esc: pausar | R: reiniciar
M: alternar efeitos | N: alternar música | +/-: volume música | [ / ]: volume efeitos.
A música e os efeitos são sintetizados no próprio código, sem arquivos externos.
Os botões e a área HOLD também respondem ao mouse.

A lógica do jogo foi mantida separada da apresentação visual.
Tabuleiro didático ampliado: 14 colunas × 20 linhas, células de 30 px.
Laterais mantêm o alinhamento da versão colorida anterior.
"""

from __future__ import annotations
from dataclasses import dataclass
from array import array
import re
import math
import random
import sys
from typing import Callable
import pygame

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA TELA E TEMA COLORIDO
# -----------------------------------------------------------------------------
LARGURA, ALTURA = 1240, 780
FPS = 60
COLUNAS, LINHAS = 14, 20
CELULA = 30
CAMPO_X, CAMPO_Y = 410, 74
CAMPO_LARGURA = COLUNAS * CELULA
CAMPO_ALTURA = LINHAS * CELULA
ESQUERDA_X, ESQUERDA_LARGURA = 34, 330
DIREITA_X, DIREITA_LARGURA = 876, 330

# A paleta fica concentrada aqui para facilitar experimentos de UX.
FUNDO = (11, 18, 31)
FUNDO_CABECALHO = (16, 26, 43)
PAINEL = (24, 37, 57)
PAINEL_INTERNO = (13, 24, 41)
BRANCO = (248, 250, 252)
TEXTO = (236, 243, 251)
TEXTO_SUAVE = (157, 175, 199)
BORDA = (64, 85, 111)
GRADE = (33, 48, 68)
CIANO = (34, 211, 238)
VERDE = (74, 222, 128)
AMARELO = (250, 204, 21)
LARANJA = (251, 146, 60)
VERMELHO = (251, 113, 133)
AZUL = (96, 165, 250)
ROXO = (192, 132, 252)
BOTAO_NEUTRO = (50, 69, 94)
BOTAO_INATIVO = (38, 52, 71)

CORES_PECAS = {
    "I": CIANO,
    "O": AMARELO,
    "T": ROXO,
    "S": VERDE,
    "Z": VERMELHO,
    "J": AZUL,
    "L": LARANJA,
}

FORMATOS = {
    "I": ("....", "XXXX", "....", "...."),
    "O": (".XX.", ".XX.", "....", "...."),
    "T": (".X..", "XXX.", "....", "...."),
    "S": (".XX.", "XX..", "....", "...."),
    "Z": ("XX..", ".XX.", "....", "...."),
    "J": ("X...", "XXX.", "....", "...."),
    "L": ("..X.", "XXX.", "....", "...."),
}


def clarear(cor: tuple[int, int, int], quantidade: int = 24) -> tuple[int, int, int]:
    """Clareia uma cor RGB sem ultrapassar 255."""
    return tuple(min(255, canal + quantidade) for canal in cor)


def escurecer(cor: tuple[int, int, int], fator: float = 0.72) -> tuple[int, int, int]:
    return tuple(round(canal * fator) for canal in cor)


# -----------------------------------------------------------------------------
# EFEITOS SONOROS: síntese de ondas retrô, sem arquivos externos
# -----------------------------------------------------------------------------
class AudioRetro:
    """Sintetiza efeitos em memória e reproduz via pygame.mixer.Sound.

    O jogo funciona normalmente mesmo em computadores sem dispositivo de áudio.
    """

    MELODIAS = {
        "iniciar": [(523, 0.070), (659, 0.070), (784, 0.110)],
        "mover": [(390, 0.035)],
        "descer": [(250, 0.040)],
        "girar": [(660, 0.055), (880, 0.075)],
        "queda": [(510, 0.050), (340, 0.065), (180, 0.110)],
        "fixar": [(190, 0.075)],
        "linha": [(523, 0.065), (659, 0.065), (784, 0.090), (1047, 0.110)],
        "tetris": [(392, 0.075), (523, 0.075), (659, 0.075),
                   (784, 0.095), (1047, 0.200)],
        "guardar": [(520, 0.075), (390, 0.085)],
        "pausa": [(370, 0.080), (260, 0.100)],
        "retomar": [(330, 0.075), (550, 0.100)],
        "fim": [(440, 0.120), (330, 0.140), (247, 0.160), (165, 0.250)],
    }
    VOLUMES = {
        "mover": 0.10, "descer": 0.075, "girar": 0.20,
        "fixar": 0.17, "queda": 0.24, "linha": 0.33,
        "tetris": 0.36, "guardar": 0.21, "iniciar": 0.25,
        "pausa": 0.20, "retomar": 0.20, "fim": 0.25,
    }

    def __init__(self) -> None:
        self.ativado = True
        self.disponivel = False
        self.volume_geral = 1.0
        self.sons: dict[str, pygame.mixer.Sound] = {}
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
            config = pygame.mixer.get_init()
            if config is None:
                return
            frequencia, formato, canais = config
            # Precisamos de amostras PCM mono de 16 bits com sinal.
            if formato != -16 or canais != 1:
                print("Áudio indisponível: mixer não está em PCM 16-bit mono.")
                return
            for nome, notas in self.MELODIAS.items():
                som = pygame.mixer.Sound(buffer=self.sintetizar(notas, frequencia))
                som.set_volume(self.VOLUMES.get(nome, 0.20) * self.volume_geral)
                self.sons[nome] = som
            pygame.mixer.set_num_channels(max(24, pygame.mixer.get_num_channels()))
            # Quatro primeiros canais dedicados à trilha, sem roubo pelos efeitos.
            pygame.mixer.set_reserved(5)
            self.disponivel = True
        except pygame.error as erro:
            print(f"Áudio desabilitado (sem dispositivo ou mixer): {erro}")

    @staticmethod
    def sintetizar(notas: list[tuple[int, float]], taxa: int) -> bytes:
        """Gera um pequeno sinal PCM com ataque/decaimento para evitar cliques."""
        amostras = array("h")
        for hz, duracao in notas:
            total = max(1, int(duracao * taxa))
            ataque = max(1, int(taxa * 0.004))
            soltura = max(1, int(taxa * 0.015))
            for indice in range(total):
                fase = (indice * hz / taxa) % 1.0
                # Onda quadrada suavizada e harmônico de seno: efeito 8-bit.
                pulso = math.tanh(3.0 * math.sin(2 * math.pi * fase))
                seno = math.sin(2 * math.pi * fase)
                envelope = min(1.0, indice / ataque,
                               (total - 1 - indice) / soltura)
                valor = int(12000 * (0.75 * pulso + 0.25 * seno) * envelope)
                amostras.append(max(-32768, min(32767, valor)))
        if sys.byteorder == "big":
            amostras.byteswap()
        return amostras.tobytes()

    def tocar(self, nome: str) -> None:
        if self.ativado and self.disponivel:
            som = self.sons.get(nome)
            if som is not None:
                som.play()

    def alternar(self) -> None:
        if not self.disponivel:
            return
        self.ativado = not self.ativado
        if self.ativado:
            self.tocar("retomar")
        else:
            # Não interrompe os canais 0–4, reservados para a música.
            for i in range(5, pygame.mixer.get_num_channels()):
                pygame.mixer.Channel(i).stop()

    def mudar_volume(self, delta: float) -> None:
        if not self.disponivel:
            return
        self.volume_geral = round(max(0.0, min(1.5, self.volume_geral + delta)), 2)
        for nome, som in self.sons.items():
            som.set_volume(min(1.0, self.VOLUMES.get(nome, 0.20) * self.volume_geral))


# -----------------------------------------------------------------------------
# MÚSICA ORIGINAL: 16 COMPASSOS × 4 TEMPOS = 30 s A 128 BPM
# -----------------------------------------------------------------------------
class TrilhaChiptune:
    """Sequenciador de música retrô: melodia, baixo, arpejo e bateria.

    Cada compasso possui oito colcheias. O sequenciamento usa os frames
    do Pygame, com canais reservados para não interromper os efeitos.
    A partitura é original e pode ser editada diretamente na constante MELODIA.
    """

    BPM_INICIAL = 128
    MAX_BPM = 168
    COMPASSOS = 16
    # Cada string = um compasso 4/4, oito passos de colcheia.
    # '-' significa silêncio. Notação científica: C4, F#5 etc.
    MELODIA = (
        "E5 - B4 D5 E5 - G5 F#5",
        "E5 D5 B4 - A4 B4 D5 -",
        "G4 B4 D5 E5 D5 B4 A4 -",
        "G4 A4 B4 - D5 - B4 -",
        "E5 - G5 F#5 E5 D5 B4 -",
        "C5 D5 E5 - B4 D5 A4 -",
        "B4 C5 D5 E5 F#5 E5 D5 B4",
        "A4 - B4 D5 E5 - - -",
        "G5 - F#5 E5 D5 B4 E5 -",
        "F#5 - E5 D5 C5 B4 A4 -",
        "E5 G5 A5 - G5 F#5 E5 D5",
        "B4 D5 E5 F#5 E5 - B4 -",
        "C5 E5 G5 E5 D5 B4 A4 -",
        "B4 D5 F#5 D5 C5 B4 A4 -",
        "G4 B4 D5 F#5 E5 D5 B4 A4",
        "E5 - B4 - G4 - E4 -",
    )
    # Raiz, quinta e três notas de arpejo por compasso.
    HARMONIA = (
        ("E2", "B2", ("E4", "G4", "B4")),
        ("C2", "G2", ("C4", "E4", "G4")),
        ("G2", "D3", ("G3", "B3", "D4")),
        ("D2", "A2", ("D4", "F#4", "A4")),
        ("E2", "B2", ("E4", "G4", "B4")),
        ("C2", "G2", ("C4", "E4", "G4")),
        ("A2", "E3", ("A3", "C4", "E4")),
        ("B2", "F#3", ("B3", "D4", "F#4")),
        ("G2", "D3", ("G3", "B3", "D4")),
        ("D2", "A2", ("D4", "F#4", "A4")),
        ("E2", "B2", ("E4", "G4", "B4")),
        ("B2", "F#3", ("B3", "D4", "F#4")),
        ("C2", "G2", ("C4", "E4", "G4")),
        ("D2", "A2", ("D4", "F#4", "A4")),
        ("B2", "F#3", ("B3", "D4", "F#4")),
        ("E2", "B2", ("E4", "G4", "B4")),
    )
    NOTAS = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
             "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}

    def __init__(self, disponivel: bool) -> None:
        self.disponivel = disponivel
        self.ativado = True
        self.rodando = False
        self.pausada = False
        self.volume = 0.46  # Volume independente dos efeitos.
        self.passo = 0
        self.acumulado = 0.0
        self.bpm = self.BPM_INICIAL
        self.partitura = [nota for compasso in self.MELODIA for nota in compasso.split()]
        assert len(self.MELODIA) == self.COMPASSOS
        assert len(self.HARMONIA) == self.COMPASSOS
        assert len(self.partitura) == self.COMPASSOS * 8
        assert all(len(compasso.split()) == 8 for compasso in self.MELODIA)
        self.cache: dict[tuple[str, str], pygame.mixer.Sound] = {}
        self.canais: list[pygame.mixer.Channel] = []
        if self.disponivel:
            try:
                self.taxa = pygame.mixer.get_init()[0]
                self.canais = [pygame.mixer.Channel(i) for i in range(5)]
                self._ajustar_volumes()
                self.cache.update({(tipo, tipo): self._criar_som_bateria(tipo)
                                   for tipo in ("kick", "snare", "hat")})
            except (pygame.error, TypeError) as erro:
                print(f"Trilha musical indisponível: {erro}")
                self.disponivel = False
                self.canais = []

    @classmethod
    def frequencia(cls, nome: str) -> float:
        m = re.fullmatch(r"([A-G]#?)([1-7])", nome)
        if m is None or m[1] not in cls.NOTAS:
            raise ValueError(f"Nota musical inválida: {nome!r}")
        midi = (int(m[2]) + 1) * 12 + cls.NOTAS[m[1]]
        return 440.0 * (2.0 ** ((midi - 69) / 12.0))

    @staticmethod
    def _pcm(valores: array) -> bytes:
        if sys.byteorder == "big":
            valores.byteswap()
        return valores.tobytes()

    def _criar_som_nota(self, nome: str, timbre: str) -> pygame.mixer.Sound:
        """Gera PCM assinado 16-bit mono com envelope anti-clique."""
        duracao = {"lead": 0.172, "bass": 0.34, "arp": 0.105}[timbre]
        hz = self.frequencia(nome)
        total = int(duracao * self.taxa)
        saida = array('h')
        ganho = {"lead": 8000, "bass": 11000, "arp": 6800}[timbre]
        for i in range(total):
            t = i / self.taxa
            fase = (hz * t) % 1.0
            if timbre == "lead":
                # Pulso 25%: timbre de sintetizador portátil.
                onda = (1.0 if fase < 0.25 else -0.333) + 0.13 * math.sin(2 * math.pi * fase)
            elif timbre == "bass":
                # Triangular + subgrave para não mascarar a melodia.
                onda = (4 * abs(fase - 0.5) - 1) * 0.76 + 0.24 * math.sin(2 * math.pi * fase)
            else:
                # Arpejo com decaimento rápido.
                onda = 2 * abs(2 * fase - 1) - 1
            ataque = min(1.0, i / max(1, int(0.004 * self.taxa)))
            soltura = min(1.0, (total - 1 - i) / max(1, int(0.022 * self.taxa)))
            decaimento = (1 - 0.7 * (i / total)) if timbre == "arp" else 1.0
            saida.append(int(max(-32767, min(32767, ganho * onda * ataque * soltura * decaimento))))
        return pygame.mixer.Sound(buffer=self._pcm(saida))

    def _criar_som_bateria(self, tipo: str) -> pygame.mixer.Sound:
        duracao = {"kick": 0.15, "snare": 0.12, "hat": 0.065}[tipo]
        total = int(duracao * self.taxa)
        rng = random.Random({"kick": 7, "snare": 11, "hat": 19}[tipo])
        saida = array('h')
        fase = 0.0
        ultimo = 0.0
        for i in range(total):
            t = i / self.taxa
            env = max(0.0, 1.0 - t / duracao) ** 2
            if tipo == "kick":
                hz = 64 + 96 * math.exp(-42 * t)
                fase += (2 * math.pi * hz) / self.taxa
                sinal = math.sin(fase) * env
            elif tipo == "snare":
                ruido = rng.uniform(-1, 1)
                sinal = (0.76 * ruido + 0.24 * math.sin(2 * math.pi * 175 * t)) * env
            else:
                ruido = rng.uniform(-1, 1)
                # Diferença entre amostras atenua frequências graves do ruído.
                sinal = (ruido - ultimo) * 0.55 * env
                ultimo = ruido
            ataque = min(1.0, i / max(1, int(self.taxa * 0.001)))
            saida.append(int(max(-32767, min(32767, 11000 * sinal * ataque))))
        return pygame.mixer.Sound(buffer=self._pcm(saida))

    def _tocar_nota(self, canal: int, timbre: str, nota: str) -> None:
        if not self.disponivel:
            return
        chave = (timbre, nota)
        if chave not in self.cache:
            self.cache[chave] = self._criar_som_nota(nota, timbre)
        self.canais[canal].play(self.cache[chave])

    def _ajustar_volumes(self) -> None:
        if self.disponivel:
            fatores = (0.32, 0.27, 0.10, 0.23, 0.10)
            for canal, fator in zip(self.canais, fatores):
                canal.set_volume(self.volume * fator if self.ativado else 0.0)

    def alterar_volume(self, delta: float) -> None:
        if not self.disponivel:
            return
        self.volume = round(max(0.0, min(1.0, self.volume + delta)), 2)
        self._ajustar_volumes()

    def alternar(self) -> None:
        if not self.disponivel:
            return
        self.ativado = not self.ativado
        # A partitura segue em andamento enquanto está silenciada.
        self._ajustar_volumes()

    def iniciar(self) -> None:
        self.passo = 0
        self.acumulado = 0.0
        self.bpm = self.BPM_INICIAL
        self.rodando = True
        self.pausada = False
        for canal in self.canais:
            canal.stop()
        self._executar_passo()

    def pausar(self) -> None:
        self.pausada = True
        for canal in self.canais:
            canal.pause()

    def retomar(self) -> None:
        self.pausada = False
        for canal in self.canais:
            canal.unpause()

    def parar(self) -> None:
        self.rodando = False
        for canal in self.canais:
            canal.fadeout(250)

    def _executar_passo(self) -> None:
        if not self.disponivel:
            return
        passo = self.passo % len(self.partitura)
        indice_compasso, colcheia = divmod(passo, 8)
        nota = self.partitura[passo]
        raiz, quinta, acorde = self.HARMONIA[indice_compasso]
        if nota != '-':
            self._tocar_nota(0, 'lead', nota)
        if colcheia in (0, 2, 4, 6):
            self._tocar_nota(1, 'bass', raiz if colcheia in (0, 4) else quinta)
        if colcheia in (1, 3, 5, 7):
            self._tocar_nota(2, 'arp', acorde[((colcheia - 1) // 2) % len(acorde)])
        if colcheia in (0, 4):
            self.canais[3].play(self.cache[('kick', 'kick')])
        elif colcheia in (2, 6):
            self.canais[3].play(self.cache[('snare', 'snare')])
        self.canais[4].play(self.cache[('hat', 'hat')])
        self.passo = (self.passo + 1) % len(self.partitura)

    def atualizar(self, dt: float, nivel: int) -> None:
        if not self.rodando or self.pausada:
            return
        self.bpm = min(self.MAX_BPM, self.BPM_INICIAL + 5 * (nivel - 1))
        periodo = 30.0 / self.bpm  # duração da colcheia, em segundos.
        self.acumulado += dt
        # Recupera passos se houver pequena oscilação no FPS.
        while self.acumulado >= periodo:
            self.acumulado -= periodo
            self._executar_passo()


@dataclass
class Peca:
    tipo: str
    x: int = (COLUNAS - 4) // 2  # Peças surgem centralizadas na grade
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

    def __init__(self, on_event: Callable[[str], None] | None = None) -> None:
        self.on_event = on_event
        self.aleatorio = random.Random()
        self.saco: list[str] = []
        self.fila: list[str] = []
        self.novo_jogo(iniciar=False)

    def emitir(self, evento: str) -> None:
        """Notifica eventos; o estado do jogo não depende do dispositivo de áudio."""
        if self.on_event is not None:
            self.on_event(evento)

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
        if iniciar:
            self.emitir("iniciar")

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
                self.emitir("descer")
            elif dx:
                self.emitir("mover")
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
                self.emitir("girar")
                break

    def queda_rapida(self) -> None:
        if self.estado != "jogando":
            return
        distancia = 0
        while self.valido(dy=1):
            self.peca.y += 1
            distancia += 1
        self.pontos += 2 * distancia
        self.emitir("queda")
        self.fixar_peca(tocar_trava=False)

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
                self.emitir("fim")
        self.hold_disponivel = False
        self.tempo_queda = 0
        self.emitir("guardar")

    def criar_proxima_peca(self) -> None:
        self.peca = Peca(self.fila.pop(0))
        self.abastecer_fila()
        if not self.valido():
            self.estado = "fim"
            self.emitir("fim")

    def fixar_peca(self, *, tocar_trava: bool = True) -> None:
        for x, y in self.posicoes():
            if y < 0:
                self.estado = "fim"
                self.emitir("fim")
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
            self.emitir("tetris" if eliminadas == 4 else "linha")
        elif tocar_trava:
            self.emitir("fixar")

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
            self.emitir("pausa")
        elif self.estado == "pausado":
            self.estado = "jogando"
            self.tempo_queda = 0
            self.emitir("retomar")

    def iniciar_ou_retomar(self) -> None:
        if self.estado in ("pronto", "fim"):
            self.novo_jogo(iniciar=True)
        elif self.estado == "pausado":
            self.alternar_pausa()


# -----------------------------------------------------------------------------
# INTERFACE: GEOMETRIA FIXA, CONTROLES ALINHADOS E CORES CONSISTENTES
# -----------------------------------------------------------------------------
class Interface:
    def __init__(self) -> None:
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        pygame.init()
        pygame.display.set_caption("Tetris — Protótipo colorido | IHC e UX")

        monitor = pygame.display.Info()
        escala = min(1.0,
                     max(640, monitor.current_w - 90) / LARGURA,
                     max(480, monitor.current_h - 120) / ALTURA)
        tamanho = (round(LARGURA * escala), round(ALTURA * escala))
        self.janela = pygame.display.set_mode(tamanho, pygame.RESIZABLE)
        self.tela = pygame.Surface((LARGURA, ALTURA)).convert()
        self.relogio = pygame.time.Clock()

        self.titulo = pygame.font.SysFont("dejavusans", 28, bold=True)
        self.subtitulo = pygame.font.SysFont("dejavusans", 19, bold=True)
        self.valor = pygame.font.SysFont("dejavusans", 39, bold=True)
        self.normal = pygame.font.SysFont("dejavusans", 17)
        self.pequena = pygame.font.SysFont("dejavusans", 13)
        self.botao_fonte = pygame.font.SysFont("dejavusans", 19, bold=True)
        self.tecla_fonte = pygame.font.SysFont("dejavusans", 19, bold=True)
        self.sons = AudioRetro()
        self.musica = TrilhaChiptune(self.sons.disponivel)
        self.jogo = Tetris(on_event=self.evento_sonoro)
        self.botao_efeitos = pygame.Rect(LARGURA - 306, 12, 132, 30)
        self.botao_musica = pygame.Rect(LARGURA - 166, 12, 150, 30)

        # Dados e desenho usam os mesmos retângulos: nenhum controle é decorativo.
        self.botoes = {
            "iniciar": pygame.Rect(ESQUERDA_X, 270, ESQUERDA_LARGURA, 50),
            "pausar": pygame.Rect(ESQUERDA_X, 332, ESQUERDA_LARGURA, 50),
            "reiniciar": pygame.Rect(ESQUERDA_X, 394, ESQUERDA_LARGURA, 50),
        }
        # Controles em 4 linhas de mesma altura. Legendas ficam numa coluna
        # exclusiva, a partir de x=204: nunca cruzam os botões.
        self.teclas_interface = {
            "esquerda": pygame.Rect(56, 523, 52, 40),
            "direita": pygame.Rect(118, 523, 52, 40),
            "baixo": pygame.Rect(56, 568, 52, 40),
            "cima": pygame.Rect(56, 613, 52, 40),
            "espaco": pygame.Rect(56, 658, 128, 40),
        }
        self.caixa_hold = pygame.Rect(54, 119, 290, 118)
        self.proximo_movimento: dict[int, float] = {}
        self.layout_checado = self.verificar_layout()

    def verificar_layout(self) -> bool:
        """Evita regressões de sobreposição na lateral esquerda."""
        painel_controles = pygame.Rect(ESQUERDA_X, 461, ESQUERDA_LARGURA, 281)
        caixas = list(self.teclas_interface.values())
        assert all(painel_controles.contains(caixa) for caixa in caixas)
        assert all(not caixas[i].colliderect(caixas[j])
                   for i in range(len(caixas)) for j in range(i + 1, len(caixas)))
        assert all(caixa.right <= 184 for caixa in caixas)
        assert 204 + 142 <= ESQUERDA_X + ESQUERDA_LARGURA
        # O tabuleiro deve ser mais largo que cada painel lateral.
        assert CAMPO_LARGURA > max(ESQUERDA_LARGURA, DIREITA_LARGURA)
        assert ESQUERDA_X + ESQUERDA_LARGURA < CAMPO_X
        assert CAMPO_X + CAMPO_LARGURA < DIREITA_X
        assert DIREITA_X + DIREITA_LARGURA < LARGURA
        return True

    def viewport(self) -> tuple[float, int, int, int, int]:
        """Mantém a proporção do layout quando a janela é redimensionada."""
        largura, altura = self.janela.get_size()
        escala = min(largura / LARGURA, altura / ALTURA)
        w, h = round(LARGURA * escala), round(ALTURA * escala)
        return escala, (largura - w) // 2, (altura - h) // 2, w, h

    def coordenadas_logicas(self, posicao: tuple[int, int]) -> tuple[int, int] | None:
        escala, x0, y0, w, h = self.viewport()
        if not (x0 <= posicao[0] < x0 + w and y0 <= posicao[1] < y0 + h):
            return None  # Clique nas faixas de letterbox, fora do jogo.
        return (min(LARGURA - 1, int((posicao[0] - x0) / escala)),
                min(ALTURA - 1, int((posicao[1] - y0) / escala)))

    def escrever(self, texto: str, x: int, y: int, fonte: pygame.font.Font,
                 *, cor: tuple[int, int, int] = TEXTO,
                 centro: bool = False, meio_y: bool = False) -> None:
        superficie = fonte.render(texto, True, cor)
        destino = superficie.get_rect()
        if centro:
            destino.center = (x, y)
        elif meio_y:
            destino.midleft = (x, y)
        else:
            destino.topleft = (x, y)
        self.tela.blit(superficie, destino)

    def painel(self, area: pygame.Rect, *, cor: tuple[int, int, int] = PAINEL) -> None:
        pygame.draw.rect(self.tela, cor, area, border_radius=10)
        pygame.draw.rect(self.tela, BORDA, area, 1, border_radius=10)

    def desenhar_bloco(self, x: int, y: int, tamanho: int, tipo: str,
                       *, fantasma: bool = False) -> None:
        cor = CORES_PECAS[tipo]
        area = pygame.Rect(x, y, tamanho, tamanho).inflate(-3, -3)
        if fantasma:
            pygame.draw.rect(self.tela, escurecer(cor, 0.28), area, border_radius=3)
            pygame.draw.rect(self.tela, cor, area, 2, border_radius=3)
            return
        pygame.draw.rect(self.tela, cor, area, border_radius=3)
        brilho = pygame.Rect(area.left + 3, area.top + 3,
                             max(3, area.width - 6), 3)
        pygame.draw.rect(self.tela, clarear(cor, 32), brilho, border_radius=1)
        pygame.draw.rect(self.tela, escurecer(cor, 0.55), area, 1, border_radius=3)

    def miniatura(self, tipo: str | None, area: pygame.Rect, tamanho: int = 27) -> None:
        if tipo is None:
            self.escrever("Nenhuma peça guardada", area.centerx, area.centery,
                          self.normal, cor=TEXTO_SUAVE, centro=True)
            return
        coords = celulas_peca(tipo)
        xs, ys = [xy[0] for xy in coords], [xy[1] for xy in coords]
        largura = (max(xs) - min(xs) + 1) * tamanho
        altura = (max(ys) - min(ys) + 1) * tamanho
        x0 = area.centerx - largura // 2
        y0 = area.centery - altura // 2
        for x, y in coords:
            self.desenhar_bloco(x0 + (x - min(xs)) * tamanho,
                                y0 + (y - min(ys)) * tamanho, tamanho, tipo)

    def desenhar_botao(self, nome: str, area: pygame.Rect,
                       mouse: tuple[int, int] | None) -> None:
        jogando = self.jogo.estado == "jogando"
        ativo = ((nome == "iniciar" and not jogando) or
                 (nome == "pausar" and self.jogo.estado in ("jogando", "pausado")) or
                 nome == "reiniciar")
        rotulos = {
            "iniciar": "JOGANDO" if jogando else
                       "RETOMAR" if self.jogo.estado == "pausado" else "INICIAR",
            "pausar": "RETOMAR" if self.jogo.estado == "pausado" else "PAUSAR",
            "reiniciar": "REINICIAR",
        }
        cor = {
            "iniciar": VERDE,
            "pausar": AMARELO,
            "reiniciar": BOTAO_NEUTRO,
        }[nome]
        if not ativo:
            cor = BOTAO_INATIVO
        elif mouse is not None and area.collidepoint(mouse):
            cor = clarear(cor, 25)
        pygame.draw.rect(self.tela, cor, area, border_radius=9)
        # Contraste escuro sobre botões luminosos; claro sobre os demais.
        cor_texto = (9, 24, 36) if ativo and nome != "reiniciar" else TEXTO
        if not ativo:
            cor_texto = TEXTO_SUAVE
        self.escrever(rotulos[nome], area.centerx, area.centery,
                      self.botao_fonte, cor=cor_texto, centro=True)

    def desenhar_lateral_esquerda(self, mouse: tuple[int, int] | None) -> None:
        area_hold = pygame.Rect(ESQUERDA_X, 74, ESQUERDA_LARGURA, 182)
        self.painel(area_hold)
        self.escrever("HOLD", 55, 88, self.subtitulo)
        self.escrever("C / SHIFT", 270, 97, self.pequena, cor=TEXTO_SUAVE)
        pygame.draw.rect(self.tela, PAINEL_INTERNO,
                         self.caixa_hold, border_radius=8)
        borda = CIANO if (mouse is not None and
                           self.caixa_hold.collidepoint(mouse)) else BORDA
        pygame.draw.rect(self.tela, borda, self.caixa_hold, 1, border_radius=8)
        self.miniatura(self.jogo.hold, self.caixa_hold, tamanho=29)

        for nome, area in self.botoes.items():
            self.desenhar_botao(nome, area, mouse)

        controles = pygame.Rect(ESQUERDA_X, 461, ESQUERDA_LARGURA, 281)
        self.painel(controles)
        self.escrever("CONTROLES", 56, 476, self.subtitulo)
        self.escrever("TECLADO / MOUSE", 222, 482, self.pequena,
                      cor=TEXTO_SUAVE)

        simbolos = {"esquerda": "←", "direita": "→", "baixo": "↓",
                    "cima": "↑", "espaco": "ESPAÇO"}
        for nome, area in self.teclas_interface.items():
            hover = mouse is not None and area.collidepoint(mouse)
            fundo = (48, 83, 108) if hover else BOTAO_NEUTRO
            pygame.draw.rect(self.tela, fundo, area, border_radius=7)
            pygame.draw.rect(self.tela, CIANO if hover else BORDA,
                             area, 1, border_radius=7)
            fonte = self.pequena if nome == "espaco" else self.tecla_fonte
            self.escrever(simbolos[nome], area.centerx, area.centery,
                          fonte, centro=True)

        # Coluna de legendas totalmente separada da coluna de teclas.
        for rotulo, y in (("Mover", 543), ("Descer", 588),
                          ("Girar", 633), ("Queda rápida", 678)):
            self.escrever(rotulo, 204, y, self.normal, meio_y=True)

        self.escrever("C ou Shift = guardar peça", 56, 716,
                      self.pequena, cor=TEXTO_SUAVE)

    def cartao_estatistica(self, titulo: str, valor: int, y: int,
                           cor: tuple[int, int, int]) -> None:
        area = pygame.Rect(DIREITA_X, y, DIREITA_LARGURA, 132)
        self.painel(area)
        pygame.draw.rect(self.tela, cor,
                         pygame.Rect(area.x, area.y + 14, 5, area.height - 28),
                         border_radius=2)
        self.escrever(titulo, area.left + 24, area.top + 16,
                      self.subtitulo, cor=TEXTO_SUAVE)
        self.escrever(str(valor), area.left + 24, area.top + 50,
                      self.valor, cor=cor)

    def desenhar_lateral_direita(self) -> None:
        area = pygame.Rect(DIREITA_X, 74, DIREITA_LARGURA, 190)
        self.painel(area)
        self.escrever("PRÓXIMA PEÇA", area.left + 23,
                      area.top + 16, self.subtitulo)
        caixa = pygame.Rect(area.left + 22, area.top + 57,
                            area.width - 44, 110)
        pygame.draw.rect(self.tela, PAINEL_INTERNO, caixa, border_radius=8)
        pygame.draw.rect(self.tela, BORDA, caixa, 1, border_radius=8)
        self.miniatura(self.jogo.fila[0], caixa, tamanho=31)

        self.cartao_estatistica("PONTOS", self.jogo.pontos, 280, CIANO)
        self.cartao_estatistica("LINHAS", self.jogo.linhas_feitas, 426, VERDE)
        self.cartao_estatistica("NÍVEL", self.jogo.nivel, 572, AMARELO)
        self.escrever(f"7 FORMAS DE PEÇAS  •  GRADE {COLUNAS} × {LINHAS}",
                      DIREITA_X + 8, 729, self.pequena,
                      cor=TEXTO_SUAVE)

    def demo_tabuleiro(self) -> list[list[str | None]]:
        """Cenário inicial meramente ilustrativo; não entra na partida."""
        exemplo: list[list[str | None]] = [[None] * COLUNAS for _ in range(LINHAS)]
        desenho = {
            19: "JJLTT..LLSS..O",
            18: "JJ.TT.LLSS..OO",
            17: ".J.T..L.S....O",
            16: ".J.....S......",
            15: "........S.....",
        }
        for y, linha in desenho.items():
            for x, char in enumerate(linha):
                if char != ".":
                    exemplo[y][x] = char
        return exemplo

    def desenhar_tabuleiro(self) -> None:
        moldura = pygame.Rect(CAMPO_X - 4, CAMPO_Y - 4,
                              CAMPO_LARGURA + 8, CAMPO_ALTURA + 8)
        pygame.draw.rect(self.tela, BORDA, moldura, border_radius=5)
        area = pygame.Rect(CAMPO_X, CAMPO_Y, CAMPO_LARGURA, CAMPO_ALTURA)
        pygame.draw.rect(self.tela, PAINEL_INTERNO, area)

        tabuleiro_visivel = (self.demo_tabuleiro() if self.jogo.estado == "pronto"
                             else self.jogo.tabuleiro)
        for y in range(LINHAS):
            for x in range(COLUNAS):
                px, py = CAMPO_X + x * CELULA, CAMPO_Y + y * CELULA
                pygame.draw.rect(self.tela, GRADE, (px, py, CELULA, CELULA), 1)
                tipo = tabuleiro_visivel[y][x]
                if tipo:
                    self.desenhar_bloco(px, py, CELULA, tipo)

        if self.jogo.estado == "pronto":
            demonstracao = Peca("L", x=(COLUNAS - 4) // 2, y=3)
            for x, y in self.jogo.posicoes(demonstracao):
                self.desenhar_bloco(CAMPO_X + x * CELULA,
                                    CAMPO_Y + y * CELULA, CELULA, "L")
        elif self.jogo.estado != "fim":
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
                "pronto": ("PRONTO PARA JOGAR", "ENTER ou botão INICIAR"),
                "pausado": ("JOGO PAUSADO", "P para continuar"),
                "fim": ("FIM DE JOGO", "R para reiniciar"),
            }
            linha1, linha2 = mensagens[self.jogo.estado]
            cartao = pygame.Rect(CAMPO_X + 14, CAMPO_Y + 252,
                                 CAMPO_LARGURA - 28, 96)
            pygame.draw.rect(self.tela, PAINEL, cartao, border_radius=9)
            pygame.draw.rect(self.tela, CIANO if self.jogo.estado == "pronto"
                             else (VERMELHO if self.jogo.estado == "fim" else AMARELO),
                             cartao, 2, border_radius=9)
            self.escrever(linha1, cartao.centerx, cartao.top + 30,
                          self.pequena, cor=TEXTO, centro=True)
            self.escrever(linha2, cartao.centerx, cartao.top + 66,
                          self.pequena, cor=TEXTO_SUAVE, centro=True)

        self.escrever(f"TABULEIRO {COLUNAS} × {LINHAS}", CAMPO_X + CAMPO_LARGURA // 2,
                      CAMPO_Y + CAMPO_ALTURA + 28, self.pequena,
                      centro=True, cor=TEXTO_SUAVE)

    def evento_sonoro(self, evento: str) -> None:
        """Liga eventos do motor do jogo ao áudio, sem acoplá-los."""
        self.sons.tocar(evento)
        if evento == 'iniciar':
            self.musica.iniciar()
        elif evento == 'pausa':
            self.musica.pausar()
        elif evento == 'retomar':
            self.musica.retomar()
        elif evento == 'fim':
            self.musica.parar()

    def desenhar(self) -> None:
        self.tela.fill(FUNDO)
        pygame.draw.rect(self.tela, FUNDO_CABECALHO, (0, 0, LARGURA, 56))
        pygame.draw.line(self.tela, BORDA, (0, 55), (LARGURA, 55), 1)
        pygame.draw.rect(self.tela, CIANO, (34, 14, 5, 28), border_radius=2)
        self.escrever("TETRIS", 50, 12, self.titulo)
        self.escrever("PROTÓTIPO COLORIDO", 188, 22,
                      self.pequena, cor=CIANO)

        mouse = self.coordenadas_logicas(pygame.mouse.get_pos())
        # Dois controles independentes sem aumentar a altura do cabeçalho.
        for area, objeto, rotulo in (
            (self.botao_efeitos, self.sons, "EFEITOS"),
            (self.botao_musica, self.musica, "MÚSICA"),
        ):
            ativo = objeto.disponivel and objeto.ativado
            cor = BOTAO_NEUTRO if objeto.disponivel else BOTAO_INATIVO
            if mouse is not None and area.collidepoint(mouse) and objeto.disponivel:
                cor = clarear(cor, 16)
            pygame.draw.rect(self.tela, cor, area, border_radius=7)
            if not objeto.disponivel:
                legenda = "SEM ÁUDIO"
            else:
                percentual = (self.sons.volume_geral if rotulo == "EFEITOS"
                              else self.musica.volume)
                legenda = f"{rotulo} {round(percentual * 100)}%" if ativo else f"{rotulo} OFF"
            self.escrever(legenda, area.centerx, area.centery,
                          self.pequena, cor=CIANO if ativo else TEXTO_SUAVE, centro=True)
        self.desenhar_lateral_esquerda(mouse)
        self.desenhar_lateral_direita()
        self.desenhar_tabuleiro()

        escala, x0, y0, w, h = self.viewport()
        self.janela.fill(FUNDO)
        pygame.transform.smoothscale(self.tela, (w, h), self.janela.subsurface((x0, y0, w, h)))
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

    def clique(self, posicao: tuple[int, int] | None) -> None:
        if posicao is None:
            return
        if self.botao_efeitos.collidepoint(posicao):
            self.sons.alternar()
            return
        if self.botao_musica.collidepoint(posicao):
            self.musica.alternar()
            return
        if self.caixa_hold.collidepoint(posicao):
            self.jogo.guardar()
            return
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
        if key == pygame.K_m:
            self.sons.alternar()
        elif key == pygame.K_n:
            self.musica.alternar()
        elif key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
            self.musica.alterar_volume(0.05)
        elif key in (pygame.K_MINUS, pygame.K_KP_MINUS):
            self.musica.alterar_volume(-0.05)
        elif key == pygame.K_LEFTBRACKET:
            self.sons.mudar_volume(-0.1)
        elif key == pygame.K_RIGHTBRACKET:
            self.sons.mudar_volume(0.1)
        elif key == pygame.K_RETURN:
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
                    self.proximo_movimento[key] = agora + (
                        0.050 if key == pygame.K_DOWN else 0.085)

    def executar(self) -> None:
        while True:
            dt = min(self.relogio.tick(FPS) / 1000, 0.10)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.VIDEORESIZE:
                    self.janela = pygame.display.set_mode(
                        (max(640, evento.w), max(480, evento.h)), pygame.RESIZABLE)
                elif evento.type == pygame.KEYDOWN:
                    self.tecla(evento.key)
                elif evento.type == pygame.KEYUP:
                    self.proximo_movimento.pop(evento.key, None)
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    self.clique(self.coordenadas_logicas(evento.pos))
                elif evento.type == pygame.MOUSEWHEEL:
                    mouse = self.coordenadas_logicas(pygame.mouse.get_pos())
                    if mouse is not None:
                        if self.botao_musica.collidepoint(mouse):
                            self.musica.alterar_volume(evento.y * 0.05)
                        elif self.botao_efeitos.collidepoint(mouse):
                            self.sons.mudar_volume(evento.y * 0.1)
            self.repetir_movimento()
            self.jogo.atualizar(dt)
            self.musica.atualizar(dt, self.jogo.nivel)
            self.desenhar()


def main() -> None:
    try:
        Interface().executar()
    except pygame.error as erro:
        print(f"Não foi possível abrir a janela do Pygame: {erro}", file=sys.stderr)
        raise SystemExit(1) from erro


if __name__ == "__main__":
    main()
