"""Módulo com a classe ContaBancaria — NÃO MODIFIQUE ESTE ARQUIVO."""


class ContaBancaria:
    """Representa uma conta bancária simples."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        if not isinstance(titular, str) or titular.strip() == "":
            raise ValueError("Titular inválido")
        if not isinstance(saldo_inicial, (int, float)) or isinstance(saldo_inicial, bool):
            raise ValueError("Saldo inicial inválido")
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo")
        self.titular = titular.strip()
        self.saldo = float(saldo_inicial)

    # ------------------------------------------------------------------
    # Função 1: depositar
    # ------------------------------------------------------------------
    def depositar(self, valor: float) -> float:
        """Deposita um valor na conta e retorna o novo saldo.

        Regras:
            - valor deve ser int ou float (bool não é aceito)
            - valor deve ser estritamente positivo (> 0)
            - retorna o novo saldo como float
            - lança ValueError em qualquer violação das regras acima
        """
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("Valor inválido: deve ser numérico")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += float(valor)
        return self.saldo

    # ------------------------------------------------------------------
    # Função 2: sacar
    # ------------------------------------------------------------------
    def sacar(self, valor: float) -> float:
        """Saca um valor da conta e retorna o novo saldo.

        Regras:
            - valor deve ser int ou float (bool não é aceito)
            - valor deve ser estritamente positivo (> 0)
            - valor não pode ser maior que o saldo disponível
            - retorna o novo saldo como float
            - lança ValueError em qualquer violação das regras acima
        """
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("Valor inválido: deve ser numérico")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= float(valor)
        return self.saldo

    # ------------------------------------------------------------------
    # Função 3: transferir
    # ------------------------------------------------------------------
    def transferir(self, destino: "ContaBancaria", valor: float) -> tuple:
        """Transfere um valor para outra conta.

        Regras:
            - destino deve ser uma instância de ContaBancaria
            - destino não pode ser a própria conta (mesma instância)
            - valor deve ser int ou float (bool não é aceito)
            - valor deve ser estritamente positivo (> 0)
            - valor não pode ser maior que o saldo disponível
            - retorna uma tupla (saldo_origem, saldo_destino) após a transferência
            - lança ValueError em qualquer violação das regras acima
        """
        if not isinstance(destino, ContaBancaria):
            raise ValueError("Destino inválido: deve ser uma ContaBancaria")
        if destino is self:
            raise ValueError("Não é possível transferir para a própria conta")
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("Valor inválido: deve ser numérico")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= float(valor)
        destino.saldo += float(valor)
        return (self.saldo, destino.saldo)

    def __repr__(self):
        return f"ContaBancaria(titular={self.titular!r}, saldo={self.saldo:.2f})"

