# Exercício 1 — Validador de Senha Forte

## 📋 Objetivo

Implementar a função `senha_forte(senha)` que verifica se uma senha atende a **cinco regras de segurança**. A função deve retornar `True` quando a senha for forte, e `False` caso contrário.

---

## 📐 As Cinco Regras

| # | Regra | Exemplo válido | Exemplo inválido |
|---|-------|----------------|-----------------|
| 1 | Pelo menos **8 caracteres** | `"Senha@12"` | `"Ab1!"` |
| 2 | Pelo menos **uma letra maiúscula** (A–Z) | `"Senha@12"` | `"senha@12"` |
| 3 | Pelo menos **um número** (0–9) | `"Senha@12"` | `"Senha@ABC"` |
| 4 | Pelo menos **um caractere especial** de `!@#$%&*` | `"Senha@12"` | `"Senha1234"` |
| 5 | **Não** pode ser `None`, vazia `""` ou só espaços | `"Senha@12"` | `None`, `""`, `"   "` |

---

## 🧠 Como Pensar na Solução

Antes de escrever código, pense nas seguintes perguntas:

1. O que acontece se a senha for `None`? Posso chamar `.len()` ou `.strip()` nela?
2. Como verificar se existe **pelo menos uma** letra maiúscula em uma string?
3. Como verificar se existe **pelo menos um** dígito?
4. Como verificar se existe **pelo menos um** caractere dentro de um conjunto específico?

> 💡 **Dica:** Em Python, a função `any()` combinada com um `for` dentro dela é muito útil para verificar se *pelo menos um* elemento de uma sequência satisfaz uma condição.

---

## 🔨 Passo a Passo

### Passo 1 — Tratar os casos especiais (Regra 5)

Sempre verifique `None` e strings vazias **primeiro**, antes de qualquer outra operação. Caso contrário, seu código vai gerar um erro (`AttributeError`) ao tentar chamar métodos em `None`.

```python
if senha is None or senha.strip() == "":
    return False
```

- `senha is None` → captura o caso nulo
- `senha.strip() == ""` → captura strings vazias **e** strings com só espaços (ex: `"   "`)

---

### Passo 2 — Verificar o comprimento mínimo (Regra 1)

```python
if len(senha) < 8:
    return False
```

`len()` retorna o número de caracteres da string.

---

### Passo 3 — Verificar letra maiúscula (Regra 2)

```python
if not any(c.isupper() for c in senha):
    return False
```

- `for c in senha` percorre cada caractere da string
- `.isupper()` retorna `True` se o caractere for uma letra maiúscula
- `any(...)` retorna `True` se **pelo menos um** caractere satisfizer a condição

---

### Passo 4 — Verificar número (Regra 3)

```python
if not any(c.isdigit() for c in senha):
    return False
```

- `.isdigit()` retorna `True` se o caractere for um dígito de `0` a `9`

---

### Passo 5 — Verificar caractere especial (Regra 4)

```python
especiais = set("!@#$%&*")
if not any(c in especiais for c in senha):
    return False
```

- `set("!@#$%&*")` cria um conjunto com os caracteres especiais permitidos
- `c in especiais` verifica se o caractere `c` está nesse conjunto
- Usar `set` é mais eficiente que verificar numa string, pois a busca em conjunto é O(1)

---

### Passo 6 — Retornar True

Se passou por todas as verificações sem retornar `False`, a senha é forte:

```python
return True
```

---

## ✅ Solução Completa

```python
def senha_forte(senha):
    """Implemente as cinco regras descritas no README."""

    # Regra 5: não pode ser None, vazia ou só espaços
    if senha is None or senha.strip() == "":
        return False

    # Regra 1: pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Regra 2: pelo menos uma letra maiúscula (A-Z)
    if not any(c.isupper() for c in senha):
        return False

    # Regra 3: pelo menos um número (0-9)
    if not any(c.isdigit() for c in senha):
        return False

    # Regra 4: pelo menos um caractere especial de !@#$%&*
    especiais = set("!@#$%&*")
    if not any(c in especiais for c in senha):
        return False

    return True
```

---

## 🧪 Casos de Teste Explicados

O arquivo `main()` testa sete casos. Entenda o que cada um valida:

```python
verificar("curta",        False, senha_forte("Ab1!"))          # só 4 chars → falha regra 1
verificar("sem maiuscula",False, senha_forte("senha123!"))      # nenhuma maiúscula → falha regra 2
verificar("sem numero",   False, senha_forte("SenhaForte!"))    # nenhum dígito → falha regra 3
verificar("sem especial", False, senha_forte("Senha1234"))      # nenhum especial → falha regra 4
verificar("valida",       True,  senha_forte("Senha@Forte2026"))# atende tudo → True
verificar("nula",         False, senha_forte(None))             # None → falha regra 5
verificar("vazia",        False, senha_forte(""))               # vazia → falha regra 5
```

> ⚠️ **Atenção:** O primeiro argumento de `verificar()` é apenas um rótulo para identificar o teste. O segundo é o valor **esperado**. O terceiro é o valor **retornado** pela sua função. O teste passa quando os dois coincidem.

---

## 🚫 Erros Comuns

### ❌ Verificar `None` depois de outras operações

```python
# ERRADO — vai gerar AttributeError se senha for None
if len(senha) < 8:
    return False
if senha is None:   # tarde demais!
    return False
```

### ❌ Esquecer o `not` no `any()`

```python
# ERRADO — retorna False quando EXISTE maiúscula (lógica invertida)
if any(c.isupper() for c in senha):
    return False
```

### ❌ Usar `==` com `None`

```python
# EVITE — o correto em Python é usar 'is'
if senha == None:   # funciona, mas não é idiomático
if senha is None:   # ✅ correto
```

---

## 💡 Conceitos Utilizados

| Conceito | Descrição |
|----------|-----------|
| **Função pura** | Não modifica variáveis externas; o resultado depende apenas da entrada |
| **Classes de equivalência** | Grupos de entradas com comportamento igual (ex: todas as senhas curtas falham pela mesma regra) |
| **`any()`** | Retorna `True` se pelo menos um elemento satisfizer a condição |
| **`set`** | Estrutura de dados para busca eficiente de pertencimento |
| **Guard clauses** | Retornos antecipados (`return False`) que simplificam a lógica |

---

## 📚 Referências

- [Documentação `str.isupper()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.isupper)
- [Documentação `str.isdigit()`](https://docs.python.org/pt-br/3/library/stdtypes.html#str.isdigit)
- [Documentação `any()`](https://docs.python.org/pt-br/3/library/functions.html#any)
- [Documentação `set`](https://docs.python.org/pt-br/3/library/stdtypes.html#set)