# Planejamento docente — Aula 02 GQS (atividades de caderno)

Pacote PCA: `artifacts/aula-02-qualidade-produto/20260826T155547Z/` (produto da aula: BDGETEC)  
Enunciado do aluno: `atividade-02-portal-horizonte.md`  
Gabarito: `gabarito-atividade-02.md` (não projetar)  
Correlação: `correlacao-aula02.md`

## Relógio = sete momentos do plano

| Minuto | Momento do plano | O que acontece | Superfície |
|---|---|---|---|
| 0–15 | mom-001 abertura | Parte 0, individual | Caderno + uma frase no quadro |
| 15–35 | mom-002 teorização | SQuaRE no quadro + Parte 1 (teste de erros) | Quadro, depois caderno |
| 35–65 | mom-003 demonstração | Parte 2 (correspondência) e duas evidências modeladas por você (6 e 8, ou 6 e 7) | Caderno + voz alta |
| 65–95 | mom-004 prática | Parte 3, questões 1 e 2 — diagnóstico, sem correção e sem voto | Grupo, caderno |
| 95–130 | mom-005 aplicação | Parte 3, questões 3 e 4 — requisito e decisão | Grupo, caderno |
| 130–155 | mom-006 consolidação | Parte 4 — troca de caderno | Grupo |
| 155–170 | mom-007 fechamento | Parte 5 — ticket e ponte para processos | Individual |

Não comece pela decisão de liberar. Isso quebraria o `erro_comum` do plano: propor solução antes de separar fato e inferência.

## Produto da aula: BDGETEC

Endereço: https://bdcgetec.cps.sp.gov.br  
Banco de Dados da CGETEC, Centro Paula Souza. Capa: mapeamento de Etecs, vestibulinho, matrículas iniciais, totais de alunos; login de operação.

Abertura: duas frases sobre o que o sítio **é**, depois só a pergunta “uma consulta de escolas foi concluída; o BDGETEC tem qualidade?”.

Não load-testar produção. Números de carga/falha/enquete = laboratório.

## Exemplo âncora (evidência 3, ~2 min no mom-003)

Cartão no pacote: `release/materiais/exemplo_legislacao_acessibilidade.md`.

Frase no quadro: “O pedido de software pode ter esquecido. A LBI não esqueceu. O BDGETEC é sítio de governo. O menu Mapeamento que só abre com o mouse já impede chamar a consulta pública de funciona.”

Cadeia: capacidade de interação → cidadão sem mouse + CGETEC → LBI arts. 55 e 63 / eMAG / WCAG 2.2 → requisito verificável → trade-off não apaga obrigação de sítio de governo.

Não projetar artigos. Não pedir parecer. Grupos G3 e G10 podem usar isso na prioridade da Parte 3.

## Quadro no bloco 15–35

Quatro cartões: produto / uso / dados / processo.

Linha do tempo (só citar, sem distribuir texto de norma): ISO/IEC 9126 (histórico) → 25010:2011 (histórico) → 25010:2023 (produto vigente) + 25019:2023 (uso) + 25012:2008 (dados).

Nove nomes, sem subcaracterísticas: adequação funcional; eficiência de desempenho; compatibilidade; capacidade de interação; confiabilidade; segurança da informação; manutenibilidade; flexibilidade; safety / segurança operacional.

Frase de limite: o modelo organiza perguntas; não escolhe limiar nem a decisão institucional.

Na atividade, a turma **não usa** texto de ISO. Pode **usar** legislação pública de acessibilidade: Lei nº 13.146/2015 (LBI) e eMAG.

## Grupos e evidências da Parte 3

| Grupo | Evidência |
|---|---|
| G1 | 1 |
| G2 | 2 |
| G3 | 3 |
| G4 | 4 |
| G5 | 5 |
| G6 | 6 |
| G7 | 7 |
| G8 | 8 |
| G9 | 2 |
| G10 | 3 |
| G11 | 4 |
| G12 | 5 |
| G13 | 6 |

Formar 10 quartetos e 3 trios no início da Parte 2 ou 3. Sem lista nominal no material.

## Troca da Parte 4

| Circuito | Quem revisa quem |
|---|---|
| Dupla | G1 ↔ G2 |
| Dupla | G3 ↔ G4 |
| Dupla | G5 ↔ G6 |
| Dupla | G7 ↔ G8 |
| Dupla | G9 ↔ G10 |
| Triângulo | G11 → G12 → G13 → G11 |

Nenhum grupo revisa a mesma evidência que escreveu.

## Amostra no plenário

No máximo dois ou três grupos, evidências diferentes (sugestão: G2, G4, G5). Cada um lê requisito + decisão + um limite. Não passar os 13. Não projetar gabarito.

## Itens GQ v2 (fonte do enunciado)

Aprovados por Elzo Brito em 2026-08-27 (`source=human`; DEC-0051).

| Parte | Subtipo | Arquivo |
|---|---|---|
| 1 | `generico.objetiva.verdadeiro_falso` | `gq/01-verdadeiro-falso-erros.json` |
| 2 | `generico.objetiva.correspondencia` | `gq/02-correspondencia-evidencias.json` |
| 3 | `generico.discursiva.estudo_caso` | `gq/03-estudo-caso-portal-horizonte.json` |
