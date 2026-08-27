# Validação GQ v2 — itens da Aula 02

Runtime: `/home/elzobrito/desenvolvimento/GPT/projetos/gerador de questões/v2`  
Modo: agente redigiu o JSON; `GenerationService` + `FakeProvider` (sem LLM, sem `gq api serve`, DEC-0051).  

## Versão em sala (BDGETEC)

Produto: **BDGETEC** (`https://bdcgetec.cps.sp.gov.br`).  
Aprovação pedagógica da substituição: **Elzo Brito**, 2026-08-27, pedido explícito na sessão Grok.  
Task ESAA: `USJT-GQS-AULA02-BDGETEC-001`

| Item | subtype_key | Arquivo de sala | gabarito |
|---|---|---|---|
| 01-verdadeiro-falso-erros.json | generico.objetiva.verdadeiro_falso | `gq/01-verdadeiro-falso-erros.json` | **C** (F V V F) |
| 02-correspondencia-evidencias.json | generico.objetiva.correspondencia | `gq/02-correspondencia-evidencias.json` | **B** |
| 03-estudo-caso-portal-horizonte.json | generico.discursiva.estudo_caso | `gq/03-estudo-caso-portal-horizonte.json` | ordem diagnóstico → requisito → decisão |

A Parte 1 objetiva passou a **C** (F V V F) em 2026-08-27: afirmação 2 usa LBI/eMAG; ISO só citada. Correspondência permanece **B**.

Cópias de trabalho em `gq/exports/` (JSON da sala + Markdown). Os jobs sqlite abaixo permanecem como **snapshot histórico** da versão Portal Horizonte; não reabrir a tarefa done `USJT-GQS-AULA02-ATIVIDADES-APROVAR-001`.

## Snapshot histórico (Portal Horizonte, jobs approved)

Aprovação original: Elzo Brito, 2026-08-27, `source=human`, task `USJT-GQS-AULA02-ATIVIDADES-APROVAR-001`.

| Item (versão antiga) | job_id | review_id | status |
|---|---|---|---|
| VF Portal Horizonte | `job_12500880606242b79714d24dfd19b639` | `rev_9fcd2c39d2b24bc2827770c069763446` | approved (histórico) |
| Correspondência Portal Horizonte | `job_f2cd8eaba4a14508977f784d602b2cb9` | `rev_d5fe1f335fd8492eb566979f19ae301a` | approved (histórico) |
| Estudo de caso Portal Horizonte | `job_8814fb9e77a5408083552ee50d5edda8` | `rev_fd210287536242428ae2f28efed0b541` | approved (histórico) |

A questão pronta **desta aula** é a versão BDGETEC nos JSON da pasta `gq/`, pedida pelo docente. Pacote PCA `artifacts/aula-02-qualidade-produto/20260826T155547Z` foi atualizado na mesma task.
