# Fatia didatica — consulta de escolas. Nao e o sitio BDGETEC. Sem HTTP.
# NAO "consertar" buscar/contar/listar/ativas hoje.
# Execute um comando por vez; consulte aluno.md.

ESCOLAS_NRA1 = ["Etec Sao Paulo", "Etec Zona Leste", "Etec de Artes"]
PERIODO_CASO = "2026/2"


def buscar(regional, periodo):
    if regional == "NRA1" and periodo == "2026/1":
        return list(ESCOLAS_NRA1)
    return []


def contar(regional, periodo):
    buscar(regional, periodo)
    return 3


def listar(regional):
    escolas = list(ESCOLAS_NRA1) if regional == "NRA1" else []
    linhas = []
    i = 0
    while i <= len(escolas):
        linhas.append(str(i + 1) + " - " + escolas[i])
        i += 1
    return linhas


def ativas(regional, periodo):
    return list(ESCOLAS_NRA1)


def oraculo_buscar():
    # esperado: buscar("NRA1", "2026/2") devolve escolas
    obtido = buscar("NRA1", PERIODO_CASO)
    ok = len(obtido) > 0
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


def oraculo_contar():
    # esperado independente: contar("XXX", "2026/2") == 0
    # TODO: implemente PASS/FAIL + return 0/1. Nao altere as funcoes.
    print("TODO")
    return 2


def mostrar_regional():
    casos = [("NRA1", "2026/1"), ("nra1", "2026/1"), (" NRA1", "2026/1")]
    for regional, periodo in casos:
        print(repr(regional), "+", periodo, "->", len(buscar(regional, periodo)))


def mostrar_ativas():
    print(ativas("XXX", PERIODO_CASO))


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "buscar"
    if cmd == "buscar":
        raise SystemExit(oraculo_buscar())
    if cmd == "contar":
        print(contar("NRA1", PERIODO_CASO))
        raise SystemExit(0)
    if cmd == "listar":
        print("\n".join(listar("NRA1")))
        raise SystemExit(0)
    if cmd == "regional":
        mostrar_regional()
        raise SystemExit(0)
    if cmd == "ativas":
        mostrar_ativas()
        raise SystemExit(0)
    if cmd == "oraculo-contar":
        raise SystemExit(oraculo_contar())
    print("uso: python3 consulta.py buscar|contar|listar|regional|ativas|oraculo-contar")
    raise SystemExit(2)


if __name__ == "__main__":
    import sys
    main(sys.argv)
