# Gabarito docente — Atividade 2 (não projetar)

O caso admite mais de uma decisão se evidência, contexto e risco forem preservados. Não aceite característica decorada. Distinga fato observável no BDGETEC de laboratório didático.

## Parte 1 — Teste de erros

Sequência: **F V V F** → alternativa **C**.

| # | Juízo | Por quê |
|---|---|---|
| 1 | F | A consulta concluída mostra adequação funcional naquele percurso, não qualidade suficiente para amanhã. |
| 2 | V | LBI e eMAG são textos públicos. Sítio de governo não perde o dever de acessibilidade porque o pedido omitiu o critério. Não é parecer jurídico. ISO permanece só citada, sem texto da norma. |
| 3 | V | O modelo organiza perguntas; não escolhe prioridade, métrica, limiar nem decisão institucional. |
| 4 | F | Dado de login visível no navegador é indício. O caso diz que o teste não confirmou uso da conta alheia nem exposição de dados. |

Erro que a Parte 1 testa: confundir função com qualidade; ignorar legislação pública de acessibilidade em sítio de governo; transformar indício em incidente.

## Parte 2 — Correspondência

Gabarito 1:1: **a1-b3, a2-b1, a3-b5, a4-b2, a5-b4** → alternativa **B**.

| Evidência | Predominante | Limite |
|---|---|---|
| a1 20/20 escolas | Adequação funcional | Não prova carga, teclado, sessão nem falha. |
| a2 p95 Totais de Alunos | Eficiência de desempenho | Laboratório; falta carga-alvo, ambiente, janela e limiar. |
| a3 Mapeamento/`onmouseover` | Capacidade de interação | Amostra pequena; o padrão de menu é observável; bloqueio de tarefa pede contenção. LBI/eMAG cabem porque é sítio de governo. |
| a4 dado de login visível | Segurança da informação | Indício, não invasão confirmada. Não mexer no login em produção. |
| a5 falha de rede | Confiabilidade | Laboratório; separar mensagem, estado no servidor, idempotência. |

Evidências 6, 7 e 8 não entram nesta tabela: você as modela em voz alta e os grupos G6–G8 / G13 as usam na Parte 3.

| Evidência | Predominante | Limite |
|---|---|---|
| 6 estimativa de 6 h | Manutenibilidade | Estimativa não é medida; o histórico pede evidência. |
| 7 99,5% | Confiabilidade | Número incompleto sem janela, fonte, exclusões e histórico. |
| 8 4,6/5 da equipe | Evidência fraca de qualidade em uso | Amostra enviesada; stakeholder inadequado. |

## Parte 3 — Estudo de caso

### Questão 1

Sequência: **P U D R**.

| # | Letra | Por quê |
|---|---|---|
| 1 | **P** | A consulta que conclui é o sítio funcionando (produto). Não prova que os totais estão certos. |
| 2 | **U** | Pessoa + tarefa: quem só usa teclado não chega a Escolas. LBI/eMAG podem justificar, sem parecer. |
| 3 | **D** | O relatório inconsistente é o conteúdo publicado, não só o botão. |
| 4 | **R** | Estimativa e regressão são modo de construir/corrigir (processo), ponte para a Aula 03. |

### Questões 2–4

Use o quadro de predominância acima. Recuse:

- voto de aceitação na questão 2;
- “o BDGETEC deve ser rápido/fácil/seguro/acessível” sem limiar;
- invasão confirmada a partir só da evidência 4;
- 2011 como modelo atual;
- tratar acessibilidade da evidência 3 como detalhe negociável só por causa do prazo, ou transformar a ficha em parecer jurídico;
- load test ou exploração do sítio em produção.

Exemplo didático de transformação (não é limiar universal nem medição oficial):

Vago: “O BDGETEC deve ser rápido.”

Verificável: “Durante a publicação do novo período, para consultas de Totais de Alunos com até 600 sessões simultâneas no ambiente de referência documentado, 95% das respostas deverão ser concluídas em até 3 segundos, medidos no servidor durante 30 minutos sem excluir erros.”

Segundo exemplo (evidência 3): “Para cidadão que navega só por teclado, na página inicial pública, o menu Mapeamento e o destino Escolas deverão ser localizados, abertos e usados sem mouse em 100% das tentativas do roteiro de homologação, antes da publicação do novo período.” Fonte do limiar: obrigação de sítio governamental (LBI/eMAG/WCAG 2.2).

### Níveis

- **Iniciante:** nomeia característica, mistura sintoma e medida ou usa adjetivo sem limiar.
- **Adequado:** liga evidência, stakeholder, contexto, característica, requisito, medida e decisão; declara um limite; distingue sítio público de laboratório.
- **Avançado:** compara riscos, separa fato de inferência e diz que evidência mudaria a decisão.

## Parte 4

O revisor que reescreve a ficha falhou no papel. Basta uma pergunta concreta.

## Parte 5

Esperado: substituir o sim/não da abertura por cadeia característica–requisito–medida–evidência–decisão, e reconhecer que processo sustenta repetir a evidência.
