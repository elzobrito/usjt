# Restrições da turma CCP1AN-MCC2 (GQS 2026-2)

**UC:** Gestão da Qualidade de Software (0006960)  
**Turma:** CCP1AN-MCC2-91149740 — noturno, 49 estudantes  
**Docente:** Elzo Brito  
**Decisão:** Conversation ESAA DEC-0052 (2026-08-27)

## Linguagem dos testes

A partir das **aulas seguintes à Aula 02**, testes automatizados são em **Java + JUnit 5**.

- Não usar Python, pytest, JavaScript ou Playwright como linguagem da turma.
- A Aula 02 (27/08) permanece **papel e caneta**; não exige notebook nem compilador.
- O “caça aos defeitos” em `atividades/2008/main.java` continua válido como inspeção. Os testes automatizados ficam em `atividades/java-testes/`.

## Produto e limites

- Produto da disciplina: BDGETEC — https://bdcgetec.cps.sp.gov.br
- Os testes Java exercitam uma **fatia didática** (consulta de escolas), não o sítio em produção.
- **Proibido:** HTTP, load test, tentativa de senha ou exploração do login no sítio real.

## O que a turma pode abrir

- **ISO / SQuaRE:** só citar o nome no quadro. Não distribuir nem abrir o texto da norma.
- **LBI (Lei nº 13.146/2015) e eMAG:** material de trabalho para critério de acessibilidade de sítio de governo.

## O que JUnit não substitui

Teste unitário mede **produto** (P). Não mede sozinho:

- **Uso (U):** menu Mapeamento só com teclado, LBI art. 63 / eMAG.
- **Dados (D):** relatório inconsistente no servidor — só se o código didático modelar isso.
- **Processo (R):** quem escreve, revisa e reexecuta o teste no próximo período.

Compilar e passar no JUnit **não** prova qualidade suficiente para o novo período.
