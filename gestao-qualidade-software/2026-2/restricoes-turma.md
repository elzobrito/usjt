# Restrições da turma CCP1AN-MCC2 (GQS 2026-2)

**UC:** Gestão da Qualidade de Software (0006960)  
**Turma:** CCP1AN-MCC2-91149740 — noturno, 49 estudantes  
**Docente:** Elzo Brito  
**Decisão de teste:** spec 2026-08-28 (revoga DEC-0052). Protocolo único; Java, JavaScript ou Python conforme a máquina. Sem JUnit/pytest/Jest como requisito de sala.

## Linguagem dos testes

A partir da **Aula 03 (03/09)**, o teste da sala é um **oráculo** `PASS`/`FAIL` (saída 0 ou 1), na língua que a máquina tiver.

- Esqueletos: `atividades/0309/oraculo.py`, `oraculo.js`, `Oraculo.java`.
- JUnit, pytest e Jest não são requisito. Podem aparecer como ponte de 10 min.
- A Aula 02 (27/08) foi papel e caneta.
- O “caça aos defeitos” em `atividades/2008/main.java` continua válido como inspeção.
- A fatia Maven em `atividades/java-testes/` é produto sob teste / material de casa, não material da Aula 03.

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
