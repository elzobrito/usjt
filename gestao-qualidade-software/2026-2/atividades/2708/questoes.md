# Aula 02 — Questões de caderno (27/08)

**UC:** Gestão da Qualidade de Software  
**Produto:** [BDGETEC](https://bdcgetec.cps.sp.gov.br)  
**Turma:** CCP1AN-MCC2-91149740  
**Formato:** papel e caneta; sem notebook do aluno  
**ISO:** só citar no quadro. **LBI / eMAG:** podem ser usados.

Não load-teste, não tente senhas e não mexa no login em produção.

---

## Parte 0 — Diagnóstico (0–15 min · individual)

No quadro:

> Uma consulta de escolas foi concluída com sucesso. O BDGETEC tem qualidade?

No caderno, em silêncio:

1. Decisão: sim / não / não sei
2. Duas razões
3. Uma informação que falta

Não leia o caso ainda.

---

## Parte 1 — Teste de erros (15–35 min · individual)

Julgue **V** ou **F**. Depois marque a sequência A–E.

1. Concluir uma consulta de escolas com período válido no ambiente de teste prova que o BDGETEC tem qualidade suficiente para o novo período no dia seguinte.
2. Como o BDGETEC é sítio de governo, a Lei Brasileira de Inclusão (Lei nº 13.146/2015) e o eMAG podem ser usados nesta aula como fonte de critério de acessibilidade, mesmo que o pedido de software não mencione isso.
3. A família SQuaRE organiza perguntas sobre produto, uso e dados, mas o modelo não escolhe automaticamente prioridade, métrica, limiar nem a decisão institucional.
4. Ver no navegador um dado de login do BDGETEC autoriza afirmar, sem investigação adicional, que houve invasão confirmada e vazamento de dados pessoais.

| | 1 | 2 | 3 | 4 | Sequência |
|---|---|---|---|---|---|
| Sua marca | V/F | V/F | V/F | V/F | A B C D E |

- A) V F V F
- B) F F V F
- C) F V V F
- D) F F F V
- E) V F F F

---

## Parte 2 — Correspondência (35–65 min)

Associe cada evidência à característica **predominante**. Uma evidência pode tocar outras; a predominante tem de caber no texto.

| Evidência (A) | Característica (B) |
|---|---|
| a1. Vinte consultas de escolas concluídas no ambiente de teste | b1. Eficiência de desempenho |
| a2. Percentil 95 sobe de 1,8 s para 14,2 s com 600 sessões em Totais de Alunos | b2. Segurança da informação |
| a3. Três pessoas só com teclado não abrem o menu Mapeamento (o menu só abre quando o mouse passa por cima) | b3. Adequação funcional |
| a4. Dado de login do BDGETEC visível no navegador | b4. Confiabilidade |
| a5. Após falha de rede, a interface nega e o servidor grava o filtro | b5. Capacidade de interação |

No caderno: `a1→__  a2→__  a3→__  a4→__  a5→__`

- A) a1-b1; a2-b3; a3-b5; a4-b2; a5-b4
- B) a1-b3; a2-b1; a3-b5; a4-b2; a5-b4
- C) a1-b3; a2-b1; a3-b2; a4-b5; a5-b4
- D) a1-b3; a2-b5; a3-b1; a4-b2; a5-b4
- E) a1-b4; a2-b1; a3-b5; a4-b2; a5-b3

---

## Parte 3 — Estudo de caso (65–130 min)

Vocês são a equipe júnior de qualidade do **BDGETEC**.

São 16h. A gerência pergunta: *“No computador da gerência, com mouse, cabo e conta administrativa, a consulta de escolas funcionou. O novo período começa amanhã. Tem qualidade suficiente?”*

O pedido de software pede só: consultar unidades, vestibulinho, totais de alunos e login. Não há critério escrito de desempenho, teclado, segurança ou falha. É sítio de governo: a omissão não apaga LBI e eMAG. Não escreva parecer jurídico.

**Evidências** (1, 2, 5, 6, 7 e 8 = laboratório; 3 = página pública; 4 = indício)

1. 20 consultas de “Mapeamento das Escolas” no teste concluíram 20 vezes.
2. Com 600 sessões em “Totais de Alunos”, o tempo de 95% das respostas sobe de 1,8 s para 14,2 s.
3. Três pessoas só com teclado não abrem o menu Mapeamento (só abre quando o mouse passa por cima).
4. No navegador aparece um dado de login. O teste **não** confirmou uso da conta de outra pessoa nem vazamento de dados.
5. A tela diz “não concluiu”, mas o servidor gravou o filtro; na nova tentativa o relatório ficou inconsistente.
6. A equipe estima 6 horas para mudar uma regra; numa mudança anterior o mesmo módulo levou 4 dias e quebrou outra coisa.
7. A operação informa 99,5% de disponibilidade, sem dizer período, fonte nem o que fica de fora.
8. Enquete interna: 4,6/5 entre 8 pessoas da própria equipe de desenvolvimento.

O grupo trabalha **só a evidência sorteada**. Não proponha correção antes de terminar a questão 2.

### Questão 1 — O caso fala de quê? (todos os grupos)

Não escreva definição. Não use texto de ISO. Uma letra por linha.

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

Não vote a aceitação. Diga se a evidência é do sítio ou do laboratório.

### Questão 3 — Requisito verificável

> Para **[stakeholder]**, no contexto **[condições]**, o BDGETEC deverá **[resultado observável]**, medido por **[medida e método]**, atingindo **[limiar]**, durante **[janela]**.

O limiar é necessidade, acordo, palpite ou obrigação legal (LBI/eMAG)? Quem mede, e de qual fonte?

### Questão 4 — Decisão

Aceitar / não aceitar / aceitar com condições.

- Justificativa (risco e evidência):
- Evidência mínima que mudaria a decisão:
- O que ainda não pode ser concluído:
- Quem, na instituição, teria autoridade de aceite:

---

## Parte 4 — Revisão cruzada (130–155 min)

O revisor **não reescreve**. Marque sim / parcial / não e faça **uma** pergunta:

- O stakeholder está identificado?
- O contexto está delimitado?
- O resultado é observável?
- Medida, unidade, fonte e limiar estão definidos?
- A evidência sustenta a decisão sem extrapolação?

Autor: aceita ou recusa a crítica, em uma linha.

---

## Parte 5 — Ticket (155–170 min)

> Antes eu decidia por ___. Agora preciso de característica, requisito, medida e ___.

> Qual processo precisaria existir para essa evidência ser produzida de novo no próximo período?


## Parte 6
### Uma escola deseja criar um sistema para empréstimo de livros.

O aluno poderá pegar alguns livros emprestados.
Os livros deverão ser devolvidos rapidamente.
Se houver atraso, o aluno receberá uma punição.
O sistema deverá ser fácil de usar.

Tarefa no caderno

1. Encontre palavras pouco claras

Copie do documento três palavras ou expressões que podem causar dúvidas.


2. Responda às perguntas

Quantos livros o aluno pode pegar?

Quantos dias ele pode ficar com o livro?

Qual é a punição por atraso?

O que significa um sistema “fácil de usar”?

3. Dê sua opinião

As informações do documento são suficientes para começar a programar o sistema?

( ) Sim
( ) Não

Explique sua resposta em uma frase:

4. Corrija uma frase

Reescreva esta frase de maneira mais clara:

Os livros deverão ser devolvidos rapidamente.

Frase corrigida: