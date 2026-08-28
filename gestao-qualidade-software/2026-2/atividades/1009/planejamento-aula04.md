# Planejamento docente — Aula 04 GQS

**Pacote PCA:** `../../../artifacts/aula-04-revisao-codigo/20260828T181834Z/`  
**Fonte principal:** Bartié, seções 3.2.1–3.2.5 e capítulos 8–11  
**Estado:** draft; alinhamento institucional proposto  
**Data:** 10/09/2026  
**Duração:** 200 minutos

## Decisão da aula

A turma primeiro verifica estaticamente o artefato e registra cinco hipóteses. Depois valida dinamicamente os cinco casos, comparando esperado e obtido. PASS vale somente para o caso executado; FAIL mostra divergência, mas não substitui o diagnóstico. As funções permanecem defeituosas para a futura aula de TDD.

## Relógio

| Minuto | Momento | Evidência principal |
|---|---|---|
| 0–10 | Onde mora o FAIL? | hipótese inicial sobre o alcance da saída |
| 10–25 | Bartié: verificar antes de executar | distinção artefato/revisão e executável/validação |
| 25–40 | Um critério, uma linha e uma hipótese | linha-modelo da revisão estática |
| 40–90 | Revisão estática das cinco funções | tabela com requisito, fragmento, suspeita e efeito |
| 90–110 | Validação dinâmica | tabela com entrada, esperado, obtido e PASS/FAIL |
| 110–120 | Oráculo independente de `contar` | `contar("XXX", "2026/2")`, esperado zero |
| 120–140 | Intervalo | pausa sem conteúdo ou correção das funções |
| 140–180 | Recuperação e conferência cruzada | tabelas revisadas e código preservado |
| 180–195 | Ticket individual | diferença entre verificação e validação; limite de PASS |
| 195–200 | Encerramento | ponte para níveis de teste da Aula 05 |

A condução detalhada está em `fala_docente_completa.md`. O gabarito em `docente.md` não deve ser projetado durante a primeira passagem.
