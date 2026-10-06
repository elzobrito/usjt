# 10/09 — Classes de equivalência e valores-limite em Python

Três exercícios que treinam a mesma ideia: **primeiro** dividir as entradas em classes e achar as fronteiras no caderno, **depois** escrever ou rodar o código. Todos usam o mesmo mini "harness" de testes (`harness.py`): cada caso imprime `✅ PASSOU` ou `❌ FALHOU`, e o programa termina com código **0** (tudo passou) ou **1** (algo falhou).

Precisa só do Python 3, sem bibliotecas extras.

## Arquivos

| Arquivo | Exercício | O que é |
|---|---|---|
| `harness.py` | todos | Funções `verificar(nome, esperado, obtido)` e `codigo_saida(resultados)`. **Não modifique** |
| [execicio.md](execicio.md) | 1 | Validador de senha forte: as cinco regras, passo a passo, solução comentada e erros comuns |
| `senha.py` | 1 | Implementação de `senha_forte(senha)` com 7 casos de teste (todos passam) |
| [Enunciado.md](Enunciado.md) | 2 | Classificador de notas: regras, questões de caderno (classes, fronteiras, pseudocódigo) e desafio com `True` |
| `Template exercicio2.py` | 2 | Modelo para você implementar `classificar_nota(nota)`. Vem vazio: os 10 testes falham até você escrever a função |
| [execicio3.md](execicio3.md) | 3 | Escrevendo testes para `ContaBancaria`: regras de `depositar`, `sacar` e `transferir`, questões de caderno e critérios de avaliação |
| [guia para o 3.md](guia%20para%20o%203.md) | 3 | Guia didático do exercício 3: classe, método, exceção, `lambda`, `capturar()`, isolamento de testes e checklist |
| `conta.py` | 3 | Classe `ContaBancaria` pronta. **Não modifique** |
| `teste_conta.py` | 3 | Modelo onde **você escreve os testes**: cada `TODO` indica um caso a implementar |

## Como executar

Entre na pasta (os scripts importam `harness.py` e `conta.py` da mesma pasta):

```bash
cd gestao-qualidade-software/2026-2/atividades/1009
```

**Exercício 1 — senha forte**

```bash
python senha.py
```

**Exercício 2 — classificador de notas**

O enunciado manda abrir `exercicio2.py`. Faça uma cópia do modelo com esse nome e trabalhe nela:

```bash
cp "Template exercicio2.py" exercicio2.py      # Windows: copy "Template exercicio2.py" exercicio2.py
python exercicio2.py
```

**Exercício 3 — testes da ContaBancaria**

O enunciado chama o arquivo de `test_conta.py`; aqui ele se chama `teste_conta.py`.

```bash
python teste_conta.py
```

Enquanto nenhum `TODO` for preenchido, a saída termina em `0/0 testes passaram`. A meta do enunciado é ter pelo menos 3 testes por método (9 no total), cobrindo casos válidos e inválidos, cada um com a sua própria conta.

> Se aparecer `SyntaxError` logo na linha 1 de `teste_conta.py`, confira se a docstring começa com **três** aspas (`"""`).

## Ordem sugerida

1. Exercício 1: leia `execicio.md` e rode `senha.py` para ver o harness funcionando.
2. Exercício 2: responda o caderno do `Enunciado.md` e implemente `classificar_nota`.
3. Exercício 3: leia o `guia para o 3.md`, responda o caderno do `execicio3.md` e escreva os testes em `teste_conta.py`.
