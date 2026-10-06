# Gestão da qualidade de software — 2026-2

Material de sala da UC **0006960**, turma de referência CCP1AN-MCC2 (quinta-feira).

| Arquivo | Para que serve |
|---|---|
| [cronograma.md](cronograma.md) | Cronograma oficial da oferta: datas, aulas, A1, A3, TechWeek e Expo |
| [restricoes-turma.md](restricoes-turma.md) | Como a turma testa (oráculo `PASS`/`FAIL`, saída 0 ou 1, na linguagem que a máquina tiver) e o que é proibido no produto real BDGETEC |

A partir da Aula 03, o teste de sala é um **oráculo**: um programa que imprime `PASS` ou `FAIL` e termina com código de saída **0** (tudo certo) ou **1** (algo falhou). JUnit, pytest e Jest não são exigidos.

## Aulas (`atividades/`)

Cada pasta tem o **dia e o mês** da aula (`0309` = 03/09).

| Pasta | Tema | Precisa de computador? |
|---|---|---|
| [atividades/2008](atividades/2008/) | Aula 01 (20/08): por que qualidade importa. Aula 02 (27/08): da característica à evidência, com o BDGETEC | Não (caderno). O `main.java` é só para leitura |
| [atividades/2708](atividades/2708/) | Questões de caderno da Aula 02 e links do livro | Não |
| [atividades/0309](atividades/0309/) | Laboratório de testes: sistema de desconto em Java | Sim (JDK) |
| [atividades/1009](atividades/1009/) | Classes de equivalência e valores-limite em Python: senha, notas e conta bancária | Sim (Python 3) |
| [atividades/2409](atividades/2409/) | Plano de teste e métricas de qualidade do MD Studio v0.2.2 | Sim (MD Studio) |

Na raiz de `atividades/` também estão:

| Arquivo | O que é |
|---|---|
| `teste.md` | Versão completa do plano de teste do MD Studio (a de `2409/` é a resumida), com o caso TC-04 "HardTest" passo a passo e o modelo de registro de achado `QA-MET` |
| `notas.md` | Massa de dados do TC-04: um `notas.md` com Markdown, GFM, KaTeX e Mermaid para abrir no MD Studio |

---

### 2008 — Aulas 01 e 02

Aula 01 (20/08):

| Arquivo | O que é |
|---|---|
| `atividade1.md` | "Você autorizaria o lançamento?": decisão em grupo sobre um foguete, em 10 minutos |
| `atividade3.md` | "O bug custa R$ 100 ou R$ 1 milhão?": orçamento de qualidade e custo do defeito |
| `busca_defeito_java.md` + `main.java` | Caça aos defeitos: o código (classe `ConsultaEscolas`) **não compila de propósito**. Leia e encontre erros de compilação, de execução e de lógica |
| `codigo.html` | Tela "Consulta de escolas" com defeitos de HTML/CSS para inspecionar |
| `Garantia da Qualidade de Software - Aula 01.pptx` | Slides da aula (só na cópia local e no Drive; não vai para o GitHub) |

Aula 02 (27/08), produto analisado: [BDGETEC](https://bdcgetec.cps.sp.gov.br):

| Arquivo | O que é |
|---|---|
| `atividade-02-portal-horizonte.md` | Enunciado da Atividade 2, Partes 0 a 5 (diagnóstico, teste de erros, correspondência, estudo de caso, revisão cruzada e ticket de saída) |
| `planejamento-aula02.md`, `correlacao-aula02.md`, `gabarito-atividade-02.md` | Material do professor |
| `gq/` | Itens das três partes em JSON (`01`, `02`, `03`), as cópias exportadas em `gq/exports/` (JSON e Markdown) e os registros `JOBS.md` e `VALIDACAO.md` |

Regra do produto real: não faça teste de carga, não tente senhas e não mexa no login do BDGETEC.

### 2708 — Aula 02, questões de caderno

| Arquivo | O que é |
|---|---|
| `questoes.md` | Questões da Aula 02 (Partes 0 a 3) e a atividade "Qualidade e zero-defeito" (a calculadora testada só com 2 + 2) |
| `livro.md` | Dois links do Drive para o livro |

### 0309 — Laboratório de testes: sistema de desconto

Veja o [README da pasta](atividades/0309/README.md).

### 1009 — Classes de equivalência em Python

Veja o [README da pasta](atividades/1009/README.md).

### 2409 — Testes e métricas do MD Studio

| Arquivo | O que é |
|---|---|
| `testes.md` | Linha de base do MD Studio v0.2.2 (requisitos, fora de escopo, divergências conhecidas entre documentação e código), matriz de métricas de qualidade e as trilhas de teste TC-01 a TC-04 |

Use o `notas.md` da pasta `atividades/` como arquivo de teste e a versão completa em `atividades/teste.md` para o TC-04.
