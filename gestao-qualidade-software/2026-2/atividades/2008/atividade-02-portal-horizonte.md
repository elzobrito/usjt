# Atividade 2 — BDGETEC: da característica à evidência

**UC:** Garantia da Qualidade de Software  
**Aula:** 02 — Qualidade de produto  
**Turma:** CCP1AN-MCC2-91149740, noturno, 49 estudantes  
**Duração:** 170 minutos (mesmo relógio do plano da aula)  
**Formato:** caderno, papel e caneta; sem notebook do aluno  
**Organização:** individual na Parte 0 e na Parte 1; depois 10 quartetos e 3 trios (G1–G13)

Esta atividade **é** a Aula 02. A ordem abaixo é a do plano: diagnóstico antes da solução; requisito antes da decisão; revisão depois da decisão.

**Produto:** [https://bdcgetec.cps.sp.gov.br](https://bdcgetec.cps.sp.gov.br) — Banco de Dados da CGETEC, Centro Paula Souza.  
Não load-teste, não tente senhas e não mexa no login em produção.

---

## Parte 0 — Diagnóstico individual (minutos 0–15)

O professor mostra o endereço e diz o que o sítio faz. No quadro fica só isto:

> Uma consulta de escolas foi concluída com sucesso. O BDGETEC tem qualidade?

No caderno, em silêncio, registre:

1. decisão: sim / não / não sei;
2. duas razões;
3. uma informação que falta.

Não leia o caso ainda.

---

## Parte 1 — Teste de erros (minutos 15–35)

Depois da linha do tempo SQuaRE no quadro, julgue cada afirmação **V** ou **F**. Depois escolha a sequência A–E.

1. Concluir uma consulta de escolas com período válido no ambiente de teste prova que o BDGETEC tem qualidade suficiente para o novo período no dia seguinte.
2. Como o BDGETEC é sítio de governo, a Lei Brasileira de Inclusão (Lei nº 13.146/2015) e o eMAG podem ser usados nesta aula como fonte de critério de acessibilidade, mesmo que o pedido de software não mencione isso.
3. A família SQuaRE organiza perguntas sobre produto, uso e dados, mas o modelo não escolhe automaticamente prioridade, métrica, limiar nem a decisão institucional.
4. Ver no navegador um dado de login do BDGETEC autoriza afirmar, sem investigação adicional, que houve invasão confirmada e vazamento de dados pessoais.

| | 1 | 2 | 3 | 4 | Sequência |
|---|---|---|---|---|---|
| Sua marca | V/F | V/F | V/F | V/F | A B C D E |

A) V F V F  B) F F V F  C) F V V F  D) F F F V  E) V F F F

---

## Parte 2 — Tabela de correspondência (minutos 35–65)

Associe cada evidência à característica **predominante**. Use só os nomes de alto nível. Uma evidência pode atravessar outras características: a predominante precisa caber no texto.

| Evidência (A) | Característica (B) |
|---|---|
| a1. Vinte consultas de escolas concluídas no ambiente de teste | b1. Eficiência de desempenho |
| a2. Percentil 95 sobe de 1,8 s para 14,2 s com 600 sessões em Totais de Alunos | b2. Segurança da informação |
| a3. Três pessoas só com teclado não abrem o menu Mapeamento (só `onmouseover`) | b3. Adequação funcional |
| a4. Dado de login do BDGETEC visível no navegador | b4. Confiabilidade |
| a5. Após falha de rede, a interface nega e o servidor grava o filtro | b5. Capacidade de interação |

No caderno: `a1→__  a2→__  a3→__  a4→__  a5→__`

Depois marque a alternativa:

- A) a1-b1; a2-b3; a3-b5; a4-b2; a5-b4
- B) a1-b3; a2-b1; a3-b5; a4-b2; a5-b4
- C) a1-b3; a2-b1; a3-b2; a4-b5; a5-b4
- D) a1-b3; a2-b5; a3-b1; a4-b2; a5-b4
- E) a1-b4; a2-b1; a3-b5; a4-b2; a5-b3

---

## Parte 3 — Estudo de caso (minutos 65–130)

### O caso

Vocês são a equipe júnior de qualidade do **BDGETEC** (Banco de Dados da CGETEC, Centro Paula Souza). Endereço: https://bdcgetec.cps.sp.gov.br.

O sítio publica, na web, dados das Etecs e Classes Descentralizadas: vestibulinho, matrículas iniciais, totais de alunos, movimentação e aproveitamento, com consultas por unidade, município, eixo e demais recortes da capa. Há login para quem opera o cadastro.

São 16h. A gerência pergunta: “A consulta pública de escolas e vestibulinho está no ar. No computador da gerência, com mouse, cabo e conta administrativa, funcionou. O novo período começa amanhã. Tem qualidade suficiente?”

O pedido de software diz só: consultar unidades, vestibulinho e totais de alunos e permitir login de operação. Não há critério documentado de desempenho, interação, acessibilidade, segurança, confiabilidade ou recuperação. Como é **sítio de governo**, a omissão não apaga LBI/eMAG. Não redija parecer jurídico.

**Evidências** (laboratório, salvo o item 3, observável na página pública)

1. Em 20 execuções no teste, a consulta “Mapeamento das Escolas” com período válido foi concluída 20 vezes.
2. Com 600 sessões simultâneas em “Totais de Alunos”, o percentil 95 sobe de 1,8 s para 14,2 s.
3. O menu **Mapeamento** só abre com `onmouseover`. Três pessoas que usam só teclado não chegaram a Escolas, Vestibulinhos nem Totais de Alunos. Login sem `label`.
4. No navegador aparece um dado de login do BDGETEC. O teste **não** confirmou uso da conta de outra pessoa nem exposição de dados pessoais.
5. Em duas falhas de rede a interface mostrou “operação não concluída”, mas o filtro foi gravado. Na nova tentativa o relatório ficou inconsistente.
6. A equipe estima seis horas para alterar uma regra de relatório. Numa mudança anterior o mesmo módulo levou quatro dias e gerou regressão.
7. A operação informa disponibilidade de 99,5%, sem janela, fonte, exclusões ou histórico.
8. A enquete interna registra 4,6/5 entre oito pessoas da própria equipe de desenvolvimento.

O novo período começa amanhã, mas a decisão pode ser adiada. Não há tempo para eliminar toda incerteza. **Não** atacar o sítio em produção.

**Seu grupo trabalha só a evidência sorteada.** Não proponha correção técnica antes de terminar a questão 2.

### Questão 1 — O caso fala de quê? (todos os grupos)

Não escreva definição. Não use texto de ISO. Marque **uma** letra em cada linha.

- **P** = produto (o sítio)
- **U** = uso (pessoa fazendo a tarefa)
- **D** = dados (números que o sítio publica)
- **R** = processo (como se constrói e corrige)

| # | Frase | Letra |
|---|---|---|
| 1 | A consulta de escolas concluiu 20 vezes no teste. | P / U / D / R |
| 2 | Três pessoas só com teclado não abriram o menu Mapeamento. | P / U / D / R |
| 3 | Depois da falha de rede, o relatório ficou inconsistente. | P / U / D / R |
| 4 | A equipe estima 6 horas para mudar uma regra; numa mudança anterior levou 4 dias e quebrou outra coisa. | P / U / D / R |

### Questão 2 — Diagnóstico (ainda sem solução)

Evidência nº ____.

- Fato observado:
- Inferência:
- Lacuna:
- Stakeholder:
- Contexto:
- Consequência:
- Característica predominante e justificativa com palavras do caso:

Não vote a aceitação nesta questão. Diga se a evidência é observável no sítio ou laboratório didático.

### Questão 3 — Requisito verificável

Complete:

> Para **[stakeholder]**, no contexto **[condições]**, o BDGETEC deverá **[resultado observável]**, medido por **[medida e método]**, atingindo **[limiar]**, durante **[janela]**.

O limiar é necessidade, acordo, palpite ou obrigação legal/normativa? Quem mede, e de qual fonte?

### Questão 4 — Decisão

Aceitar / não aceitar / aceitar com condições.

- Justificativa (risco e evidência):
- Evidência mínima que mudaria a decisão:
- O que ainda não pode ser concluído:
- Quem, na instituição, teria autoridade de aceite:

---

## Parte 4 — Revisão cruzada (minutos 130–155)

Troquem o caderno conforme a tabela do professor. O revisor **não reescreve** a solução. Marque sim / parcial / não e faça **uma** pergunta:

- O stakeholder está identificado?
- O contexto está delimitado?
- O resultado é observável?
- Medida, unidade, fonte e limiar estão definidos?
- A evidência sustenta a decisão sem extrapolação?

Autor: aceita ou recusa a crítica, em uma linha.

---

## Parte 5 — Ticket de saída (minutos 155–170)

Volte à Parte 0 e complete:

> Antes eu decidia por ___. Agora preciso de característica, requisito, medida e ___.

Pergunta final, sem catálogo de processos:

> Qual processo precisaria existir para essa evidência ser produzida de novo no próximo período?
