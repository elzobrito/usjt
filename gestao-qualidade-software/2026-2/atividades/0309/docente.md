# Aula 03 — Folha docente

**Clímax:** a consulta “funcionou” e o oráculo do caso **2026/2** imprime `FAIL`. Isso é evidência de **produto**. Quem guarda e reexecuta o oráculo é **processo**. O script **não** mede **uso** (LBI/teclado).

**Oráculo esperado:** `FAIL` e saída `1`. A função só devolve escolas em `2026/1`. **Não deixar a turma “consertar” hoje** — isso é a Aula 07 (TDD).

**Ponte da Aula 02:** o ticket “qual processo produz essa evidência de novo?” vira o arquivo que acabaram de rodar.

## Relógio

| Min | O quê |
|---|---|
| 0–10 | Pergunta no quadro. Sem ementa. Sem ISO. |
| 10–15 | `java -version` · `python3 --version` · `node -version`. Quem não tiver, papel. Sem instalar. |
| 15–35 | Protocolo no quadro (dado → ação → oráculo → PASS/FAIL). Turma preenche a tabela **antes** de rodar. |
| 35–75 | Rodam **um** arquivo. Você lê o terminal: uma linha e 0/1. Não depura três stacks. |
| 75–100 | Tabela P / R / U. Gabarito: 1=P, 2=R, 3=U. Frase: `PASS` de produto ≠ qualidade de uso. |
| 100–120 | Ticket. Recolher ou foto. Anunciar: Aula 04 = revisão neste código; A3 = este oráculo é peça 1. |
| resto | Margem. Se atrasar, corte a ponte de 10 min sobre JUnit/pytest/Jest. |

## Dois erros comuns

1. Trocar o oráculo para `2026/1` “para passar”. Isso destrói a evidência.  
2. Tratar `FAIL` como setup quebrado. É o ponto da aula.

## O que cortar se atrasar

1. Ponte “framework = mesmo oráculo com runner”.  
2. Segunda língua no projetor.  
3. Discussão longa de LBI — uma frase basta: o script não abre o sítio.

## Bartie (máx. 5 min, depois que o `FAIL` existir)

> É mais fácil provar que “algo funciona” do que provar que “algo não funciona”.

Ligação: o desenvolvedor prova que “voltaram três escolas”. O oráculo pergunta se o **período do caso** está no produto. Fonte: `bartie-trecho.md`.

## Gabarito da classificação

| # | Letra | Por quê |
|---|---|---|
| 1 | P | O programa, no período 2026/2, não satisfaz o oráculo. |
| 2 | R | Hábito de quem escreve, guarda e reexecuta. |
| 3 | U | Teclado / LBI. Este arquivo não mede isso. |

ISO/SQuaRE: só o nome, se alguém perguntar. Sem texto de norma.
