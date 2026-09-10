"""Exercicio 2: funcao pura e classes de equivalencia."""

from harness import codigo_saida, verificar


def classificar_nota(nota):
    """Implemente as regras descritas no README.

    Retornos possíveis:
        "invalido"    → nota é None, não é número, ou está fora de [0, 10]
        "reprovado"   → 0 <= nota < 5
        "recuperacao" → 5 <= nota < 7
        "aprovado"    → 7 <= nota <= 10
    """
    # Escreva sua solução aqui
    pass


def main():
    resultados = [
        verificar("nula",             "invalido",    classificar_nota(None)),
        verificar("texto",            "invalido",    classificar_nota("oito")),
        verificar("negativa",         "invalido",    classificar_nota(-1)),
        verificar("acima do maximo",  "invalido",    classificar_nota(11)),
        verificar("reprovado minimo", "reprovado",   classificar_nota(0)),
        verificar("reprovado maximo", "reprovado",   classificar_nota(4.9)),
        verificar("recuperacao minimo","recuperacao", classificar_nota(5)),
        verificar("recuperacao maximo","recuperacao", classificar_nota(6.9)),
        verificar("aprovado minimo",  "aprovado",    classificar_nota(7)),
        verificar("aprovado maximo",  "aprovado",    classificar_nota(10)),
    ]
    raise SystemExit(codigo_saida(resultados))


if __name__ == "__main__":
    main()
