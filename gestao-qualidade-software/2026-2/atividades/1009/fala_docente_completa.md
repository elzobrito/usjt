# Fala docente completa — Aula 04

**Uso:** leia antes da aula e siga as seções indicadas pelo roteiro. O texto entre colchetes é ação de sala, não precisa ser pronunciado. A fala é deliberadamente completa para permitir que outro docente conduza a sessão. Adapte somente exemplos de linguagem; preserve os conceitos, os casos e o relógio.

## 0–10 min — Onde mora o FAIL?

[Projete ou escreva apenas `FAIL`. Não abra o código.]

“Boa noite. Hoje nós começaremos por uma palavra que já apareceu na nossa sequência: FAIL. Eu não vou mostrar o programa ainda. Quero que vocês respondam a uma pergunta curta: onde esse FAIL mora? Ele mora no requisito, no código, na execução ou na interpretação de quem olhou o resultado?”

[Espere respostas. Escreva as quatro opções no quadro.]

“Observem que todas parecem possíveis, mas a palavra sozinha não nos dá endereço. FAIL informa que, para um caso e um critério, houve divergência. Ainda não informa qual linha causou a divergência. Também não informa se existe uma única causa. Essa será a tensão da aula: sair de ‘deu errado’ para uma cadeia de evidência que outra pessoa consiga verificar.”

“Hoje vocês serão revisores de uma fatia local da consulta de escolas. Não existe HTTP, login ou dado real. O produto tem cinco defeitos intencionais. A meta não é corrigi-los. A meta é encontrá-los de modo responsável, registrar o que vimos e depois executar casos controlados. Se alguém corrigir primeiro, apaga parte da evidência de que precisaremos na aula de TDD.”

[Pergunte.] “Ao ver somente FAIL, o que podemos afirmar com segurança?”

[Resposta esperada: existe divergência no caso executado, mas a causa ainda não foi localizada.]

“Exatamente. Se alguém disser ‘o código está errado na linha tal’, minha próxima pergunta será: qual requisito e qual fragmento sustentam isso? Essa cobrança não é burocracia. É o que separa opinião de revisão.”

[Peça que cada estudante escreva uma hipótese de uma frase.]

“Guardem essa hipótese. No fim, vocês vão comparar o que pensavam agora com o que conseguem afirmar depois de revisar e validar. Nossa primeira mudança de postura é esta: uma saída não é um diagnóstico completo.”

“Para organizar a investigação, vamos usar Bartié como fonte principal. O livro não será lido como um bloco de definições; vamos transformar um percurso de verificação em uma prática de código.”

## 10–25 min — Bartié: verificar antes de executar

[Desenhe duas linhas no quadro: `artefato → verificação → hipótese registrada` e `produto executável → validação → resultado observado`.]

“Bartié trata a garantia da qualidade ao longo do processo. Nos capítulos dedicados à verificação, o objeto pode ser um requisito, uma decisão, um documento ou a implementação. Isso significa que podemos encontrar problemas relevantes antes de executar o software. Chamaremos essa primeira passagem de verificação estática.”

“Estática não quer dizer superficial. Uma revisão útil precisa de foco, critério e registro. No capítulo 9, o percurso é organizado de forma simples: escolhemos um tópico, levantamos uma questão, discutimos a evidência, confirmamos ou rejeitamos a suspeita, registramos o defeito quando existe e continuamos até cobrir o escopo. Hoje os tópicos são cinco: período, contagem, limite do laço, normalização e filtragem.”

“Outra ideia importante: a revisão procura identificar e registrar problemas. Ela não precisa resolver o problema durante a própria descoberta. Em projetos reais, correção e acompanhamento são essenciais, mas misturar a discussão com uma corrida para editar tudo pode fazer a equipe perder foco e rastreabilidade. Na nossa sequência, há uma razão adicional: a correção será feita depois de um teste que falha, na aula de TDD.”

[Mostre o guia Bartié.]

“O checklist aparece como um guia que reduz subjetividade. Ele disciplina o olhar, mas não pensa por nós. Se uma pessoa apenas marcar ‘sim’ ou ‘não’, sem indicar requisito e fragmento, ela ainda não produziu evidência suficiente. Nosso checklist fará perguntas, não entregará respostas.”

“Agora olhem a segunda linha do quadro. No capítulo 11, Bartié passa a tratar um produto computacional que pode ser executado. Na nossa segunda passagem, chamaremos isso de validação dinâmica: escreveremos a entrada e o resultado esperado, executaremos e registraremos o que foi obtido.”

[Pergunte.] “Uma revisão precisa executar o código para encontrar um problema?”

[Resposta esperada: não; pode examinar o artefato com critérios.]

“E uma validação dinâmica?”

[Resposta esperada: executa o produto e compara comportamento.]

“Ótimo. Evitem duas frases perigosas. A primeira é ‘todo teste é apenas execução’. Bartié organiza também testes de verificação sobre artefatos e atividades. A segunda é comemorar qualquer FAIL sem avaliar o oráculo. FAIL pode ser uma evidência valiosa, mas só é interpretável se o oráculo estiver correto. PASS também pode ser valioso. Nenhum dos dois merece comemoração automática; ambos pedem leitura.”

“Copiem duas frases com suas palavras: verificação examina o artefato com critério; validação executa o produto e compara esperado com obtido. Daqui a pouco essas frases terão cinco exemplos concretos.”

## 25–40 min — Um critério, uma linha e uma hipótese

[Entregue a folha e abra o arquivo, mas mantenha o terminal fechado.]

“Vamos modelar uma revisão. Não começaremos por um dos cinco gabaritos completos, para não transformar a prática em cópia. Observem o formato da primeira tabela: critério, fragmento, defeito suspeito e efeito previsto.”

“Imaginem uma regra simples: a mensagem exibida ao usuário deve ser clara. Se eu encontro no código uma mensagem vazia, o critério é clareza da mensagem; o fragmento é a string vazia; a suspeita é ausência de informação; o efeito previsto é que o usuário não saiba o que aconteceu. Ainda não executei. Tenho uma hipótese rastreável.”

“Qual parte dessa linha é observável agora?”

[Resposta esperada: o requisito e o fragmento.]

“Qual parte ainda é previsão?”

[Resposta esperada: o efeito na execução.]

“É exatamente assim que vocês trabalharão. Para cada tópico da consulta, leiam a regra da folha, localizem o trecho e prevejam um efeito específico. Evitem escrever ‘vai dar erro’. Prefiram ‘vai devolver lista vazia’, ‘vai acessar posição fora do limite’ ou ‘vai incluir escolas de uma regional inexistente’.”

[Mostre os cinco tópicos, sem abrir o gabarito.]

“Nos próximos cinquenta minutos, o terminal fica fechado. O piloto será quem navega pelo arquivo e aponta o fragmento. O navegador registra e pergunta: qual critério? qual trecho? qual efeito? Na metade do tempo vocês trocam de papel.”

“Se alguém disser que executar seria mais rápido, minha resposta será: talvez seja mais rápido obter uma saída, mas o objetivo agora é exercitar a capacidade de antecipar e explicar. Depois vamos executar e verificar se a previsão resiste.”

[Cheque uma linha-modelo em duas mesas.]

“Antes de começar, repitam o contrato: não corrigir as funções, não acessar o site, não instalar ferramenta. Uma linguagem basta. Quem estiver sem runtime faz tudo no papel.”

## 40–90 min — Revisão estática das cinco funções

[Escreva no quadro: período, contar, laço, normalização, ativas.]

“Comecem pelo período. A regra informa o período do caso. Localizem onde o código decide se uma escola pertence à consulta. Não me digam apenas o valor que vocês acham errado. Registrem a condição inteira o suficiente para outra pessoa localizar.”

[Após alguns minutos, circule.]

Perguntas de circulação:

- “Qual requisito vocês estão usando?”
- “Mostrem o fragmento, não a conclusão.”
- “O efeito previsto é observável ou é só o adjetivo ‘errado’?”
- “Vocês executaram? Se sim, fechem o terminal e reconstruam a hipótese pelo artefato.”

“Agora passem para `contar`. Perguntem se a função usa os dados da entrada ou uma quantidade fixa. Não comparem ainda com outra função. A questão estática é: o trecho consegue representar uma regional inexistente?”

“Em `listar`, desenhem uma coleção de três posições: zero, um e dois. Observem a condição de continuidade do laço. Se o índice chegar ao tamanho três, existe uma posição três? Registrem o efeito previsto com precisão.”

“Para normalização, comparem a regra da folha com a condição do código. `NRA1`, `nra1` e uma entrada com espaços representam a mesma regional no pedido. O código prepara a entrada antes de comparar? Registrem sem executar.”

“Em `ativas`, verifiquem se regional e período realmente influenciam a lista devolvida. Uma função pode ter parâmetros no cabeçalho e ainda ignorá-los. O checklist não pergunta se o código parece elegante; pergunta se o comportamento codificado respeita a regra.”

[No minuto 65, anuncie troca de papéis.]

“Troquem piloto e navegador. Quem estava escrevendo agora precisa defender um fragmento; quem estava navegando precisa registrar com palavras próprias.”

[Erros prováveis e falas de intervenção.]

Se a dupla escrever “está errado”: “Isso é um veredito sem evidência. Complete: segundo qual regra, qual fragmento e qual efeito?”

Se a dupla quiser corrigir: “Copiem a mudança desejada no campo de observação, mas não alterem o produto. A aula de TDD precisará deste estado para começar com FAIL.”

Se disserem que já encontraram três e basta: “O escopo da revisão tem cinco tópicos relacionados. Bartié chama atenção para foco e cobertura. Uma revisão curta não significa incompleta.”

Se confundirem defeito com falha: “Estamos olhando o artefato ou observando a execução neste minuto? A resposta indica qual palavra usar.”

[No minuto 80, faça checagem coletiva sem revelar gabarito.]

“Levante a mão quem tem cinco fragmentos. Agora quem tem cinco efeitos previstos. Se falta um, use os dez minutos finais deste bloco. As cinco linhas não precisam ter o mesmo texto, mas precisam ser verificáveis.”

[No minuto 88.]

“Fechem a primeira passagem. Tracem uma linha. Agora escreveremos o esperado antes de executar. A revisão produziu hipóteses; a validação produzirá comportamento observado.”

## 90–110 min — Validação dinâmica: esperado versus obtido

“Na segunda tabela, a coluna mais importante neste momento é esperado. Preencham-na antes de executar. O esperado vem do pedido, não da saída que o programa escolher produzir.”

“Caso um: `buscar("NRA1", "2026/2")`. Esperamos três escolas. Rodem o comando `buscar`. Registrem o que apareceu. Se a linguagem imprimir apenas FAIL, anotem também que a lista interna ficou vazia conforme o oráculo fornecido.”

“Caso dois: `contar("XXX", "2026/2")`. Uma regional inexistente tem quantas escolas? Zero. Rodem `contar` e registrem o três obtido. Essa entrada é importante porque fornece um esperado independente.”

“Caso três: `listar("NRA1")`. Esperamos três linhas sem exceção. Rodem e não se assustem com a mensagem. Uma exceção é o resultado observado do caso. Ela não é automaticamente defeito do computador.”

“Caso quatro: normalização. Usaremos `2026/1` somente para isolar a regional enquanto o defeito de período continua presente. As três formas da regional deveriam produzir a mesma quantidade. Registrem os três resultados.”

“Caso cinco: `ativas("XXX", "2026/2")`. Esperamos lista vazia. Registrem a lista completa devolvida.”

[Enquanto circula, pergunte.] “O esperado foi escrito antes ou depois da saída?”

Se foi escrito depois: “Volte ao pedido e reescreva a justificativa. Ajustar o esperado para combinar com o programa transforma o defeito em regra por conveniência.”

“Agora comparem cada previsão estática com o comportamento. Houve alguma hipótese refutada? Uma hipótese refutada também é aprendizado; revisão não é adivinhação infalível. Neste conjunto, as cinco foram construídas para aparecer, mas o método precisa continuar válido quando uma previsão não se confirma.”

[Pergunte.] “O que mudou entre as duas tabelas?”

[Resposta esperada: na primeira examinamos artefato e previmos; na segunda executamos e observamos.]

“Marquem PASS ou FAIL para cada caso. Não escrevam ‘sucesso’ ou ‘fracasso’ da equipe. Escrevam apenas o resultado da comparação.”

## 110–120 min — Oráculo independente para contar

[Escreva no quadro: `contar("XXX", "2026/2")`; abaixo, `esperado = 0`.]

“Chegamos ao clímax. A versão anterior desta atividade sugeria comparar `contar` com o tamanho de `buscar`. Parece uma reutilização elegante, mas existe um problema: as duas funções pertencem ao mesmo produto e as duas podem estar defeituosas. Se errarem de maneira compatível, podem concordar e produzir PASS.”

“Nosso oráculo precisa de uma referência que não dependa dessa concordância. A regra do domínio é suficiente: uma regional inexistente tem zero escolas. Portanto, a entrada é `XXX`, período `2026/2`, esperado zero. O obtido hoje é três. O caso resulta em FAIL.”

[Pergunte.] “Quem valida o validador quando usamos buscar como única fonte de verdade?”

[Resposta esperada: ninguém; o oráculo herda o defeito de buscar.]

“Escrevam quatro linhas em código ou pseudocódigo: obtenham `contar`, definam esperado zero, comparem e registrem PASS ou FAIL. Não alterem `contar`.”

[Espere dois minutos.]

“Agora expliquem ao par por que esse oráculo é independente. Uma boa resposta não é ‘porque o professor disse’. É: o esperado vem da regra de uma regional inexistente, não de outra implementação suspeita.”

“Se o programa imprimir FAIL, não tratem o resultado como diagnóstico completo. Digam: o caso revelou uma divergência útil. Ainda precisamos do registro estático para diagnosticar a causa provável.”

“Guardem tudo. Temos um intervalo de vinte minutos. Na volta, vamos recuperar lacunas e conferir as evidências entre pares.”

## 120–140 min — Intervalo

“Intervalo de vinte minutos. Retorno no minuto 140. Não há tarefa escondida no intervalo. Deixem as tabelas guardadas e não corrijam as funções.”

[Não ministre conteúdo. No retorno, confirme o estado.]

“Antes de retomar: alguém alterou as funções? Se alterou por curiosidade, reverta para a versão da aula. Precisamos manter a mesma evidência para a conferência.”

## 140–180 min — Completar, revisar e recuperar

“Agora cada dupla identifica onde está sua pendência. Existem três trilhas: primeira tabela incompleta, segunda tabela incompleta ou oráculo dependente. Escolham uma e levantem um dedo, dois dedos ou três dedos. Isso me permite circular pela necessidade, não pela ordem das carteiras.”

[Para trilha 1.]

“Se a revisão estática está incompleta, voltem ao checklist. Não executem de novo. Perguntem: qual regra, qual fragmento, qual efeito previsto? O objetivo é completar a cadeia do artefato.”

[Para trilha 2.]

“Se a validação está incompleta, confiram se o esperado foi definido pelo pedido. Depois executem apenas o caso faltante e registrem a saída exata, inclusive exceção.”

[Para trilha 3.]

“Se o oráculo depende de buscar, substituam a fonte do esperado pela regra da regional inexistente. Não substituam a função do produto; substituam somente a justificativa do esperado.”

[Após dez minutos, promova conferência cruzada.]

“Troquem a folha com outra dupla. A dupla revisora não corrige texto em silêncio. Ela faz uma pergunta: ‘qual critério sustenta esta linha?’ ou ‘de onde veio este esperado?’. A dupla autora responde e decide se ajusta o registro.”

“Revisar não é atacar o autor. Bartié separa papéis e mantém a discussão sobre o material. Comentem o requisito e a evidência, não a habilidade da pessoa.”

[Erros e intervenções.]

Se copiaram o gabarito do outro grupo: “Uma resposta igual pode estar correta, mas mostrem a justificativa no próprio arquivo. Sem fragmento, a cópia não é evidência.”

Se corrigiram o código: “Revertam juntos. Anotem a correção desejada à parte. A função permanece defeituosa porque a transformação desta aula está no raciocínio e no registro.”

Se PASS for tratado como prova total: “Enumerem as entradas não testadas. Uma única lista já mostra por que a conclusão precisa ser limitada.”

Se FAIL for tratado como causa: “Qual fragmento da primeira tabela localiza a causa provável? A segunda tabela sozinha mostra divergência, não endereço.”

[No minuto 165, aplique rubrica por amostragem.]

“Vou olhar quatro aspectos: cinco hipóteses estáticas, cinco comparações dinâmicas, oráculo independente e preservação do código. Iniciante não significa incapaz; significa que ainda falta uma parte observável. Adequado significa que a cadeia está completa. Avançado significa que vocês conseguem explicar os limites do próprio método.”

[No minuto 175.]

“Finalizem a conferência. Devolvam a folha com uma pergunta e uma melhoria concreta. Daqui a pouco o ticket será individual, para que eu saiba se a distinção pertence a cada estudante e não apenas à dupla.”

## 180–195 min — Ticket individual

“Silêncio por alguns minutos. Duas perguntas. Primeira: usando uma função desta aula, explique a diferença entre verificação estática e validação dinâmica. Segunda: por que um PASS não prova que o produto não possui defeitos?”

“Uma resposta insuficiente seria ‘verificação é teoria e validação é prática’. Isso não mostra o objeto nem a ação. Uma resposta adequada diz que, na verificação, examinamos requisito e fragmento sem executar; na validação, executamos uma entrada e comparamos esperado com obtido.”

“Para a segunda pergunta, evitem ‘porque pode ter bug’. Delimitem: o PASS cobre aquela entrada, aquele oráculo, aquele ambiente e aquele comportamento observado. Outras entradas, propriedades ou defeitos podem continuar fora do caso.”

[Dê sete minutos de escrita.]

[Leia três respostas, preservando autoria se necessário.]

“Se alguém escreveu que FAIL prova a causa, acrescente: FAIL mostra divergência. A primeira tabela e outras investigações localizam causas prováveis. Se alguém escreveu que PASS não vale nada, ajuste: PASS é evidência útil, só não é evidência total.”

“Compare sua hipótese do começo com o ticket. No início talvez você tivesse apenas uma palavra. Agora consegue dizer qual artefato foi examinado, qual comportamento foi executado e qual conclusão cabe na evidência. Essa é a transformação da aula.”

## 195–200 min — Encerramento

[Escreva quatro palavras: artefato, execução, oráculo, evidência.]

“Fechamos com quatro palavras. Artefato: o que examinamos na revisão. Execução: o que fizemos na validação dinâmica. Oráculo: a referência que permitiu comparar esperado e obtido. Evidência: o registro que sustenta uma conclusão limitada.”

“Hoje não corrigimos as funções. Isso foi intencional. Na aula de TDD, a regra será escrever ou preservar o FAIL antes da alteração. Antes disso, na Aula 05, vamos organizar onde esses testes vivem: unidade, integração, sistema e outros níveis, ainda usando uma fatia local e sem HTTP.”

[Pergunte.] “O que um PASS permite afirmar?”

[Resposta esperada: que o caso observado produziu o esperado naquele contexto.]

“E o que um FAIL permite afirmar?”

[Resposta esperada: que houve divergência, ainda exigindo diagnóstico.]

“Perfeito. Guardem as tabelas e não levem como tarefa uma versão corrigida. Levem a cadeia de evidência. Aula encerrada.”

## Proveniência e limites

A organização didática usa como fonte principal Alexandre Bartié, *Garantia da Qualidade de Software* (2002), especialmente as seções 3.2.1–3.2.5 e os capítulos 8, 9 e 10 para verificação, revisões e checklist, com o capítulo 11 como ponte para validação executável. O conteúdo foi parafraseado; não reproduz extensamente a obra. A ementa institucional da UC 0006960 fornece a baliza curricular. Pressman e Delamaro são referências complementares. Esta aula não cobre inspeção organizacional completa, HTTP, Selenium, automação de interface ou correção das funções.
