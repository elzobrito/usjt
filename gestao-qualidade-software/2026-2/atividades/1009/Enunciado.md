# Exercício 2 — Classificador de Notas

## 📋 Descrição

Implemente a função `classificar_nota(nota)` que recebe uma nota e retorna
uma string indicando a situação do aluno.

---

## 📐 Regras

| Condição | Retorno |
|---|---|
| `nota` é `None` | `"invalido"` |
| `nota` não é número (`str`, `list`, etc.) | `"invalido"` |
| `nota` < 0 ou `nota` > 10 | `"invalido"` |
| 0 ≤ `nota` < 5 | `"reprovado"` |
| 5 ≤ `nota` < 7 | `"recuperacao"` |
| 7 ≤ `nota` ≤ 10 | `"aprovado"` |

---

## ✏️ PARTE 1 — Caderno (faça antes de abrir o computador!)

Responda no caderno **antes** de escrever qualquer código.

### Questão 1 — Classes de Equivalência

Preencha a tabela identificando as classes de equivalência do problema:

| # | Nome da Classe | Intervalo / Condição | Resultado Esperado |
|---|---|---|---|
| C1 | | | |
| C2 | | | |
| C3 | | | |
| C4 | | | |
| C5 | | | |

> 💡 Dica: quantas saídas diferentes a função pode ter? Cada saída é (pelo menos) uma classe.

---

### Questão 2 — Casos de Teste

Para cada classe de equivalência que você identificou, escolha **um valor representativo** e preencha:

| Caso | Entrada | Saída Esperada | Classe que representa |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

### Questão 3 — Valores de Fronteira

As **fronteiras** são os pontos onde o comportamento da função muda.
Identifique pelo menos 4 valores de fronteira e o que acontece em cada um:

| Valor de Fronteira | Resultado |
|---|---|
| | |
| | |
| | |
| | |

---

### Questão 4 — Pseudocódigo

Escreva no caderno o pseudocódigo da função antes de implementá-la:

```
função classificar_nota(nota):
    se nota é _______ ou não é _______:
        retorne "_______"
    se nota < _____ ou nota > _____:
        retorne "_______"
    se nota < _____:
        retorne "_______"
    se nota < _____:
        retorne "_______"
    retorne "_______"
```

---

## 💻 PARTE 2 — Computador

Após responder as questões do caderno, abra o arquivo `exercicio2.py`
e implemente a função `classificar_nota(nota)`.

### Como rodar

```bash
python exercicio2.py
```

### Resultado esperado ao terminar corretamente

```
  ✅ PASSOU: nula
  ✅ PASSOU: texto
  ✅ PASSOU: negativa
  ✅ PASSOU: acima do maximo
  ✅ PASSOU: reprovado minimo
  ✅ PASSOU: reprovado maximo
  ✅ PASSOU: recuperacao minimo
  ✅ PASSOU: recuperacao maximo
  ✅ PASSOU: aprovado minimo
  ✅ PASSOU: aprovado maximo
```

---

## 🔍 Dicas

- Use `isinstance(nota, (int, float))` para verificar se é número
- Cuide da **ordem das verificações**: trate os casos inválidos primeiro
- Lembre-se: `bool` em Python é subclasse de `int` — `isinstance(True, int)` retorna `True`!
  Isso pode ser um problema. Como resolver?

---

## 🎯 Desafio Extra (opcional)

Adicione mais um caso de teste para o valor `True` (booleano).
Qual deveria ser o retorno? Justifique sua resposta no caderno.