#!/usr/bin/env python3
"""
Incidente 074 — Investigação em IHC
=====================================
12 telas encadeadas, progresso salvo em JSON por equipe.
O caso: um guarda-chuva azul foi registrado no prédio errado.
A dupla investiga como aconteceu e propõe melhorias.

Uso:
    python incidente_074.py          → abrir (novo ou continuar)
    python incidente_074.py --novo   → forçar nova investigação
    python incidente_074.py --teste  → smoke test automático
"""

import sys, json, os, textwrap
from pathlib import Path
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
#  CONSTANTES E DADOS DO CASO
# ═══════════════════════════════════════════════════════════════

VERSAO = "1.0"
DIR_SAVES = Path("saves_074")
W = 72   # largura do terminal

CODIGOS = {
    "predios":    {"Prédio A": "28", "Prédio B": "74", "Prédio C": "63"},
    "categorias": {"Acessório": "K",  "Documento": "D",  "Eletrônico": "Y"},
    "locais":     {"Armário 1": "12", "Armário 2": "16", "Armário 3": "19"},
}

PISTAS = {
    "E01": "Destino solicitado: 74 / K / 19.",
    "E02": "A interface inicia com Prédio A selecionado e destaca a ação de concluir.",
    "E03": "Preservar os dados e indicar o ponto de retomada são apoios diferentes.",
    "E04": "O destino foi registrado como Prédio A; categoria, armário e descrição correspondem à solicitação.",
    "E05": "Corrigir um campo não deve eliminar informações válidas sem necessidade.",
    "E06": "A ação 'Concluir' não apresentava uma etapa de revisão do destino.",
    "E07": "A investigação também precisa considerar frequência de uso, alcance e organização do posto.",
    "E08": "B atende aos critérios definidos neste teste; isso não comprova superioridade em qualquer contexto.",
    "E09": "O registro terminou com o prédio inicial; os eventos ajudam a reconstruir ações, mas não demonstram sozinhos a causa cognitiva.",
}

DICAS = {
    1:  ["Fato: algo verificável diretamente no relato.",
         "Hipótese: uma explicação ainda não demonstrada.",
         "As perguntas de investigação guiam todo o restante."],
    2:  ["Prédio B tem código próximo de 70.",
         "Categoria Acessório: pense na inicial em inglês.",
         "Organize a tabela no caderno antes de preencher."],
    3:  ["O campo de prédio é essencial para conferir o destino.",
         "O botão verde grande e o aviso de campanha são os competidores.",
         "Visível ≠ em destaque."],
    4:  ["Ao retornar, note quais campos ainda estão preenchidos.",
         "O balcão correto está no aviso mostrado.",
         "O ponto de retomada é o próximo campo vazio."],
    5:  ["Consulte a pista E01 para o destino esperado.",
         "O código 28 não é Prédio B.",
         "Apenas um campo diverge."],
    6:  ["Uma boa correção altera só o campo errado.",
         "Os outros campos (K, 19, guarda-chuva azul) eram válidos.",
         "Observe quais campos ficam em branco na simulação."],
    7:  ["Teste cada comando com o formulário preenchido.",
         "Voltar deveria perguntar antes de descartar.",
         "Concluir deveria exibir um resumo do destino."],
    8:  ["Itens muito usados devem estar próximos.",
         "Teclado, telefone e bandeja são os mais frequentes.",
         "O arquivo pode ficar em posição secundária."],
    9:  ["Os dois critérios: tempo ≤ 50s e incorretos ≤ 1.",
         "Versão A falha no critério de incorretos.",
         "1 ÷ 20 × 100 = 5%."],
    10: ["O histórico mostra ações, não intenções.",
         "Siga a ordem dos horários para ordenar os eventos.",
         "O histórico não revela se Lia conferiu conscientemente o destino."],
    11: ["Cada relação: evidência → problema → melhoria → verificação.",
         "Recupere a resposta quantitativa da tela 9.",
         "Registre algo que a investigação não conseguiu responder."],
    12: ["Prédio C = 63, Documento = D, Armário 2 = 16.",
         "Ative a revisão de destino antes de iniciar.",
         "Ao retomar, verifique se os campos foram preservados."],
}

NOMES_TELAS = {
    1: "O Incidente 074",       2: "O Manual de Códigos",
    3: "O que chama atenção?",  4: "O telefone tocou",
    5: "O registro suspeito",   6: "Corrigir sem recomeçar",
    7: "O que significa concluir?", 8: "Além da tela",
    9: "Mais rápido significa melhor?", 10: "Reconstruindo os acontecimentos",
    11: "O relatório da equipe", 12: "A recepção reabriu",
}

# ═══════════════════════════════════════════════════════════════
#  UTILITÁRIOS DE UI
# ═══════════════════════════════════════════════════════════════

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def ln(c="─"): print(c * W)

def p(texto, ind=2):
    for linha in textwrap.wrap(texto, W - ind):
        print(" " * ind + linha)

def titulo(t):
    ln("═"); print(f"  {t}"); ln("═")

def cabecalho(n, est):
    cls()
    concl = len(est["etapas_concluidas"])
    npist = len(est["pistas"])
    eq    = est["equipe"] or "—"
    print(f"  ▸ INCIDENTE 074  ·  Tela {n}/12 — {NOMES_TELAS[n]}")
    print(f"  Equipe: {eq}  ·  {concl}/12 etapas  ·  {npist} pistas coletadas")
    ln(); print()

def pausa(modo_teste):
    if not modo_teste:
        input("\n  [ ENTER para continuar ] ")
    print()

def inp(prompt, validos=None, modo_teste=False, auto=None):
    """Lê entrada. Retorna (valor, cmd_global|None).
    cmd_global in ('A','P','D','S') dispara ação global."""
    enquanto = True
    while enquanto:
        try:
            if modo_teste and auto is not None:
                r = str(auto)
                print(f"  {prompt}: [TESTE→{r}]")
                return r, None
            r = input(f"  {prompt}: ").strip()
        except (EOFError, KeyboardInterrupt):
            return "S", "S"

        upper = r.upper()
        if upper in ("A", "P", "D", "S"):
            return upper, upper

        if validos is None:
            return r, None
        if r.upper() in [v.upper() for v in validos]:
            return r.upper() if len(r) == 1 else r, None
        print(f"  ⚠  Escolha uma opção válida: {', '.join(validos)}")

def global_cmd(cmd, est, n, caminho):
    """Executa comando global. Retorna False (continuar)."""
    if cmd == "A":
        mostrar_arquivo(est)
    elif cmd == "P":
        mostrar_pistas(est)
    elif cmd == "D":
        mostrar_dica(est, n)
    elif cmd == "S":
        salvar(est, caminho)
        print("\n  ✓ Progresso salvo. Até logo!\n")
        sys.exit(0)

def mostrar_arquivo(est):
    cls(); titulo("ARQUIVO DO CASO — Incidente 074"); print()
    p("Objeto: guarda-chuva azul")
    p("Destino solicitado: Prédio B / Acessório / Armário 3")
    p("Destino registrado: Prédio A / Acessório / Armário 3")
    p("Data fictícia: 14h02–14h06"); print()
    t2 = est["respostas"].get("t02", {})
    if t2:
        p(f"Sua conversão (T2): {t2.get('predio','?')} / {t2.get('cat','?')} / {t2.get('local','?')} / {t2.get('desc','?')}")
    ln(); input("\n  [ ENTER ] ")

def mostrar_pistas(est):
    cls(); titulo("PISTAS COLETADAS"); print()
    if not est["pistas"]:
        p("Nenhuma pista coletada ainda.")
    else:
        for pid in sorted(est["pistas"]):
            print(f"\n  [{pid}] {est['pistas'][pid]}")
    print(); input("  [ ENTER ] ")

def mostrar_dica(est, n):
    cls(); titulo(f"DICA — Tela {n}"); print()
    dicas  = DICAS.get(n, ["Releia o enunciado com atenção."])
    usado  = est["dicas_usadas"].get(str(n), 0)
    if usado < len(dicas):
        p(f"💡 {dicas[usado]}")
        est["dicas_usadas"][str(n)] = usado + 1
    else:
        p("Todas as dicas desta tela foram reveladas.")
        for d in dicas: p(f"• {d}")
    print(); input("  [ ENTER ] ")

# ═══════════════════════════════════════════════════════════════
#  PERSISTÊNCIA
# ═══════════════════════════════════════════════════════════════

def novo_estado():
    return {
        "versao": VERSAO,
        "equipe": "",
        "tela_atual": 1,
        "etapas_concluidas": [],
        "pistas": {},
        "hipoteses_iniciais": [],
        "hipoteses_revisadas": [],
        "respostas": {},
        "dicas_usadas": {},
        "tentativas": {},
        "horario_inicio": datetime.now().isoformat(),
        "relatorio": {},
    }

def carregar(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)

def salvar(est, caminho):
    DIR_SAVES.mkdir(exist_ok=True)
    tmp = Path(str(caminho) + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(est, f, ensure_ascii=False, indent=2)
    tmp.replace(caminho)

def concluir(est, n, caminho):
    if n not in est["etapas_concluidas"]:
        est["etapas_concluidas"].append(n)
    if est["tela_atual"] == n:
        est["tela_atual"] = n + 1
    salvar(est, caminho)

def add_pista(est, pid, caminho):
    est["pistas"][pid] = PISTAS[pid]
    salvar(est, caminho)

def add_tentativa(est, chave, caminho):
    est["tentativas"][chave] = est["tentativas"].get(chave, 0) + 1
    salvar(est, caminho)

def set_resp(est, chave, dados, caminho):
    est["respostas"][chave] = dados
    salvar(est, caminho)

def get_resp(est, chave):
    return est["respostas"].get(chave, {})

# ═══════════════════════════════════════════════════════════════
#  TELAS
# ═══════════════════════════════════════════════════════════════

def t01(est, caminho, modo_teste):
    """T01 — O Incidente 074"""
    while True:
        cabecalho(1, est)
        p("São 14h06. O supervisor encontra uma inconsistência:")
        p("Um guarda-chuva azul foi registrado no Prédio A, mas a ficha de")
        p("recebimento indicava o Prédio B, Armário 3.")
        print()
        p('"Lia provavelmente não prestou atenção." — supervisor')
        p("Ainda não há evidências suficientes para explicar a causa.")
        print(); ln()

        # ── Equipe ──────────────────────────────────────────────
        if not est["equipe"]:
            print("\n  IDENTIFICAÇÃO DA EQUIPE\n")
            r, cmd = inp("Nome da equipe (ex: Dupla-01)", modo_teste=modo_teste, auto="Dupla-01")
            if cmd: global_cmd(cmd, est, 1, caminho); continue
            est["equipe"] = r.strip() or "Equipe"
            salvar(est, caminho)
        else:
            print(f"\n  Equipe: {est['equipe']}\n")

        # ── Classificação ───────────────────────────────────────
        ln(); print("\n  CLASSIFICAR AFIRMAÇÕES\n")
        p("Classifique cada afirmação:")
        print("    [1] Fato informado no caso")
        print("    [2] Hipótese ainda não demonstrada")
        print("    [3] Hipótese a investigar")
        print()

        afirm = [
            ("A01", "O prédio registrado difere daquele indicado na ficha.",  "1"),
            ("A02", "Lia não prestou atenção.",                                "2"),
            ("A03", "A interface pode ter contribuído para o erro.",           "3"),
        ]
        labels = {
            "1": "Fato informado no caso",
            "2": "Hipótese ainda não demonstrada",
            "3": "Hipótese a investigar",
        }

        resps_c = get_resp(est, "t01_class").copy()
        corretas = 0
        reiniciar = False

        for cod, texto, gab in afirm:
            p(f"[{cod}] {texto}")
            atual = resps_c.get(cod, "")
            if atual == gab:
                print(f"       ✓ {labels[gab]}\n")
                corretas += 1
                continue

            r, cmd = inp("Resposta (1/2/3)", validos=["1","2","3"],
                         modo_teste=modo_teste, auto=gab)
            if cmd: global_cmd(cmd, est, 1, caminho); reiniciar = True; break

            resps_c[cod] = r
            set_resp(est, "t01_class", resps_c, caminho)

            if r == gab:
                print(f"  ✅ {labels[gab]}\n")
                corretas += 1
            else:
                add_tentativa(est, "t01_class", caminho)
                print(f"  ❌ Revise. Dica: [D]\n")

        if reiniciar: continue

        if corretas < 3:
            p("Revise as classificações e tente novamente.")
            pausa(modo_teste); continue

        # ── Perguntas de investigação ────────────────────────────
        ln(); print("\n  PERGUNTAS DE INVESTIGAÇÃO\n")
        p("Escreva duas perguntas para guiar a investigação.")
        p("Exemplo: 'Qual prédio estava selecionado inicialmente?'")
        p("→ Caderno: escreva e desenvolva antes de preencher aqui.")
        print()

        pergs = list(est.get("hipoteses_iniciais", []))
        n_perg = 1
        while len(pergs) < 2:
            autos = ["Qual prédio estava selecionado inicialmente?",
                     "O que aconteceu durante o atendimento de Lia?"]
            r, cmd = inp(f"Pergunta {n_perg}",
                         modo_teste=modo_teste, auto=autos[n_perg - 1])
            if cmd: global_cmd(cmd, est, 1, caminho); continue
            if len(r.strip()) < 10:
                p("⚠ Escreva uma pergunta mais completa (mínimo 10 caracteres)."); continue
            pergs.append(r.strip())
            n_perg += 1
            est["hipoteses_iniciais"] = pergs
            salvar(est, caminho)

        print()
        p("✅ Identificação, classificações e perguntas registradas.")
        p("→ Controles fixos disponíveis em qualquer tela:")
        p("  [A] Arquivo do caso · [P] Pistas · [D] Dica · [S] Salvar e sair")
        pausa(modo_teste)
        concluir(est, 1, caminho)
        return True


def t02(est, caminho, modo_teste):
    """T02 — O Manual de Códigos"""
    cabecalho(2, est)

    print("  MANUAL DO SISTEMA\n")
    print("  ┌─────────────┬──────┐  ┌──────────────┬──────┐  ┌────────────┬──────┐")
    print("  │ Prédio      │ Cód  │  │ Categoria    │ Cód  │  │ Local      │ Cód  │")
    print("  ├─────────────┼──────┤  ├──────────────┼──────┤  ├────────────┼──────┤")
    print("  │ Prédio A    │  28  │  │ Acessório    │  K   │  │ Armário 1  │  12  │")
    print("  │ Prédio B    │  74  │  │ Documento    │  D   │  │ Armário 2  │  16  │")
    print("  │ Prédio C    │  63  │  │ Eletrônico   │  Y   │  │ Armário 3  │  19  │")
    print("  └─────────────┴──────┘  └──────────────┴──────┘  └────────────┴──────┘")
    print()
    p("FICHA DO INCIDENTE:")
    print("    Prédio B  ·  Acessório  ·  Armário 3  ·  guarda-chuva azul")
    print()
    p("→ Caderno: copie as tabelas e converta a ficha antes de preencher.")
    print(); ln(); print("\n  CONVERTER FICHA PARA CÓDIGOS DO SISTEMA\n")

    gab = {"predio": "74", "cat": "K", "local": "19", "desc": "guarda-chuva azul"}
    campos = [
        ("predio", "Código do Prédio B", "prédio"),
        ("cat",    "Código de Acessório", "categoria"),
        ("local",  "Código do Armário 3", "local"),
        ("desc",   "Descrição do objeto", "descrição"),
    ]

    resps = get_resp(est, "t02").copy()

    for chave, rotulo, cat_nome in campos:
        if resps.get(chave, "").lower() == gab[chave].lower():
            print(f"  {rotulo}: {resps[chave]} ✓")
            continue
        while True:
            r, cmd = inp(rotulo, modo_teste=modo_teste, auto=gab[chave])
            if cmd: global_cmd(cmd, est, 2, caminho); continue
            if chave == "desc":
                ok = "guarda" in r.lower() or "azul" in r.lower()
            else:
                ok = r.strip() == gab[chave]

            if ok:
                resps[chave] = r.strip()
                set_resp(est, "t02", resps, caminho)
                print(f"  ✅ {rotulo}: {r}")
                break
            else:
                add_tentativa(est, "t02", caminho)
                print(f"  ❌ Revise a tabela de {cat_nome}.")

    print()
    add_pista(est, "E01", caminho)
    p(f"🔍 Pista E01 coletada: {PISTAS['E01']}")
    p("→ Caderno: registre E01 e verifique sua legenda de códigos.")
    pausa(modo_teste)
    concluir(est, 2, caminho)
    return True


def t03(est, caminho, modo_teste):
    """T03 — O que chama atenção?"""
    cabecalho(3, est)
    p("Reprodução da interface antiga (apenas para inspeção):")
    print()
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║  SISTEMA DE ACHADOS E PERDIDOS                       ║")
    print("  ╠══════════════════════════════════════════════════════╣")
    print("  ║  [E1] Prédio:    [ Prédio A ▾ ]  ← já selecionado  ║")
    print("  ║  [E2] Categoria: [             ]                     ║")
    print("  ║  [E3] Armário:   [             ]                     ║")
    print("  ║  [E4] Descrição: guarda-chuva azul   (centro)        ║")
    print("  ║                                                       ║")
    print("  ║  [E5] ⚠ CAMPANHA: Sorteio na sexta-feira! ⚠         ║")
    print("  ║                                                       ║")
    print("  ║       ┌──────────────────────────┐                   ║")
    print("  ║       │  ✅  CONCLUIR  [E6]      │ ← botão verde    ║")
    print("  ║       └──────────────────────────┘                   ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print()
    p("Elementos: [E1] Campo Prédio · [E2] Categoria · [E3] Armário · [E4] Descrição · [E5] Aviso campanha · [E6] Botão CONCLUIR")
    print(); ln(); print("\n  INSPEÇÃO\n")

    while True:
        p("1) Elemento ESSENCIAL para conferir o destino correto:")
        r1, cmd = inp("Código (E1–E6)", modo_teste=modo_teste, auto="E1")
        if cmd: global_cmd(cmd, est, 3, caminho); continue
        r1 = r1.upper()
        if r1 == "E1":
            print("  ✅ Campo Prédio — essencial para verificar o destino.\n")
        else:
            add_tentativa(est, "t03_1", caminho)
            print("  ℹ️  E1 (campo Prédio) é o essencial — é o valor divergente.\n")
            r1 = "E1"
        break

    while True:
        p("2) Elemento que COMPETE pela atenção com o campo Prédio:")
        r2, cmd = inp("Código (E1–E6)", modo_teste=modo_teste, auto="E6")
        if cmd: global_cmd(cmd, est, 3, caminho); continue
        r2 = r2.upper()
        if r2 in ("E5", "E6"):
            print(f"  ✅ {r2} compete pela atenção.\n")
        else:
            add_tentativa(est, "t03_2", caminho)
            print("  ℹ️  E6 (botão verde grande) e E5 (aviso) são os principais competidores.\n")
            r2 = "E6"
        break

    p("3) Consequência de E1 (campo Prédio com pouco destaque):")
    print("    [1] Pode passar despercebido")
    print("    [2] Compete pela atenção")
    print("    [3] Ajuda a conferir o destino")
    r3, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="1")
    if cmd: global_cmd(cmd, est, 3, caminho)

    p("\n4) Consequência do competidor que você identificou:")
    print("    [1] Pode passar despercebido")
    print("    [2] Compete pela atenção")
    print("    [3] Ajuda a conferir o destino")
    r4, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="2")
    if cmd: global_cmd(cmd, est, 3, caminho)

    set_resp(est, "t03", {"essencial": r1, "competidor": r2, "c_essencial": r3, "c_comp": r4}, caminho)

    print()
    add_pista(est, "E02", caminho)
    p(f"🔍 Pista E02 coletada: {PISTAS['E02']}")
    p("→ Caderno: 'O que estava visível?' e 'O que estava em destaque?' não têm a mesma resposta.")
    pausa(modo_teste)
    concluir(est, 3, caminho)
    return True


def t04(est, caminho, modo_teste):
    """T04 — O telefone tocou"""
    cabecalho(4, est)
    p("Formulário de TREINAMENTO — dados fictícios, separado do incidente.")
    p("Tarefa: Prédio C · Eletrônico · Armário 2 · carregador branco")
    print(); ln()

    print("\n  ETAPA 1 — Preencher os dois primeiros campos\n")
    r_pred, cmd = inp("Código do Prédio C", modo_teste=modo_teste, auto="63")
    if cmd: global_cmd(cmd, est, 4, caminho)
    r_cat, cmd  = inp("Código de Eletrônico", modo_teste=modo_teste, auto="Y")
    if cmd: global_cmd(cmd, est, 4, caminho)

    ok_pred = r_pred.strip() == "63"
    ok_cat  = r_cat.strip().upper() == "Y"
    print(f"  {'✅' if ok_pred else 'ℹ️ '} Prédio: {r_pred} {'✓' if ok_pred else '(esperado: 63)'}")
    print(f"  {'✅' if ok_cat  else 'ℹ️ '} Categoria: {r_cat} {'✓' if ok_cat else '(esperado: Y)'}")

    print()
    ln(); print("\n  🔔  O TELEFONE TOCOU\n")
    p("Uma pessoa pergunta onde retirar documentos perdidos.")
    p("Aviso na recepção: Balcão 2 atende documentos · Balcão 3 atende eletrônicos")
    print()
    r_tel, cmd = inp("Qual balcão você indicou?", modo_teste=modo_teste, auto="Balcão 2")
    if cmd: global_cmd(cmd, est, 4, caminho)

    ok_tel = "2" in r_tel
    if ok_tel:
        print("  ✅ Correto — Balcão 2.")
    else:
        add_tentativa(est, "t04_tel", caminho)
        print("  ℹ️  O aviso indicava Balcão 2 para documentos.")

    print(); ln(); print("\n  ETAPA 2 — Retorno ao formulário\n")
    p("Quais campos estavam preenchidos ao retornar?")
    print("    [1] Nenhum — a tela estava em branco")
    print("    [2] Prédio e Categoria (preservados)")
    print("    [3] Todos os campos")
    r_camp, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="2")
    if cmd: global_cmd(cmd, est, 4, caminho)
    if r_camp == "2":
        print("  ✅ Prédio e Categoria foram preservados.")
    else:
        add_tentativa(est, "t04_camp", caminho)
        print("  ℹ️  Na interface original, campos preenchidos persistem durante a sessão.")

    p("\nQual era a PRÓXIMA AÇÃO ao retornar?")
    print("    [1] Redigitar todos os campos")
    print("    [2] Preencher Armário (próximo campo vazio)")
    print("    [3] Clicar em Concluir diretamente")
    r_prox, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="2")
    if cmd: global_cmd(cmd, est, 4, caminho)
    if r_prox == "2":
        print("  ✅ A próxima ação era preencher Armário.")
    else:
        add_tentativa(est, "t04_prox", caminho)
        print("  ℹ️  O próximo campo era Armário.")

    print(); p("Complete o registro de treinamento:")
    r_loc, cmd  = inp("Código do Armário 2", modo_teste=modo_teste, auto="16")
    if cmd: global_cmd(cmd, est, 4, caminho)
    r_desc, cmd = inp("Descrição", modo_teste=modo_teste, auto="carregador branco")
    if cmd: global_cmd(cmd, est, 4, caminho)

    set_resp(est, "t04", {
        "tel": r_tel, "campos": r_camp, "prox": r_prox,
        "completo": f"63 / Y / {r_loc.strip()} / {r_desc.strip()}"
    }, caminho)

    print()
    add_pista(est, "E03", caminho)
    p(f"🔍 Pista E03: {PISTAS['E03']}")
    p("→ Caderno: o que ajudou ou dificultou saber onde continuar?")
    pausa(modo_teste)
    concluir(est, 4, caminho)
    return True


def t05(est, caminho, modo_teste):
    """T05 — O registro suspeito"""
    cabecalho(5, est)
    p("Registro encontrado no sistema após o incidente:")
    print()
    print("  ┌────────────┬──────────────────────────┐")
    print("  │ Campo      │ Valor registrado          │")
    print("  ├────────────┼──────────────────────────┤")
    print("  │ Prédio     │  28                       │")
    print("  │ Categoria  │  K                        │")
    print("  │ Armário    │  19                       │")
    print("  │ Descrição  │  guarda-chuva azul        │")
    print("  └────────────┴──────────────────────────┘")
    print()
    p("Compare com a pista E01 (74 / K / 19). Consulte suas anotações.")
    p("→ Caderno: traduza os códigos e marque a divergência antes de responder.")
    print(); ln(); print("\n  ANÁLISE\n")

    while True:
        p("1) O código 28 corresponde a qual prédio?")
        r1, cmd = inp("Resposta", modo_teste=modo_teste, auto="Prédio A")
        if cmd: global_cmd(cmd, est, 5, caminho); continue
        if "a" in r1.lower() or "28" in r1:
            print("  ✅ 28 = Prédio A")
        else:
            add_tentativa(est, "t05_1", caminho)
            print("  ℹ️  28 = Prédio A (consulte a tabela da tela 2)")
        break

    p("\n2) Qual campo diverge do destino solicitado (E01)?")
    print("    [1] Prédio  [2] Categoria  [3] Armário  [4] Descrição")
    r2, cmd = inp("Escolha (1/2/3/4)", validos=["1","2","3","4"], modo_teste=modo_teste, auto="1")
    if cmd: global_cmd(cmd, est, 5, caminho)
    if r2 == "1":
        print("  ✅ Prédio é o único campo divergente.")
    else:
        add_tentativa(est, "t05_2", caminho)
        print("  ℹ️  Apenas Prédio difere: 28 (A) vs. 74 (B).")
        r2 = "1"

    p("\n3) Valor registrado (código / nome):")
    r3, cmd = inp("Código registrado", modo_teste=modo_teste, auto="28")
    if cmd: global_cmd(cmd, est, 5, caminho)

    p("\n4) Valor esperado (código / nome):")
    r4, cmd = inp("Código esperado", modo_teste=modo_teste, auto="74")
    if cmd: global_cmd(cmd, est, 5, caminho)

    set_resp(est, "t05", {"trad_28": r1, "campo": r2, "registrado": r3, "esperado": r4}, caminho)

    print()
    add_pista(est, "E04", caminho)
    p(f"🔍 Pista E04: {PISTAS['E04']}")
    pausa(modo_teste)
    concluir(est, 5, caminho)
    return True


def t06(est, caminho, modo_teste):
    """T06 — Corrigir sem recomeçar"""
    cabecalho(6, est)
    p("Cópia de treinamento — registro incorreto para simulação:")
    print()
    print("  Estado inicial: 28 / K / 19 / guarda-chuva azul")
    print()
    p("▶ Simulando 'Aplicar correção' (alterar apenas Prédio de 28 para 74)...")
    print()
    print("  Antes:  28  /  K   /  19  /  guarda-chuva azul")
    print("  Após:   74  /  __ /  __ /  __________________")
    print()
    p("⚠ A simulação apagou Categoria, Armário e Descrição ao corrigir o Prédio.")
    p("→ Caderno: 'Qual trabalho o sistema obrigou a repetir?' e 'O que deveria ser preservado?'")
    print(); ln(); print("\n  ANÁLISE\n")

    p("1) Quais campos foram apagados? (indique todos)")
    print("    [A] Categoria   [B] Armário   [C] Descrição   [D] Prédio (o corrigido)")
    r1, cmd = inp("Resposta (ex: ABC)", modo_teste=modo_teste, auto="ABC")
    if cmd: global_cmd(cmd, est, 6, caminho)
    ok1 = all(c in r1.upper() for c in "ABC") and "D" not in r1.upper()
    if ok1:
        print("  ✅ Categoria, Armário e Descrição foram apagados incorretamente.")
    else:
        add_tentativa(est, "t06_1", caminho)
        print("  ℹ️  Os campos apagados foram: Categoria (K), Armário (19) e Descrição.")

    p("\n2) Regra de correção ideal:")
    print("    [1] Alterar apenas o campo errado, preservar os demais")
    print("    [2] Apagar tudo e pedir preenchimento completo novamente")
    print("    [3] Criar registro novo e arquivar o incorreto")
    r2, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="1")
    if cmd: global_cmd(cmd, est, 6, caminho)
    if r2 == "1":
        print("  ✅ Preservar campos válidos é a abordagem correta.")
    else:
        add_tentativa(est, "t06_2", caminho)
        print("  ℹ️  Alterar apenas o campo errado e preservar os demais é a melhor regra.")
        r2 = "1"

    print()
    p("Simulando nova correção com sua regra:")
    print("  Antes:  28  /  K  /  19  /  guarda-chuva azul")
    print("  Após:   74  /  K  /  19  /  guarda-chuva azul  ✓")
    print()

    set_resp(est, "t06", {"campos": r1, "regra": r2}, caminho)
    add_pista(est, "E05", caminho)
    p(f"🔍 Pista E05: {PISTAS['E05']}")
    pausa(modo_teste)
    concluir(est, 6, caminho)
    return True


def t07(est, caminho, modo_teste):
    """T07 — O que significa concluir?"""
    cabecalho(7, est)
    p("Formulário preenchido no ambiente de teste:")
    print("  Prédio: 28  |  Categoria: K  |  Armário: 19  |  Descrição: guarda-chuva azul")
    print()
    p("Três comandos para testar:")
    print("  [V] Voltar   → abandona o formulário sem aviso")
    print("  [C] Cancelar → limpa os campos imediatamente")
    print("  [O] Concluir → verifica obrigatórios e encerra, SEM revisar o destino")
    print()
    p("→ Caderno: escreva o que espera de cada comando ANTES de testá-los.")
    print(); ln(); print("\n  EXPECTATIVAS\n")

    pergs_exp = [
        ("Voltar", ["1","2","3"],
         "1=Pergunta antes · 2=Volta sem aviso · 3=Mantém rascunho"),
        ("Cancelar", ["1","2","3"],
         "1=Pede confirmação · 2=Limpa imediatamente · 3=Salva rascunho"),
        ("Concluir", ["1","2","3"],
         "1=Finaliza sem revisão · 2=Mostra resumo · 3=Pede aprovação"),
    ]
    exp = []
    for nome, vals, hint in pergs_exp:
        print(f"  O que você espera de {nome}?  ({hint})")
        r, cmd = inp("Escolha (1/2/3)", validos=vals, modo_teste=modo_teste, auto="2")
        if cmd: global_cmd(cmd, est, 7, caminho)
        exp.append(r); print()

    p("Resultado dos testes na simulação:")
    print("  VOLTAR   → formulário descartado sem aviso   (atual)")
    print("  CANCELAR → campos limpos imediatamente       (atual)")
    print("  CONCLUIR → encerrado sem revisão do destino  (atual ← ponto crítico)")
    print(); ln(); print("\n  PROPOSTA DE COMPORTAMENTO\n")
    p("Associe a operação ideal a cada comando:")
    print("    [1] Voltar preservando rascunho")
    print("    [2] Descartar com confirmação")
    print("    [3] Revisar destino antes de finalizar")
    print()

    props = []
    gabs_prop = {"Voltar": "2", "Cancelar": "2", "Concluir": "3"}
    for nome, gab in gabs_prop.items():
        r, cmd = inp(f"Operação ideal para {nome} (1/2/3)",
                     validos=["1","2","3"], modo_teste=modo_teste, auto=gab)
        if cmd: global_cmd(cmd, est, 7, caminho)
        if nome == "Concluir" and r != "3":
            add_tentativa(est, "t07", caminho)
            print("  ℹ️  Concluir com revisão do destino é a melhoria central.")
            r = "3"
        props.append(r)

    set_resp(est, "t07", {"exp": exp, "props": props}, caminho)
    print()
    add_pista(est, "E06", caminho)
    p(f"🔍 Pista E06: {PISTAS['E06']}")
    pausa(modo_teste)
    concluir(est, 7, caminho)
    return True


def t08(est, caminho, modo_teste):
    """T08 — Além da tela"""
    cabecalho(8, est)
    p("Posto de trabalho de Lia (hipótese baseada no caso — não medição real).")
    print()
    print("  Objetos  ·  frequência de uso:")
    print("    [A] Teclado            — muito frequente")
    print("    [B] Telefone           — frequente")
    print("    [C] Bandeja de entrada — frequente")
    print("    [D] Arquivo de consulta — raro")
    print()
    print("  Posições disponíveis:")
    print("    [1] Frente imediata  [2] Esquerda  [3] Direita  [4] Fundo/secundária")
    print()
    p("Situação atual: Lia gira o corpo para alcançar o telefone repetidamente.")
    p("→ Caderno: desenhe uma disposição melhor antes de configurar aqui.")
    print(); ln(); print("\n  CONFIGURAR DISPOSIÇÃO\n")

    resps = get_resp(est, "t08").copy()
    posicoes = {}
    autos_obj = {"A": "1", "B": "2", "C": "3", "D": "4"}

    for cod, nome, _ in [("A","Teclado",None), ("B","Telefone",None),
                          ("C","Bandeja",None), ("D","Arquivo",None)]:
        if resps.get(cod):
            print(f"  {nome}: posição {resps[cod]} ✓")
            posicoes[cod] = resps[cod]
            continue
        r, cmd = inp(f"{nome} → posição (1/2/3/4)",
                     validos=["1","2","3","4"], modo_teste=modo_teste, auto=autos_obj[cod])
        if cmd: global_cmd(cmd, est, 8, caminho)
        posicoes[cod] = r
        resps[cod] = r
        set_resp(est, "t08", resps, caminho)

    # Validar: itens frequentes não podem estar todos no fundo
    freq_no_fundo = all(posicoes.get(c) == "4" for c in ["A","B","C"])
    nomes_pos = {"1": "frente", "2": "esquerda", "3": "direita", "4": "fundo"}
    if freq_no_fundo:
        p("⚠ Itens frequentes ficaram todos no fundo. Considere deixá-los mais acessíveis.")
    else:
        print(); print("  Nova disposição:")
        for c, n in [("A","Teclado"), ("B","Telefone"), ("C","Bandeja"), ("D","Arquivo")]:
            print(f"    {n}: {nomes_pos.get(posicoes.get(c,'?'), '?')}")

    print()
    p("Registre uma condição a verificar com a pessoa real:")
    r_lim, cmd = inp("Condição", modo_teste=modo_teste,
                     auto="Verificar se Lia é destra para ajustar o lado do telefone")
    if cmd: global_cmd(cmd, est, 8, caminho)
    resps["limite"] = r_lim
    set_resp(est, "t08", resps, caminho)

    print()
    add_pista(est, "E07", caminho)
    p(f"🔍 Pista E07: {PISTAS['E07']}")
    p("→ As regiões de alcance são hipóteses do desenho, não medidas universais.")
    pausa(modo_teste)
    concluir(est, 8, caminho)
    return True


def t09(est, caminho, modo_teste):
    """T09 — Mais rápido significa melhor?"""
    cabecalho(9, est)
    p("Resultados fictícios — 20 atendimentos por versão:")
    print()
    print("  ┌─────────┬──────────────┬──────────────────────┬─────────────────┐")
    print("  │ Versão  │ Tempo médio  │ Registros incorretos │ Campos refeitos │")
    print("  ├─────────┼──────────────┼──────────────────────┼─────────────────┤")
    print("  │   A     │   38 s       │         5            │       12        │")
    print("  │   B     │   47 s       │         1            │        2        │")
    print("  │   C     │   43 s       │         2            │        0        │")
    print("  └─────────┴──────────────┴──────────────────────┴─────────────────┘")
    print()
    p("Critérios: tempo médio ≤ 50 s  e  registros incorretos ≤ 1")
    p("→ Caderno: anote os critérios e os resultados antes de decidir.")
    print(); ln(); print("\n  ANÁLISE\n")

    while True:
        r1, cmd = inp("Versão que atende os dois critérios (A/B/C)",
                      validos=["A","B","C"], modo_teste=modo_teste, auto="B")
        if cmd: global_cmd(cmd, est, 9, caminho); continue
        r1 = r1.upper()
        if r1 == "B":
            print("  ✅ Versão B — 47s (≤50) e 1 incorreto (≤1).\n")
        else:
            erros = {"A": "5 incorretos", "C": "2 incorretos"}
            add_tentativa(est, "t09_v", caminho)
            print(f"  ❌ Versão {r1} falha: {erros.get(r1,'')}. A resposta é Versão B.")
            r1 = "B"
        break

    p("Calcule: 1 registro incorreto em 20 × 100 =")
    r2, cmd = inp("Porcentagem (%)", modo_teste=modo_teste, auto="5")
    if cmd: global_cmd(cmd, est, 9, caminho)
    ok2 = "5" in r2.replace("%", "").strip()
    if ok2:
        print("  ✅ 5%")
    else:
        add_tentativa(est, "t09_pct", caminho)
        print("  ℹ️  1 ÷ 20 × 100 = 5%")

    print()
    p("Informe uma limitação deste teste (campo aberto para devolutiva docente):")
    r3, cmd = inp("Limitação", modo_teste=modo_teste,
                  auto="Testes em laboratório sem interrupções não reproduzem o ambiente real da recepção")
    if cmd: global_cmd(cmd, est, 9, caminho)

    set_resp(est, "t09", {"versao": r1, "pct": "5%", "limitacao": r3}, caminho)
    est["relatorio"]["t09_versao"] = r1
    est["relatorio"]["t09_pct"]    = "5%"
    salvar(est, caminho)

    print()
    add_pista(est, "E08", caminho)
    p(f"🔍 Pista E08: {PISTAS['E08']}")
    pausa(modo_teste)
    concluir(est, 9, caminho)
    return True


def t10(est, caminho, modo_teste):
    """T10 — Reconstruindo os acontecimentos"""
    cabecalho(10, est)
    p("Depoimentos:")
    print("  [L] Lia:        'O telefone tocou durante o atendimento.'")
    print("  [C] Colega:     'Acho que ela já tinha conferido o destino.'")
    print("  [S] Supervisor: 'O botão maior deveria ter resolvido o problema.'")
    print()
    p("Histórico de eventos (fictício, preparado para a atividade):")
    print()
    evs = [
        "EV1 · 14:02 — Formulário aberto com prédio 28 já selecionado",
        "EV2 · 14:03 — Categoria K, armário 19 e descrição preenchidos",
        "EV3 · 14:04 — Atendimento telefônico iniciado",
        "EV4 · 14:06 — Retorno ao formulário",
        "EV5 · 14:06 — Comando Concluir acionado",
        "EV6 · 14:06 — Registro encerrado com prédio 28",
    ]
    for ev in evs: print(f"  {ev}")
    print(); ln(); print("\n  ANÁLISE\n")

    p("1) Ordene os 6 eventos (já estão na sequência correta neste caso — confirme):")
    r1, cmd = inp("Sequência (ex: EV1,EV2,EV3,EV4,EV5,EV6)",
                  modo_teste=modo_teste, auto="EV1,EV2,EV3,EV4,EV5,EV6")
    if cmd: global_cmd(cmd, est, 10, caminho)
    gab_ev = ["EV1","EV2","EV3","EV4","EV5","EV6"]
    tent_ev = [e.strip().upper() for e in r1.split(",")]
    if tent_ev == gab_ev:
        print("  ✅ Sequência correta.")
    else:
        add_tentativa(est, "t10_ord", caminho)
        print("  ℹ️  Sequência: EV1→EV2→EV3→EV4→EV5→EV6")

    p("\n2) Afirmação APOIADA pelo histórico:")
    print("    [1] Lia atendeu ao telefone durante o preenchimento")
    print("    [2] Lia conferiu conscientemente o destino antes de concluir")
    print("    [3] O botão maior causou o erro")
    r2, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="1")
    if cmd: global_cmd(cmd, est, 10, caminho)
    if r2 == "1":
        print("  ✅ EV3 apoia que houve atendimento telefônico.")
    else:
        add_tentativa(est, "t10_ap", caminho)
        print("  ℹ️  EV3 apoia que houve atendimento telefônico (única ação registrada nesse sentido).")
        r2 = "1"

    p("\n3) Afirmação que o histórico NÃO permite confirmar:")
    print("    [1] O formulário foi aberto às 14:02")
    print("    [2] Houve atendimento telefônico")
    print("    [3] Lia verificou conscientemente o destino antes de concluir")
    r3, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="3")
    if cmd: global_cmd(cmd, est, 10, caminho)
    if r3 == "3":
        print("  ✅ O histórico mostra ações, não intenções. Não confirma verificação consciente.")
    else:
        add_tentativa(est, "t10_nap", caminho)
        print("  ℹ️  O histórico não revela intenções — não confirma se Lia verificou conscientemente.")
        r3 = "3"

    print()
    p("4) Revise suas hipóteses iniciais:")
    for i, h in enumerate(est.get("hipoteses_iniciais", []), 1):
        print(f"  Original {i}: {h}")
    print()
    r4, cmd = inp("Hipótese revisada (campo aberto)",
                  modo_teste=modo_teste,
                  auto="A interface iniciou com prédio errado e não exigiu revisão do destino antes de concluir")
    if cmd: global_cmd(cmd, est, 10, caminho)
    est["hipoteses_revisadas"] = [r4]
    salvar(est, caminho)

    set_resp(est, "t10", {"ordem": r1, "apoiada": r2, "nao_ap": r3, "rev": r4}, caminho)

    print()
    add_pista(est, "E09", caminho)
    p(f"🔍 Pista E09: {PISTAS['E09']}")
    pausa(modo_teste)
    concluir(est, 10, caminho)
    return True


def t11(est, caminho, modo_teste):
    """T11 — O relatório da equipe"""
    cabecalho(11, est)
    p("Monte quatro relações encadeadas:")
    p("  Evidência → Problema / risco → Melhoria → Como verificar")
    print()
    p("Exemplo aceito: E05 → perda de dados válidos → preservar campos → testar se apenas o campo corrigido muda")
    print(); ln()

    temas_rel = [
        ("R1", "Retomada após interrupção",   "E03",      "preservar dados e indicar ponto de retomada"),
        ("R2", "Conferência do destino",       "E02,E06",  "revisão explícita do destino antes de confirmar"),
        ("R3", "Correção de dados",            "E05",      "alterar apenas o campo errado, preservar os válidos"),
        ("R4", "Organização do posto",         "E07",      "colocar itens frequentes em posição acessível"),
    ]

    relacoes = get_resp(est, "t11").copy() if get_resp(est, "t11") else {}

    for r_id, tema, ev_sug, melhoria_sug in temas_rel:
        print(f"\n  ── {r_id}: {tema}\n")

        ev, cmd = inp("  Evidência(s) (ex: E03)", modo_teste=modo_teste, auto=ev_sug)
        if cmd: global_cmd(cmd, est, 11, caminho)

        prob, cmd = inp("  Problema ou risco", modo_teste=modo_teste,
                        auto=f"Ausência de {melhoria_sug.split()[0]}")
        if cmd: global_cmd(cmd, est, 11, caminho)

        mel, cmd = inp("  Melhoria proposta", modo_teste=modo_teste, auto=melhoria_sug)
        if cmd: global_cmd(cmd, est, 11, caminho)

        ver, cmd = inp("  Como verificar", modo_teste=modo_teste,
                       auto="Testar com 20 atendimentos e medir registros incorretos")
        if cmd: global_cmd(cmd, est, 11, caminho)

        relacoes[r_id] = {"tema": tema, "ev": ev, "prob": prob, "mel": mel, "ver": ver}
        set_resp(est, "t11", relacoes, caminho)

    # Recuperar conclusão da T9
    print(); ln(); print("\n  CONCLUSÃO QUANTITATIVA (recuperada da Tela 9)\n")
    t9r = get_resp(est, "t09")
    if t9r:
        print(f"  Versão escolhida: {t9r.get('versao','?')}  ·  {t9r.get('pct','?')} de incorretos")
        print(f"  Limitação: {t9r.get('limitacao','?')}")
    else:
        p("⚠ Tela 9 ainda não concluída — volte para completá-la antes de fechar o relatório.")

    print()
    r_inc, cmd = inp("Incerteza que a investigação NÃO resolveu",
                     modo_teste=modo_teste,
                     auto="Não sabemos se o aviso de campanha ou o telefone foi o principal fator de distração")
    if cmd: global_cmd(cmd, est, 11, caminho)
    relacoes["incerteza"] = r_inc
    set_resp(est, "t11", relacoes, caminho)

    print()
    p("✅ Relatório construído: 4 relações, conclusão quantitativa e incerteza registradas.")
    pausa(modo_teste)
    concluir(est, 11, caminho)
    return True


def t12(est, caminho, modo_teste):
    """T12 — A recepção reabriu"""
    cabecalho(12, est)
    p("A recepção reabriu. Novo atendimento para aplicar o que investigou.")
    print()
    print("  NOVO CASO:")
    print("    Objeto:    caderno vermelho")
    print("    Categoria: Documento")
    print("    Prédio:    C")
    print("    Armário:   2")
    print()
    p("⚠ A nova interface preserva campos e indica a etapa após interrupção.")
    p("⚠ AINDA inicia com Prédio A selecionado — o risco não foi eliminado sozinho.")
    p("→ Caderno: converta o caso antes de preencher aqui.")
    print(); ln(); print("\n  ETAPA 1 — CONVERTER O NOVO CASO\n")

    gab = {"predio": "63", "cat": "D", "local": "16", "desc": "caderno vermelho"}
    campos = [
        ("predio", "Código do Prédio C",    "prédio"),
        ("cat",    "Código de Documento",   "categoria"),
        ("local",  "Código do Armário 2",   "local"),
        ("desc",   "Descrição do objeto",   "descrição"),
    ]
    resps = get_resp(est, "t12").copy()

    for chave, rotulo, cat_n in campos:
        if resps.get(chave, "").lower() == gab[chave].lower():
            print(f"  {rotulo}: {resps[chave]} ✓"); continue
        while True:
            r, cmd = inp(rotulo, modo_teste=modo_teste, auto=gab[chave])
            if cmd: global_cmd(cmd, est, 12, caminho); continue
            ok = r.strip().lower() == gab[chave].lower() if chave != "desc" else \
                 ("caderno" in r.lower() or "vermelho" in r.lower())
            if ok:
                resps[chave] = r.strip()
                set_resp(est, "t12", resps, caminho)
                print(f"  ✅ {rotulo}: {r}")
                break
            else:
                add_tentativa(est, "t12_conv", caminho)
                print(f"  ℹ️  {rotulo} = {gab[chave]}")
                resps[chave] = gab[chave]
                set_resp(est, "t12", resps, caminho)
                break

    print(); ln(); print("\n  ETAPA 2 — CONFIGURAR APOIO\n")
    p("Ativar revisão de destino antes de concluir? (recomendado pela investigação)")
    print("    [S] Sim · [N] Não")
    r_cfg, cmd = inp("Escolha (S/N)", validos=["S","N"], modo_teste=modo_teste, auto="S")
    if cmd: global_cmd(cmd, est, 12, caminho)
    r_cfg = r_cfg.upper()
    if r_cfg == "S":
        print("  ✅ Apoio de revisão ativado.")
    else:
        p("⚠ Sem apoio, o risco do prédio padrão permanece. A E06 indica essa melhoria.")
    resps["config"] = r_cfg
    set_resp(est, "t12", resps, caminho)

    print(); ln(); print("\n  ETAPA 3 — ATENDIMENTO\n")
    p("Preenchendo o formulário:")
    print(f"  Prédio: {resps.get('predio','63')} (alterado de 28 → 63 ✓)")
    print(f"  Categoria: {resps.get('cat','D')} ✓")
    print(f"  Armário: {resps.get('local','16')} ✓")
    print(f"  Descrição: {resps.get('desc','caderno vermelho')} ✓")
    print()
    print("  ── 🔔  INTERRUPÇÃO ────────────────────────────────────")
    p("Uma pessoa chegou. Ao retornar:")
    print("  Todos os campos preservados. Indicador: → Próxima ação: Concluir")
    print()
    pausa(modo_teste)

    if r_cfg == "S":
        print("  ── REVISÃO DO DESTINO ─────────────────────────────────")
        print()
        print(f"  Resumo antes de concluir:")
        print(f"  Prédio C (63) · Documento (D) · Armário 2 (16) · caderno vermelho")
        print()
        r_rev, cmd = inp("Destino correto? (S/N)", validos=["S","N"], modo_teste=modo_teste, auto="S")
        if cmd: global_cmd(cmd, est, 12, caminho)
        r_rev = r_rev.upper()
        resps["revisao"] = r_rev
        set_resp(est, "t12", resps, caminho)
        if r_rev == "S":
            print("  ✅ Registro concluído: 63 / D / 16 / caderno vermelho")
        else:
            p("⚠ Ao identificar erro, corrija apenas o campo divergente (E05).")

    print(); ln(); print("\n  ETAPA 4 — VERIFICAÇÃO FINAL\n")
    p("Escolha a verificação mais pertinente para este caso:")
    print("    [1] Confirmar se o prédio gravado corresponde à ficha")
    print("    [2] Contar quantos campos foram preenchidos")
    print("    [3] Verificar se a conexão de rede funcionou")
    r_ver, cmd = inp("Escolha (1/2/3)", validos=["1","2","3"], modo_teste=modo_teste, auto="1")
    if cmd: global_cmd(cmd, est, 12, caminho)
    if r_ver == "1":
        print("  ✅ Verificação direta e compatível com o problema investigado.")
    else:
        add_tentativa(est, "t12_ver", caminho)
        print("  ℹ️  Confirmar o prédio gravado é a verificação mais direta.")
    resps["verif"] = r_ver
    set_resp(est, "t12", resps, caminho)

    print()
    ln("═"); print()
    print("  🏁  INVESTIGAÇÃO CONCLUÍDA — INCIDENTE 074")
    print()
    p("Sua equipe utilizou evidências, revisou hipóteses e aplicou as melhorias a um novo atendimento.")
    print()
    p(f"Equipe       : {est['equipe']}")
    p(f"Pistas       : {len(est['pistas'])}/9 coletadas (E01–E09)")
    p(f"Etapas       : 12/12")
    p(f"Arquivo salvo: {caminho}")
    print(); ln("═")

    concluir(est, 12, caminho)
    return True


# ═══════════════════════════════════════════════════════════════
#  NAVEGAÇÃO E INICIALIZAÇÃO
# ═══════════════════════════════════════════════════════════════

TELAS_FN = {
    1: t01,  2: t02,  3: t03,  4: t04,
    5: t05,  6: t06,  7: t07,  8: t08,
    9: t09, 10: t10, 11: t11, 12: t12,
}


def escolher_estado(forcar_novo, modo_teste):
    DIR_SAVES.mkdir(exist_ok=True)
    saves = sorted(DIR_SAVES.glob("*.json"))

    if forcar_novo or not saves:
        if modo_teste:
            nome = "equipe_teste"
        else:
            print("\n  INCIDENTE 074 — Nova investigação\n")
            nome = input("  Nome do arquivo da equipe (ex: dupla01): ").strip() or "equipe"
        caminho = DIR_SAVES / f"{nome}.json"
        est = novo_estado()
        salvar(est, caminho)
        return est, caminho

    # Saves existentes
    cls()
    titulo("INCIDENTE 074 — Investigação em IHC")
    print()
    print("  Investigações encontradas:\n")
    for i, s in enumerate(saves, 1):
        try:
            d = carregar(s)
            print(f"    [{i}] {s.stem:<20} equipe: {d.get('equipe','?'):<15} tela {d.get('tela_atual',1)}/12")
        except Exception:
            print(f"    [{i}] {s.stem}  (arquivo com problema)")
    print(f"\n    [N] Nova investigação")
    print()

    if modo_teste:
        escolha = "1"
    else:
        escolha = input("  Escolha: ").strip()

    if escolha.upper() == "N" or not escolha:
        nome = input("  Nome do arquivo: ").strip() or "equipe"
        caminho = DIR_SAVES / f"{nome}.json"
        est = novo_estado()
        salvar(est, caminho)
        return est, caminho

    try:
        idx = int(escolha) - 1
        caminho = saves[idx]
        est = carregar(caminho)
        print(f"\n  ▶ Continuando: {caminho.stem}  (tela {est['tela_atual']})")
        if not modo_teste:
            input("  [ ENTER ] ")
        return est, caminho
    except Exception:
        nome = "equipe"
        caminho = DIR_SAVES / f"{nome}.json"
        est = novo_estado()
        salvar(est, caminho)
        return est, caminho


def mostrar_menu_telas(est, caminho, modo_teste):
    """Exibe menu de seleção de telas e retorna a tela escolhida."""
    if modo_teste:
        return est["tela_atual"]
    cls()
    titulo("MENU DE TELAS")
    print()
    for n in range(1, 13):
        concl = "✓" if n in est["etapas_concluidas"] else " "
        atual = "◀" if n == est["tela_atual"] else " "
        print(f"  [{concl}] {n:2d}.  {NOMES_TELAS[n]} {atual}")
    print()
    print("  [0] Sair e salvar")
    print()
    r = input("  Ir para a tela: ").strip()
    if r == "0":
        salvar(est, caminho)
        print("  Progresso salvo. Até logo!")
        sys.exit(0)
    try:
        n = int(r)
        if 1 <= n <= 12:
            return n
    except Exception:
        pass
    return est["tela_atual"]


def main():
    forcar_novo  = "--novo"  in sys.argv
    modo_teste   = "--teste" in sys.argv or "--test" in sys.argv

    if not modo_teste:
        cls()

    est, caminho = escolher_estado(forcar_novo, modo_teste)

    tela_n = est["tela_atual"]

    while tela_n <= 12:
        fn = TELAS_FN.get(tela_n)
        if fn is None:
            break
        try:
            fn(est, caminho, modo_teste)
            tela_n = est["tela_atual"]
        except SystemExit:
            raise
        except KeyboardInterrupt:
            salvar(est, caminho)
            print("\n\n  Progresso salvo. Até logo!\n")
            sys.exit(0)
        except Exception as e:
            salvar(est, caminho)
            print(f"\n  ⚠ Erro na tela {tela_n}: {e}")
            import traceback; traceback.print_exc()
            if not modo_teste:
                input("  [ ENTER para continuar ] ")
            tela_n = est["tela_atual"]

    if not modo_teste:
        print()
    titulo("INVESTIGAÇÃO CONCLUÍDA — INCIDENTE 074")
    print()
    p(f"Equipe   : {est['equipe']}")
    p(f"Pistas   : {len(est['pistas'])}/9")
    p(f"Arquivo  : {caminho}")
    print()
    print("  ERGONOMIA_INVESTIGACAO_PASS")
    print()


if __name__ == "__main__":
    main()
