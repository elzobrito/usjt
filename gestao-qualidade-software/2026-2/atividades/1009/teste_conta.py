""Exercicio 3: escrevendo testes para ContaBancaria."""

from conta import ContaBancaria
from harness import codigo_saida, verificar


# ------------------------------------------------------------------
# Função auxiliar — não modifique
# ------------------------------------------------------------------
def capturar(fn) -> str:
    """Executa fn() e retorna 'ValueError' se essa exceção for lançada,
    ou 'sem excecao' caso contrário.

    Uso:
        capturar(lambda: conta.depositar(-10))  →  "ValueError"
        capturar(lambda: conta.depositar(50))   →  "sem excecao"
    """
    try:
        fn()
        return "sem excecao"
    except ValueError:
        return "ValueError"


# ==================================================================
# FUNÇÃO 1 — depositar
# Regras:
#   R1. valor deve ser numérico (int ou float, bool NÃO vale)
#   R2. valor deve ser > 0
#   R3. retorna o novo saldo (float) após o depósito
# ==================================================================
def testar_depositar():
    resultados = []

    # --- Cenários VÁLIDOS ---
    # TODO: teste R3 — depósito válido retorna o novo saldo correto
    # Dica: crie uma conta com saldo inicial conhecido, deposite e verifique o retorno
    # resultados.append(verificar("deposito valido", ..., ...))

    # TODO: teste R3 — dois depósitos consecutivos acumulam corretamente
    # resultados.append(verificar("dois depositos", ..., ...))

    # --- Cenários INVÁLIDOS (devem lançar ValueError) ---
    # TODO: teste R2 — valor zero deve lançar ValueError
    # resultados.append(verificar("deposito zero", "ValueError", capturar(lambda: ...)))

    # TODO: teste R2 — valor negativo deve lançar ValueError
    # resultados.append(verificar("deposito negativo", "ValueError", capturar(lambda: ...)))

    # TODO: teste R1 — string deve lançar ValueError
    # resultados.append(verificar("deposito string", "ValueError", capturar(lambda: ...)))

    # TODO: teste R1 — None deve lançar ValueError
    # resultados.append(verificar("deposito none", "ValueError", capturar(lambda: ...)))

    # TODO: teste R1 — bool deve lançar ValueError (True é int em Python, cuidado!)
    # resultados.append(verificar("deposito bool", "ValueError", capturar(lambda: ...)))

    return resultados


# ==================================================================
# FUNÇÃO 2 — sacar
# Regras:
#   R1. valor deve ser numérico (int ou float, bool NÃO vale)
#   R2. valor deve ser > 0
#   R3. valor não pode exceder o saldo disponível
#   R4. retorna o novo saldo (float) após o saque
# ==================================================================
def testar_sacar():
    resultados = []

    # --- Cenários VÁLIDOS ---
    # TODO: teste R4 — saque válido retorna o novo saldo correto
    # resultados.append(verificar("saque valido", ..., ...))

    # TODO: teste R4 — saque do valor exato do saldo (saldo fica zerado)
    # resultados.append(verificar("saque total", ..., ...))

    # --- Cenários INVÁLIDOS (devem lançar ValueError) ---
    # TODO: teste R2 — valor zero deve lançar ValueError
    # resultados.append(verificar("saque zero", "ValueError", capturar(lambda: ...)))

    # TODO: teste R2 — valor negativo deve lançar ValueError
    # resultados.append(verificar("saque negativo", "ValueError", capturar(lambda: ...)))

    # TODO: teste R3 — valor maior que saldo deve lançar ValueError
    # resultados.append(verificar("saldo insuficiente", "ValueError", capturar(lambda: ...)))

    # TODO: teste R1 — string deve lançar ValueError
    # resultados.append(verificar("saque string", "ValueError", capturar(lambda: ...)))

    return resultados


# ==================================================================
# FUNÇÃO 3 — transferir
# Regras:
#   R1. destino deve ser uma instância de ContaBancaria
#   R2. destino não pode ser a própria conta
#   R3. valor deve ser numérico (int ou float, bool NÃO vale)
#   R4. valor deve ser > 0
#   R5. valor não pode exceder o saldo disponível
#   R6. retorna tupla (saldo_origem, saldo_destino) após a transferência
# ==================================================================
def testar_transferir():
    resultados = []

    # --- Cenários VÁLIDOS ---
    # TODO: teste R6 — transferência válida retorna os saldos corretos
    # Dica: crie duas contas e verifique a tupla retornada
    # resultados.append(verificar("transferencia valida", ..., ...))

    # TODO: teste R6 — saldo da origem diminuiu e destino aumentou corretamente
    # Dica: verifique os atributos .saldo das duas contas após a transferência
    # resultados.append(verificar("saldo origem apos transferencia", ..., ...))
    # resultados.append(verificar("saldo destino apos transferencia", ..., ...))

    # --- Cenários INVÁLIDOS (devem lançar ValueError) ---
    # TODO: teste R1 — destino que não é ContaBancaria deve lançar ValueError
    # resultados.append(verificar("destino invalido", "ValueError", capturar(lambda: ...)))

    # TODO: teste R2 — transferência para si mesmo deve lançar ValueError
    # resultados.append(verificar("transferencia para si", "ValueError", capturar(lambda: ...)))

    # TODO: teste R4 — valor zero deve lançar ValueError
    # resultados.append(verificar("transferencia zero", "ValueError", capturar(lambda: ...)))

    # TODO: teste R5 — valor maior que saldo deve lançar ValueError
    # resultados.append(verificar("transferencia sem saldo", "ValueError", capturar(lambda: ...)))

    return resultados


# ==================================================================
# NÃO MODIFIQUE ABAIXO DESTA LINHA
# ==================================================================
def main():
    print("\n── depositar ──────────────────────────")
    r1 = testar_depositar()

    print("\n── sacar ──────────────────────────────")
    r2 = testar_sacar()

    print("\n── transferir ─────────────────────────")
    r3 = testar_transferir()

    todos = r1 + r2 + r3
    total  = len(todos)
    passou = sum(todos)
    print(f"\n{'─'*40}")
    print(f"  {passou}/{total} testes passaram")
    raise SystemExit(codigo_saida(todos))


if __name__ == "__main__":
    main()

