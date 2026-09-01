# Aula 07 — O contrato da reserva que o Pages ainda não faz

**UC:** Usabilidade, desenvolvimento web, mobile e jogos  
**Data:** 01/09/2026  
**Produto de hoje:** três wireframes em papel + uma ficha de contrato. Sem Flask. Sem Canva. Sem HTML novo.

Na Aula 06 o cadastro era de `usuarios` e o campo era `nome`. O item 3 do ticket pedia o substantivo do site que você publicou. Hoje esse substantivo vira o sistema: o usuário principal da lista de 155 precisa concluir o trabalho (na barbearia, reserva de corte e horário). O GitHub Pages continua só entregando arquivo. O que a foto da mesa registrar no fim da aula é o que a próxima sessão implementa. O que não estiver na foto não entra no `main.py`.

## Três palavras de trabalho

- **Wireframe:** traço rápido no papel que mostra estrutura, campos e botão. Sem cor de marca, sem pixel, sem foto. Tempo de um rabisco, não de um layout.
- **Mockup:** o wireframe com cara de produto (cor, tipo, identidade). Não é o produto de hoje. Quem abrir Canva ou Figma saiu do contrato desta sessão.
- **Protótipo:** o desenho ganha interação. Hoje o protótipo é de papel: a dupla aponta e “clica” nas folhas. Não é o site no ar e não é JavaScript.

Iterar no código Flask sem essas folhas é a forma mais cara de descobrir que o campo errado foi o `mensagem` genérico.

## O que entregar (e o que congela)

Quatro superfícies, todas com **nome, número do tema na lista 155 e data** no canto:

1. Wireframe da tela de pedido (usuário principal).
2. Wireframe do que a pessoa vê depois de enviar (estado **pendente** escrito em palavras).
3. Wireframe da lista de quem atende, com confirmar / recusar / cancelar.
4. Ficha-contrato (os quatro itens abaixo).

Às 190–200 min tira-se foto legível ou deixa-se o papel na mesa. Essa foto é o contrato. Campo, botão, rota ou estado que não estiver nela não entra na aula do Flask.

Não entregar: `main.py`, HTML novo, print da home “bonita”, mockup digital, segundo extra no Pages.

## Parte 1 — O site que já está no ar (caderno, 15–35 min)

Abra o seu `github.io`. Se a URL não abrir, use o `site-padrao` local e o tema que você escolheu na lista.

Escreva:

- URL (ou “sem Pages; tema N”):
- Número e tipo na lista 155:
- Usuário principal (a pessoa da tabela, não “todo mundo”):
- Trabalho que essa pessoa tenta concluir hoje:

No formulário de Contato, circule e copie:

| O que a tela tem hoje | O que você leu |
|---|---|
| `action` | |
| `method` | |
| Campos com `name` | |
| Aviso de que o Pages não envia | sim / não |

Frase obrigatória (complete):

> A pessoa acredita que __________, mas nesta versão o site apenas __________.

Erro a evitar: chamar o GET para `contato.html` de “cadastro no servidor”.

## Parte 2 — Três wireframes (papel, 55–95 min)

Uma folha por tela. Retângulo da página, um `h1`, campos com rótulo e o `name` que o servidor leria, um botão com o caminho POST ao lado. Menu só para não perder Início / Sobre / Serviço / Contato. Sem sombreado, sem paleta, sem logotipo novo.

### Tela A — Pedido (usuário principal)

Quem usa: a pessoa da lista 155.  
O que precisa conseguir: o trabalho daquela linha (barbearia = corte + horário; casa de bolo = sabor, tamanho, data).  
Campos: só o que essa pessoa consegue informar agora, com segurança. Nomes fictícios. Proibido documento, e-mail real, dado de menor.  
Ao lado do botão, escreva o POST, por exemplo `POST /reservas`.

### Tela B — Depois do envio

A pessoa vê o próprio pedido com o estado **pendente** em texto, não só em verde.  
Uma frase do que acontece agora (“a barbearia confirma o encaixe”).  
Não invente tela de pagamento nem de login.

### Tela C — Quem atende

Lista dos pedidos. Cada linha: identificador, campos principais, estado por palavra.  
Ações em POST, intenção no caminho, método POST (como na Aula 06):

- `POST /reservas/<id>/confirmar`
- `POST /reservas/<id>/recusar`
- `POST /reservas/<id>/cancelar`

Troque `reservas` pelo seu substantivo.

### Protótipo de papel (95–115 min)

Com a dupla de tema **diferente** do seu: um faz o papel do usuário principal e “toca” a Tela A; o outro vira o sistema e mostra a Tela B. Depois invertem: alguém atende na Tela C. Se o botão não tiver POST na folha, o sistema não responde — rasura e corrige ainda nesta sessão.

## Parte 3 — Ficha-contrato (115–145 min)

Preencha a partir dos wireframes, não de memória. Se a ficha e o papel divergirem, o papel vence e a ficha se corrige **antes** da foto.

### 1. Substantivo do recurso

Caminho no plural, coisa do negócio, sem verbo de tela.

Válido: `/reservas`, `/encomendas`, `/orcamentos`, `/agendamentos`, `/chamados`.  
Inválido: `/enviar`, `/salvarFormulario`, `/mandaWhats`, `/contato`.

Meu recurso: `/________________`

### 2. Campos que coleta e um que decide não coletar

| Campo (`name`) | Quem informa | Por que precisa |
|---|---|---|
| | usuário principal | |
| | usuário principal | |
| | usuário principal | |

Dado que **não** coleto: ________________  
Por quê (uma linha; segurança, não consegue informar agora, ou o balcão já tem): ________________

### 3. Rotas

| Método | Caminho | Intenção | Quem chama (qual tela) |
|---|---|---|---|
| GET | `/` e as quatro páginas do site | ver o site estático | menu |
| POST | `/________________` | criar o pedido | botão da Tela A |
| POST | `/________________/<id>/confirmar` | confirmar | quem atende, Tela C |
| POST | `/________________/<id>/recusar` | recusar | quem atende, Tela C |
| POST | `/________________/<id>/cancelar` | cancelar | cliente ou atendimento |

As quatro páginas continuam arquivo HTML. O POST é o recurso. HTML de formulário envia GET ou POST; a intenção mora no caminho, como `/editar` e `/excluir` de ontem. Sem PUT, sem DELETE, sem JavaScript.

### 4. Dois papéis e três estados

Estados desta aula, só estes três, escritos em palavra: **pendente**, **confirmado**, **cancelado**.

| Quem | O que faz | Estado de origem | Estado de destino | Rota |
|---|---|---|---|---|
| Usuário principal | cria o pedido | (não existia) | pendente | POST do recurso |
| Quem atende | confirma | pendente | confirmado | `.../confirmar` |
| Quem atende | recusa | pendente | cancelado | `.../recusar` |
| Usuário principal ou quem atende | cancela | pendente ou confirmado | cancelado | `.../cancelar` |

Recusar e cancelar chegam no mesmo estado `cancelado`; o caminho diz quem fez o quê. Não invente `pago`, `em rota` ou `finalizado` nesta ficha.

## Conferência antes de assinar (145–170 min)

A dupla devolve a folha, ainda sem congelar, se aparecer qualquer um:

- verbo de tela no caminho;
- um só papel (sumiu quem atende);
- estado só como cor;
- botão no wireframe sem POST na tabela;
- campo na ficha que não está desenhado, ou o contrário.

Ainda dá para rasurar. Depois da foto, não.

## Assinatura da sessão

Nome: ________________  
Tema (número e tipo): ________________  
Data: 01/09/2026

Li que a foto destas folhas é o contrato da próxima aula. O Flask implementa isto, não o que eu lembrar depois.

## O que não fazer nesta aula

- JavaScript, `fetch`, `onclick`, Flask, banco, PUT, DELETE.
- Canva, Figma, HTML novo, identidade nova no `:root`.
- Copiar o substantivo do colega: cada tema da lista 155 é único na turma.
- Colocar e-mail real, telefone de verdade, documento ou dado de menor no wireframe.
- Entregar só o print do Pages no lugar das quatro superfícies.