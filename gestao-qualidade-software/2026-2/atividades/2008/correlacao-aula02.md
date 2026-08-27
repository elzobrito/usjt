# Correlação — Atividade 2 × Aula 02 × GQ v2

## 1. Partes da atividade × momentos do plano

| Parte da atividade | Momento | Minutos no plano | Objetivo | Conteúdos | Competência |
|---|---|---|---|---|---|
| 0 Diagnóstico individual | mom-001 | 0–15 | obj-001 | con-001 | comp-001 |
| 1 Teste de erros | mom-002 (checagem) | 15–35 | obj-001 | con-001, con-002 | comp-001 |
| 2 Correspondência evidência → característica | mom-003 | 35–65 | obj-002 | con-003, con-004 | comp-001 |
| 3 Q1 classificação P/U/D/R | mom-004 início | 65–75 | obj-001 | con-002 | comp-001 |
| 3 Q2 diagnóstico | mom-004 | 75–95 | obj-002 | con-003, con-004 | comp-001, comp-002 |
| 3 Q3 requisito | mom-005 | 95–115 | obj-003 | con-005 | comp-001, comp-002 |
| 3 Q4 decisão | mom-005 | 115–130 | obj-004 | con-006 | comp-002 |
| 4 Revisão cruzada | mom-006 | 130–155 | obj-004 | con-005, con-006 | comp-002 |
| 5 Ticket de saída | mom-007 | 155–170 | obj-001, obj-004 | con-001, con-006 | comp-001, comp-002 |

## 2. Erros da aula que a atividade testa

| `erro_comum` do plano | Onde testa | Item esperado |
|---|---|---|
| Usar “o sistema funciona” como qualidade suficiente | Parte 1, afirmação 1; Parte 0 | Falso; pedir stakeholder e evidência |
| Ignorar legislação pública de acessibilidade em sítio de governo | Parte 1, afirmação 2; evidência 3 | Verdadeiro usar LBI/eMAG como critério; ISO só citada |
| Distribuir sintomas entre nomes decorados | Parte 2; Parte 3 Q2 | Predominante + justificativa no texto |
| Transformar indício em incidente confirmado | Parte 1, afirmação 4; evidência 4 | Não afirmar invasão a partir de um dado de login visível |
| Escolher número arbitrário / adjetivo sem limiar | Parte 3 Q3 | Molde com medida, unidade e janela |
| Propor solução antes de separar fato e inferência | Parte 3 Q2 proíbe voto e correção | Diagnóstico sem decisão |
| Tratar opinião da equipe como aceite formal | Parte 3 Q4; evidência 8 | Autoridade institucional |
| Maximizar tudo ou ignorar requisito legal / stakeholder vulnerável (con-006) | Evidência 3; Parte 3 Q4 | LBI/WCAG/NBR como fonte do limiar, sem parecer jurídico |

## 3. Evidências × grupos × característica predominante

| Evidência | Grupos | Predominante | Entra na Parte 2? |
|---|---|---|---|
| 1 vinte consultas de escolas | G1 | Adequação funcional | sim (a1) |
| 2 p95 14,2 s Totais de Alunos | G2, G9 | Eficiência de desempenho | sim (a2) |
| 3 menu Mapeamento / teclado | G3, G10 | Capacidade de interação | sim (a3) |
| 4 dado de login visível no navegador | G4, G11 | Segurança da informação | sim (a4) |
| 5 falha de rede | G5, G12 | Confiabilidade | sim (a5) |
| 6 estimativa 6 h | G6, G13 | Manutenibilidade | não — modelagem docente |
| 7 99,5% | G7 | Confiabilidade | não — modelagem docente |
| 8 4,6/5 da equipe | G8 | Qualidade em uso fraca | não — modelagem docente |

## 4. Itens GQ v2

| Arquivo | Subtipo | Construto da Aula 02 | Status de pipeline |
|---|---|---|---|
| `gq/01-verdadeiro-falso-erros.json` | verdadeiro_falso | erros de con-001 e con-002 | **approved** (`job_12500880606242b79714d24dfd19b639`, Elzo Brito, 2026-08-27) |
| `gq/02-correspondencia-evidencias.json` | correspondencia | con-003 classificação justificada | **approved** (`job_f2cd8eaba4a14508977f784d602b2cb9`, Elzo Brito, 2026-08-27) |
| `gq/03-estudo-caso-portal-horizonte.json` | estudo_caso | obj-001 a obj-004 em ordem | **approved** (`job_8814fb9e77a5408083552ee50d5edda8`, Elzo Brito, 2026-08-27) |

DEC-0051: a questão pronta é a que o docente aprovou. Elzo Brito aprovou os três itens em 2026-08-27 (`source=human`). Export em `gq/exports/`.

## 5. Cobertura dos quatro objetivos

| Objetivo | Verbo | Onde o aluno produz a evidência esperada do plano |
|---|---|---|
| obj-001 distinguir | distinguir produto/uso/dados/processo | Parte 1 + Parte 3 Q1 (P/U/D/R) + ticket |
| obj-002 analisar | fato, inferência, característica | Parte 2 + Parte 3 Q2 |
| obj-003 elaborar | requisito verificável | Parte 3 Q3 |
| obj-004 justificar | decisão + revisão | Parte 3 Q4 + Parte 4 |
