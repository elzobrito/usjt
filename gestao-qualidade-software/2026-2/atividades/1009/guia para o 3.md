# Guia Didático — Exercício 3: Escrevendo Testes para ContaBancaria

## 🎯 O que você vai aprender

Antes de qualquer código, entenda **o que este exercício pede**:

> Você recebe uma classe pronta. Sua tarefa **não** é implementá-la.
> Sua tarefa é **provar que ela funciona** — escrevendo testes.

Isso é o que programadores profissionais fazem todos os dias.

---

## 📚 Conceitos que você precisa entender

---

## 1. O que é uma Classe?

Uma **classe** é um molde para criar objetos. Pense assim:

```
Classe ContaBancaria  →  é o molde (a planta de uma casa)
objeto conta          →  é a instância (a casa construída)
```

Para criar um objeto a partir de uma classe:

```python
#         classe        titular   saldo inicial
#           ↓              ↓          ↓
conta = ContaBancaria("Maria", 500.0)
```

Após isso, `conta` é um objeto do tipo `ContaBancaria` com:
- `conta.titular` → `"Maria"`
- `conta.saldo`   → `500.0`

---

## 2. O que são Métodos?

Métodos são **funções que pertencem a uma classe**. Você chama assim:

```python
objeto.metodo(argumentos)
```

Exemplos com `ContaBancaria`:

```python
conta = ContaBancaria("Maria", 500.0)

conta.depositar(100)    # adiciona 100 ao saldo
conta.sacar(50)         # remove 50 do saldo
conta.transferir(outra_conta, 200)  # move 200 para outra conta
```

---

## 3. O que é uma Exceção (`ValueError`)?

Uma **exceção** é um erro que a função lança intencionalmente quando
recebe uma entrada inválida.

```python
conta = ContaBancaria("Maria", 500.0)
conta.depositar(-10)  # ← ERRO! valor negativo não é permitido
```

Quando isso acontece, o Python "lança" um `ValueError` e o programa para —
a menos que você **capture** esse erro.

### Como capturar uma exceção

```python
try:
    conta.depositar(-10)   # tenta executar
except ValueError:
    print("deu ValueError!") # captura o erro se ele acontecer
```

---

## 4. O que é `lambda`?

`lambda` cria uma **função anônima** (sem nome) em uma única linha.

Compare:

```python
# Função normal
def minha_funcao():
    return conta.depositar(-10)

# Mesma coisa com lambda
lambda: conta.depositar(-10)
```

São equivalentes. Usamos `lambda` quando precisamos passar uma função
como argumento sem precisar nomeá-la.

---

## 5. Como funciona `capturar()`?

`capturar()` é uma função auxiliar já fornecida no template.
Ela executa uma função e retorna:
- `"ValueError"` se uma exceção foi lançada
- `"sem excecao"` se tudo correu bem

```python
def capturar(fn) -> str:
    try:
        fn()          # tenta executar a função
        return "sem excecao"
    except ValueError:
        return "ValueError"
```

### Na prática

```python
conta = ContaBancaria("Maria", 500.0)

capturar(lambda: conta.depositar(100))   # → "sem excecao"
capturar(lambda: conta.depositar(-10))   # → "ValueError"
capturar(lambda: conta.depositar(0))     # → "ValueError"
```

---

## 6. Como funciona `verificar()`?

```python
verificar(nome, esperado, obtido)
```

| Parâmetro | O que é |
|---|---|
| `nome` | Nome do teste (para aparecer no terminal) |
| `esperado` | O valor que você **espera** que a função retorne |
| `obtido` | O valor que a função **realmente** retornou |

Ela compara `esperado` com `obtido`:
- Se forem iguais → `✅ PASSOU`
- Se forem diferentes → `❌ FALHOU`

### Exemplos

```python
conta = ContaBancaria("Maria", 500.0)

# Testando valor retornado
verificar("deposito valido", 600.0, conta.depositar(100))
#                              ↑            ↑
#                          esperado       obtido

# Testando exceção
verificar("deposito negativo", "ValueError", capturar(lambda: conta.depositar(-10)))
#                                  ↑                        ↑
#                              esperado            capturar retorna "ValueError"
```

---

## 7. Como montar um teste completo

Todo teste segue **três etapas**:

```
1. PREPARAR  →  crie o objeto com o estado necessário
2. AGIR      →  execute o método que está testando
3. VERIFICAR →  confirme que o resultado é o esperado
```

### Exemplo para `depositar`

```python
# 1. PREPARAR
conta = ContaBancaria("Ana", 200.0)

# 2. AGIR + 3. VERIFICAR (em uma linha só)
resultados.append(verificar("deposito valido", 250.0, conta.depositar(50)))
```

Explicação:
- Criamos uma conta com saldo `200.0`
- Depositamos `50`
- Esperamos que o retorno seja `250.0`
- Se `conta.depositar(50)` retornar `250.0` → ✅

---

## 8. Testes com Exceção — passo a passo

```python
# 1. PREPARAR
conta = ContaBancaria("Ana", 200.0)

# 2. AGIR + 3. VERIFICAR
resultados.append(
    verificar(
        "deposito negativo",           # nome do teste
        "ValueError",                  # esperado: deve lançar ValueError
        capturar(lambda: conta.depositar(-10))  # obtido: captura o que acontece
    )
)
```

Fluxo interno:
```
capturar(lambda: conta.depositar(-10))
    → tenta executar conta.depositar(-10)
    → depositar lança ValueError (valor negativo)
    → capturar captura e retorna "ValueError"

verificar("deposito negativo", "ValueError", "ValueError")
    → esperado == obtido → ✅ PASSOU
```

---

## 9. Isolamento de testes ⚠️

> **Regra de ouro: cada teste usa sua própria conta.**

Veja o problema de reutilizar a mesma conta:

```python
# ❌ ERRADO
conta = ContaBancaria("Ana", 100.0)

resultados.append(verificar("saque 80", 20.0, conta.sacar(80)))
# saldo agora é 20.0

resultados.append(verificar("saque 30", "ValueError", capturar(lambda: conta.sacar(30))))
# saldo é 20, sacar 30 realmente falha — mas pelo motivo certo?
# E se o saldo fosse 100? Também falharia? NÃO! Então o teste é inválido.
```

```python
# ✅ CORRETO
conta1 = ContaBancaria("Ana", 100.0)
resultados.append(verificar("saque 80", 20.0, conta1.sacar(80)))

conta2 = ContaBancaria("Ana", 100.0)  # conta nova, saldo zerado
resultados.append(verificar("saque 30 insuficiente", "ValueError", capturar(lambda: conta2.sacar(130))))
```

---

## 10. Guia por método — o que testar

---

### 🔵 `depositar(valor)`

Você precisa cobrir estas situações:

#### Casos válidos (sem exceção)

| Situação | Como criar | Esperado |
|---|---|---|
| Depósito simples | `conta.depositar(100)` | novo saldo como `float` |
| Dois depósitos seguidos | depositar duas vezes | saldo acumulado |
| Depósito com `float` | `conta.depositar(0.01)` | saldo correto |

**Exemplo:**
```python
conta = ContaBancaria("Ana", 200.0)
resultados.append(verificar("deposito simples", 300.0, conta.depositar(100)))
```

#### Casos inválidos (com exceção)

| Situação | Entrada | Por que falha |
|---|---|---|
| Valor zero | `0` | R2: deve ser `> 0` |
| Valor negativo | `-50` | R2: deve ser `> 0` |
| String | `"cem"` | R1: não é número |
| `None` | `None` | R1: não é número |
| Booleano | `True` | R1: `bool` não é aceito |

**Exemplo:**
```python
conta = ContaBancaria("Ana", 200.0)
resultados.append(verificar("deposito zero", "ValueError", capturar(lambda: conta.depositar(0))))
```

> 💡 **Por que `True` é inválido?**
> Em Python, `bool` é subclasse de `int`, então `isinstance(True, int)` retorna `True`.
> A classe trata isso explicitamente como erro para evitar bugs silenciosos.

---

### 🟡 `sacar(valor)`

#### Casos válidos

| Situação | Como criar | Esperado |
|---|---|---|
| Saque simples | conta com 200, sacar 50 | `150.0` |
| Saque do valor exato | conta com 100, sacar 100 | `0.0` |

**Exemplo:**
```python
conta = ContaBancaria("Ana", 200.0)
resultados.append(verificar("saque simples", 150.0, conta.sacar(50)))
```

```python
conta = ContaBancaria("Ana", 100.0)
resultados.append(verificar("saque total", 0.0, conta.sacar(100)))
```

#### Casos inválidos

| Situação | Entrada | Por que falha |
|---|---|---|
| Valor zero | `0` | R2: deve ser `> 0` |
| Valor negativo | `-10` | R2: deve ser `> 0` |
| Maior que saldo | conta com 100, sacar 200 | R3: saldo insuficiente |
| String | `"cinquenta"` | R1: não é número |

**Fronteira importante:**
```python
# Saldo exato: deve funcionar
conta = ContaBancaria("Ana", 100.0)
resultados.append(verificar("saque exato", 0.0, conta.sacar(100)))

# Um centavo a mais: deve falhar
conta = ContaBancaria("Ana", 100.0)
resultados.append(verificar("saque acima", "ValueError", capturar(lambda: conta.sacar(100.01))))
```

---

### 🔴 `transferir(destino, valor)`

Este método envolve **duas contas**. Sempre crie as duas:

```python
origem  = ContaBancaria("Ana",  500.0)
destino = ContaBancaria("Beto", 100.0)
```

#### Casos válidos

| Situação | Esperado |
|---|---|
| Transferência válida | retorna `(saldo_origem, saldo_destino)` |
| Saldo de origem diminuiu | `origem.saldo` correto |
| Saldo de destino aumentou | `destino.saldo` correto |

**Exemplo:**
```python
origem  = ContaBancaria("Ana",  500.0)
destino = ContaBancaria("Beto", 100.0)
resultado = origem.transferir(destino, 200)

resultados.append(verificar("retorno da transferencia", (300.0, 300.0), resultado))
resultados.append(verificar("saldo origem", 300.0, origem.saldo))
resultados.append(verificar("saldo destino", 300.0, destino.saldo))
```

#### Casos inválidos

| Situação | Como criar | Por que falha |
|---|---|---|
| Destino não é ContaBancaria | `origem.transferir("Beto", 100)` | R1 |
| Transferência para si mesmo | `origem.transferir(origem, 100)` | R2 |
| Valor zero | `origem.transferir(destino, 0)` | R4 |
| Valor negativo | `origem.transferir(destino, -50)` | R4 |
| Saldo insuficiente | conta com 100, transferir 200 | R5 |

**Exemplo:**
```python
conta = ContaBancaria("Ana", 100.0)
resultados.append(
    verificar("transferencia para si", "ValueError",
              capturar(lambda: conta.transferir(conta, 50)))
)
```

---

## 11. Template preenchido — exemplo completo

Veja um exemplo de como preencher **dois testes** no template:

```python
def testar_depositar():
    resultados = []

    # Teste 1: depósito válido retorna o novo saldo
    conta = ContaBancaria("Ana", 200.0)
    resultados.append(verificar("deposito valido", 300.0, conta.depositar(100)))

    # Teste 2: valor zero lança ValueError
    conta = ContaBancaria("Ana", 200.0)
    resultados.append(
        verificar("deposito zero", "ValueError", capturar(lambda: conta.depositar(0)))
    )

    return resultados
```

> Note: sempre `return resultados` no final — sem isso, os testes não são contados!

---

## 12. Checklist antes de entregar

Antes de submeter, responda:

- [ ] Tenho pelo menos **3 testes em cada método** (9 no total)?
- [ ] Cada método tem testes de casos **válidos** (sem exceção)?
- [ ] Cada método tem testes de casos **inválidos** (com exceção)?
- [ ] Cada teste usa uma **conta nova** (não reaproveitei o mesmo objeto)?
- [ ] Todos os testes estão retornando `✅ PASSOU` no terminal?
- [ ] Preenchi as tabelas do caderno com as classes de equivalência?

---

## 13. Mapa mental do exercício

```
ContaBancaria
│
├── depositar(valor)
│   ├── ✅ válido   → retorna novo saldo (float)
│   └── ❌ inválido → lança ValueError
│       ├── valor ≤ 0
│       └── valor não é número (str, None, bool)
│
├── sacar(valor)
│   ├── ✅ válido   → retorna novo saldo (float)
│   └── ❌ inválido → lança ValueError
│       ├── valor ≤ 0
│       ├── valor > saldo
│       └── valor não é número
│
└── transferir(destino, valor)
    ├── ✅ válido   → retorna (saldo_origem, saldo_destino)
    └── ❌ inválido → lança ValueError
        ├── destino não é ContaBancaria
        ├── destino é a própria conta
        ├── valor ≤ 0
        ├── valor > saldo
        └── valor não é número
```

---

## 💬 Resumo em uma frase

> **Um bom teste diz claramente: dado este estado, com esta entrada, espero este resultado — e prova que o código cumpre o combinado.**