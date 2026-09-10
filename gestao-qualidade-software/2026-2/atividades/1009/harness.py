"""Harness de testes — NÃO MODIFIQUE ESTE ARQUIVO."""


def verificar(nome, esperado, obtido):
    """Compara o resultado esperado com o obtido e imprime o resultado."""
    if esperado == obtido:
        print(f"  ✅ PASSOU: {nome}")
        return True
    else:
        print(f"  ❌ FALHOU: {nome} → esperado={esperado}, obtido={obtido}")
        return False


def codigo_saida(resultados):
    """Retorna 0 se todos passaram, 1 se algum falhou."""
    return 0 if all(resultados) else 1
