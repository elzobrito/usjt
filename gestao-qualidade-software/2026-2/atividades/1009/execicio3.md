# Exercício 3 — Escrevendo Testes para ContaBancaria

## 📋 Contexto

Você recebeu uma classe `ContaBancaria` **já implementada** por outro desenvolvedor.
Sua tarefa é **escrever os testes** que garantam que ela funciona corretamente.

> Esta é uma habilidade fundamental no mercado: saber testar código — não apenas escrever código.

---

## 📁 Arquivos do Exercício

| Arquivo | O que é | Pode modificar? |
|---|---|---|
| `conta.py` | Classe `ContaBancaria` implementada | ❌ Não |
| `harness.py` | Funções auxiliares de teste | ❌ Não |
| `test_conta.py` | Template onde você escreve os testes | ✅ Sim |

---

## 🏦 A Classe ContaBancaria

A classe possui **3 métodos** que você deve testar:

---

### Método 1 — `depositar(valor)`

Deposita um valor na conta e retorna o novo saldo.

**Regras:**

| # | Regra | Comportamento |
|---|---|---|
| R1 | `valor` deve ser `int` ou `float` (`bool` **não** é aceito) | Lança `ValueError` |
| R2 | `valor` deve ser estritamente positivo (`> 0`) | Lança `ValueError` |
| R3 | Depósito válido retorna o novo saldo como `float` | Retorna `float` |

---

### Método 2 — `sacar(valor)`

Saca um valor da conta e retorna o novo saldo.

**Regras:**

| # | Regra | Comportamento |
|---|---|---|
| R1 | `valor` deve ser `int` ou `float` (`bool` **não** é aceito) | Lança `ValueError` |
| R2 | `valor` deve ser estritamente positivo (`> 0`) | Lança `ValueError` |
| R3 | `valor` não pode exceder o saldo disponível | Lança `ValueError` |
| R4 | Saque válido retorna o novo saldo como `float` | Retorna `float` |

---

### Método 3 — `transferir(destino, valor)`

Transfere um valor para outra conta.

**Regras:**

| # | Regra | Comportamento |
|---|---|---|
| R1 | `destino` deve ser uma instância de `ContaBancaria` | Lança `ValueError` |
| R2 | `destino` não pode ser a própria conta | Lança `ValueError` |
| R3 | `valor` deve ser `int` ou `float` (`bool` **não** é aceito) | Lança `ValueError` |
| R4 | `valor` deve ser estritamente positivo (`> 0`) | Lança `ValueError` |
| R5 | `valor` não pode exceder o saldo disponível | Lança `ValueError` |
| R6 | Transferência válida retorna `(saldo_origem, saldo_destino)` | Retorna `tuple` |

---

## ✏️ PARTE 1 — Caderno (faça antes do computador!)

### Questão 1 — Classes de Equivalência

Para **cada método**, identifique as classes de equivalência e preencha:

#### `depositar`
| Classe | Condição | Resultado |
|---|---|---|
| | | |
| | | |
| | | |

#### `sacar`
| Classe | Condição | Resultado |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

#### `transferir`
| Classe | Condição | Resultado |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

---

### Questão 2 — Valores de Fronteira

Liste os valores de fronteira para `depositar` e `sacar`:

| Método | Valor de Fronteira | Resultado Esperado |
|---|---|---|
| `depositar` | 0 | |
| `depositar` | 0.01 | |
| `sacar` | saldo exato | |
| `sacar` | saldo + 0.01 | |

---

### Questão 3 — Planejamento dos Testes

Antes de programar, liste **todos os testes** que pretende escrever:

| # | Método | Nome do Teste | Entrada | Esperado |
|---|---|---|---|---|
| 1 | `depositar` | | | |
| 2 | `depositar` | | | |
| 3 | `depositar` | | | |
| 4 | `sacar` | | | |
| 5 | `sacar` | | | |
| 6 | `sacar` | | | |
| 7 | `transferir` | | | |
| 8 | `transferir` | | | |
| 9 | `transferir` | | | |

> Mínimo exigido: **3 testes por método** (9 no total).

---

## 💻 PARTE 2 — Computador

Abra `test_conta.py` e substitua os comentários `# TODO` pelos seus testes.

### Como criar uma conta para testar

```python
conta = ContaBancaria("Ana", 100.0)  # titular="Ana", saldo inicial=100.0
```

### Como testar um valor retornado

```python
conta = ContaBancaria("Ana", 100.0)
resultados.append(verificar("deposito valido", 150.0, conta.depositar(50)))
```

### Como testar uma exceção

Use a função `capturar()` que já está no template:

```python
conta = ContaBancaria("Ana", 100.0)
resultados.append(
    verificar("deposito zero", "ValueError", capturar(lambda: conta.depositar(0)))
)
```

> ⚠️ **Atenção:** Crie uma **nova conta** para cada teste que modifica o saldo.
> Reutilizar a mesma conta pode fazer um teste interferir no próximo!

### Como rodar

```bash
python test_conta.py
```

### Exemplo de saída esperada

```
── depositar ──────────────────────────
  ✅ PASSOU: deposito valido
  ✅ PASSOU: deposito zero
  ✅ PASSOU: deposito negativo
  ...

── sacar ──────────────────────────────
  ✅ PASSOU: saque valido
  ✅ PASSOU: saldo insuficiente
  ...

── transferir ─────────────────────────
  ✅ PASSOU: transferencia valida
  ✅ PASSOU: destino invalido
  ...

────────────────────────────────────────
  9/9 testes passaram
```

---

## 💡 Dicas Importantes

### Isolamento de testes
Cada teste deve ser **independente**. Nunca reutilize uma conta que já sofreu operações:

```python
# ❌ ERRADO — o segundo teste depende do estado do primeiro
conta = ContaBancaria("Ana", 100)
resultados.append(verificar("saque 50", 50.0, conta.sacar(50)))
resultados.append(verificar("saque 80", "ValueError", capturar(lambda: conta.sacar(80))))
# saldo agora é 50, não 100 — o segundo teste pode passar pelo motivo errado!

# ✅ CORRETO — cada teste usa sua própria conta
conta1 = ContaBancaria("Ana", 100)
resultados.append(verificar("saque 50", 50.0, conta1.sacar(50)))

conta2 = ContaBancaria("Ana", 100)
resultados.append(verificar("saque 80", "ValueError", capturar(lambda: conta2.sacar(80))))
```

### O caso do `bool`
Em Python, `bool` é subclasse de `int`:
```python
isinstance(True, int)   # → True  ← Python aceita como int!
isinstance(True, bool)  # → True
```
A classe rejeita `bool` explicitamente. Como você testaria isso?

---

## 🎯 Critérios de Avaliação

| Critério | Pontos |
|---|---|
| Mínimo de 3 testes por método (9 total) | 4,0 |
| Testes cobrem casos válidos **e** inválidos | 3,0 |
| Testes são independentes (contas separadas) | 1,5 |
| Caderno com classes de equivalência preenchidas | 1,5 |
| **Total** | **10,0** |

---

## 🔥 Desafio Extra (opcional)

Escreva um teste que verifique o que acontece quando você tenta
**criar** uma `ContaBancaria` com titular vazio ou saldo inicial negativo.

```python
capturar(lambda: ContaBancaria("", 100))     # O que deve retornar?
capturar(lambda: ContaBancaria("Ana", -50))  # E este?
```