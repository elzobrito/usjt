# Aula 04 — Verificar antes de validar

**UC:** Gestão e qualidade de software (0006960)  
**Data:** 10/09/2026  
**Produto:** uma fatia local da consulta de escolas, sem HTTP e sem dados reais

Hoje você não vai corrigir `buscar`, `contar`, `listar` ou `ativas`. Primeiro vai preservar evidência: examinar o artefato, prever efeitos e depois executar casos controlados.

## 1. Quatro palavras de trabalho

- **Defeito:** problema existente em um artefato, como requisito, documento ou código.
- **Verificação estática:** exame do artefato com critério, sem precisar executá-lo.
- **Validação dinâmica:** execução do produto e comparação entre resultado esperado e obtido.
- **Evidência:** registro que sustenta uma conclusão limitada; PASS ou FAIL não explica tudo sozinho.

## 2. Pedido da consulta

- `buscar("NRA1", "2026/2")` deve devolver as três escolas da regional.
- `NRA1`, `nra1` e ` NRA1 ` representam a mesma regional.
- Uma regional inexistente, como `XXX`, deve possuir zero escolas.
- `listar("NRA1")` deve produzir três linhas sem acessar posição inexistente.
- `ativas("XXX", "2026/2")` deve devolver lista vazia.

## 3. Primeira passagem — revisão estática

Não execute ainda. Abra uma única linguagem e use o pedido como checklist.

| Tópico | Critério ou requisito | Fragmento observado | Defeito suspeito | Efeito previsto |
|---|---|---|---|---|
| `buscar` e período | | | | |
| `contar` e regional inexistente | | | | |
| `listar` e limite do laço | | | | |
| normalização da regional | | | | |
| `ativas` e filtragem | | | | |

Uma linha com apenas “está errado” não é evidência. Indique o fragmento e explique a ligação com o critério.

## 4. Segunda passagem — validação dinâmica

Escreva o esperado antes de executar.

| Caso | Entrada | Esperado | Obtido | PASS/FAIL |
|---|---|---|---|---|
| `buscar` | `NRA1`, `2026/2` | 3 escolas | | |
| `contar` | `XXX`, `2026/2` | 0 | | |
| `listar` | `NRA1` | 3 linhas, sem exceção | | |
| normalização | `nra1` e ` NRA1 `, `2026/1` | igual a `NRA1` | | |
| `ativas` | `XXX`, `2026/2` | lista vazia | | |

O período `2026/1` no caso de normalização serve somente para isolar a regional enquanto o defeito de período continua presente.

## 5. Comandos — execute um por vez

### Python

```text
python3 consulta.py buscar
python3 consulta.py contar
python3 consulta.py listar
python3 consulta.py regional
python3 consulta.py ativas
```

### JavaScript

```text
node consulta.js buscar
node consulta.js contar
node consulta.js listar
node consulta.js regional
node consulta.js ativas
```

### Java

```text
javac Consulta.java
java Consulta buscar
java Consulta contar
java Consulta listar
java Consulta regional
java Consulta ativas
```

## 6. Clímax — oráculo independente de `contar`

Complete no caderno ou em `oraculo_contar` / `oraculoContar`:

```text
obtido = contar("XXX", "2026/2")
esperado = 0
PASS se obtido for igual ao esperado; caso contrário, FAIL
```

Não use `len(buscar(...))`, `.length` ou `.size()` como única fonte do esperado. Duas funções defeituosas podem concordar e produzir um falso PASS.

## 7. Ticket individual

1. Usando esta aula, explique a diferença entre verificação estática e validação dinâmica.
2. Por que um PASS não prova que o produto não possui defeitos?

Entregue as duas tabelas e o ticket. Mantenha o código defeituoso para a futura aula de TDD.
