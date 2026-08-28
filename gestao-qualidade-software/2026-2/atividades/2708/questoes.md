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

## Parte 3
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


# Atividade: Qualidade e “Zero-defeito”

## Leia a situação

Uma equipe criou um aplicativo de calculadora. Antes de entregar o aplicativo, realizou apenas um teste:

> 2 + 2 = 4

Como o resultado estava correto, a equipe afirmou:

> “O aplicativo não possui nenhum erro.”

## Responda no caderno

### 1. Marque verdadeiro ou falso

a) ( ) Um único teste garante que o aplicativo não possui erros.  
b) ( ) O objetivo dos testes é procurar possíveis erros.  
c) ( ) É possível testar todas as situações de qualquer software.  
d) ( ) A qualidade busca reduzir ao máximo a quantidade de defeitos.  
e) ( ) Os defeitos devem ser identificados o mais cedo possível.

### 2. Pense em outros testes

Escreva três operações diferentes que poderiam ser usadas para testar a calculadora.

1. ______________________________________  
2. ______________________________________  
3. ______________________________________  

### 3. Encontre situações especiais

O que a calculadora deveria fazer nestas situações?

a) Divisão por zero: ______________________________

b) Número muito grande: __________________________

c) Usuário digita uma letra: _______________________

### 4. Explique com suas palavras

O que significa afirmar que um software com “zero defeito” é praticamente inatingível?

____________________________________________________

____________________________________________________

### 5. Decisão da equipe

A equipe pode garantir que a calculadora não possui erros apenas porque o teste “2 + 2” funcionou? Explique.

____________________________________________________

____________________________________________________
