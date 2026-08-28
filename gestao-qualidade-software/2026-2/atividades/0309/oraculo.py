# esperado: consultar("NRA1", "2026/2") devolve escolas (lista nao vazia)
# Fatia didatica. Nao e o sitio BDGETEC. Sem HTTP.

def consultar(regional, periodo):
    if regional == "NRA1" and periodo == "2026/1":
        return ["Etec Sao Paulo", "Etec Zona Leste", "Etec de Artes"]
    return []


PERIODO_CASO = "2026/2"
obtido = consultar("NRA1", PERIODO_CASO)
ok = len(obtido) > 0
print("PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
