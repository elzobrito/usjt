# Bartié como guia da revisão — Aula 04

Esta folha é uma síntese autoral para uso didático; não substitui o livro.

## 1. Verificar é trabalhar sobre artefatos

Nas seções 3.2.1 a 3.2.5 e no capítulo 8, Bartié organiza verificação e validação como partes da garantia da qualidade. Para esta aula, a ideia central é: requisitos, documentos, decisões e código podem ser examinados antes que um comportamento seja executado. A revisão precisa de foco, regras e registro; olhar livremente e dizer “parece certo” produz pouca evidência.

## 2. Revisar é identificar e registrar, não resolver durante a reunião

O capítulo 8 recomenda revisões curtas, focadas e orientadas à identificação de problemas. A adaptação para a turma é simples: durante a primeira passagem, não corrigimos as funções. Selecionamos um requisito, apontamos um fragmento, formulamos a suspeita e prevemos o efeito. Preservar o estado defeituoso permite que a futura aula de TDD comece por uma evidência FAIL.

## 3. Uma sequência estruturada reduz dispersão

Na seção 9.3.3, o processo apresentado percorre tópico, questão, discussão, confirmação do defeito, registro detalhado e continuidade até cobrir o escopo. A tabela estática da aula traduz essa sequência para cinco tópicos do código. A discussão deve permanecer sobre o artefato, não sobre a pessoa que o escreveu.

## 4. Checklist é guia, não prova automática

O capítulo 9 mostra o checklist como instrumento que disciplina a investigação e reduz subjetividade. Nesta aula, as perguntas cobrem período, normalização, contagem, limite do laço e filtragem. Marcar cinco itens não comprova qualidade: cada resposta precisa estar ligada a um requisito e a um fragmento verificável.

## 5. A implementação também pode ser verificada

O capítulo 10 inclui verificação da implementação e exemplos de pontos de inspeção do código-fonte. A turma não está restrita a formatação: verifica se o comportamento codificado é coerente com as regras do pedido e se estruturas como condições e laços sustentam o resultado esperado.

## 6. Validar envolve executar o produto

O capítulo 11 marca a passagem para um produto computacional executável. Na segunda passagem da aula, cada caso tem entrada e esperado definidos antes da execução. O resultado observado produz PASS ou FAIL. Essa evidência vale para o caso, o oráculo e o contexto utilizados; não autoriza declarar o produto livre de defeitos.

## Perguntas do checklist da aula

1. O período codificado corresponde ao período pedido?
2. A contagem depende de dados reais da entrada ou de valor fixo?
3. O laço acessa somente índices válidos?
4. A regional é normalizada conforme a regra?
5. A lista de ativas respeita regional e período?

**Referência principal:** BARTIÉ, Alexandre. *Garantia da Qualidade de Software*. Elsevier, 2002, seções 3.2.1–3.2.5 e capítulos 8–11.
