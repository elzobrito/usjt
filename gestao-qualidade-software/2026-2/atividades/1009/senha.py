"""Exercicio 1: funcao pura e classes de equivalencia."""

from harness import codigo_saida, verificar


def senha_forte(senha):
    """Implemente as cinco regras descritas no README."""
    if senha is None or not isinstance(senha, str):
        return False
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in "!@#$%&*" for c in senha):
        return False
    return True


def main():
    resultados = [
        verificar("curta", False, senha_forte("Ab1!")),
        verificar("sem maiuscula", False, senha_forte("senha123!")),
        verificar("sem numero", False, senha_forte("SenhaForte!")),
        verificar("sem especial", False, senha_forte("Senha1234")),
        verificar("valida", True, senha_forte("Senha@Forte2026")),
        verificar("nula", False, senha_forte(None)),
        verificar("vazia", False, senha_forte("")),
    ]
    raise SystemExit(codigo_saida(resultados))


if __name__ == "__main__":
    main()
