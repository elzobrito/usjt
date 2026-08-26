# Atividade de caderno — Correlação URL × rota

**UC:** Usabilidade, desenvolvimento web, mobile e jogos (0011109)  
**Aula 5:** da interface ao dispatcher  
**Formato:** individual, no caderno (pode olhar o próprio site)  
**Tempo:** 25 min + 5 min de conferência em dupla  
**Produto avaliado do site:** continua só HTML e CSS. Aqui ninguém programa.

## Objetivo

Dado um endereço, um `href` ou um clique, o estudante aponta **qual rota (se houver)** o servidor usaria — e explica quando **não há correlação**.

Não basta “é a página de contato”. A resposta completa tem **método + caminho**.

---

## Copie isto no alto da folha (legenda)

```text
arquivo  = nome no disco          contato.html
URL      = endereço completo      https://ana.github.io/oficina/contato.html
caminho  = parte depois do host   /oficina/contato.html
rota     = regra do servidor      GET /contato
                                  POST /api/orcamentos
```

Correlação, nesta aula, é a seta:

```text
o que aparece na tela  →  pedido HTTP (método + URL)  →  rota registrada
```

Se faltar o método, a seta está quebrada.  
Se só existir o arquivo HTML, a terceira caixa pode ficar **sem rota**.

---

## Parte 1 — Desmonte a URL (5 min)

A URL ainda **não** é a rota. Separe as peças. Deixe em branco o que não existir.

| # | URL | esquema | host | caminho | query | fragmento |
|---|---|---|---|---|---|---|
| 1 | `https://ana.github.io/oficina/contato.html` | | | | | |
| 2 | `https://ana.github.io/oficina/contato.html?nome=Lia` | | | | | |
| 3 | `http://127.0.0.1:8000/api/solicitacoes` | | | | | |
| 4 | `https://loja.exemplo/contato#formulario` | | | | | |
| 5 | `/api/orcamentos/DEMO-0007` | | | | | |

Depois, uma frase:

> O roteador desta aula compara principalmente ________ e ________.  
> Query e fragmento: quem lê cada um?

Dica: o fragmento (`#formulario`) **não** vai para o servidor.

---

## Parte 2 — Uma etiqueta só (4 min)

Para cada item, escreva **apenas uma**: `arquivo` · `URL` · `caminho` · `rota` · `não é nenhum`.

Não vale marcar dois. Se parecer os dois, escolha o mais específico e justifique em meia linha.

| # | Item | Etiqueta | Por quê (meia linha) |
|---|---|---|---|
| A | `contato.html` | | |
| B | `https://ana.github.io/oficina/contato.html` | | |
| C | `/contato` | | |
| D | `GET /contato` | | |
| E | `POST /api/orcamentos` | | |
| F | `/enviarFormulario` | | |
| G | `href="servico.html"` | | |
| H | `GET /api/orcamentos/42` | | |
| I | `Pages` / GitHub | | |
| J | `method="get"` no `<form>` | | |

Armadilhas:

- `C` é caminho, não rota: falta o método.
- `F` parece rota, mas nomeia o botão, não o recurso.
- `G` é um trecho de HTML que **produz** um pedido; ainda não é a rota.
- `I` é hospedagem, não endereço nem regra.

---

## Parte 3 — A tabela de correlação (10 min)

Três colunas. Na coluna da direita, copie o código da rota (`R1`…`R6`) **ou** escreva `nenhuma`.

Rotas já registradas no servidor **didático** (não é o GitHub Pages):

```text
R1  GET    /                     home
R2  GET    /contato              página do formulário
R3  GET    /servico              página do serviço
R4  POST   /api/orcamentos       criar pedido de orçamento
R5  GET    /api/orcamentos       listar pedidos (se autorizado)
R6  GET    /api/orcamentos/{id}  consultar um protocolo
```

O que chega:

| # | Na tela / no código | Pedido HTTP que o navegador monta | Rota |
|---|---|---|---|
| 1 | Menu: `href="contato.html"` no site do Pages | | |
| 2 | Menu: `href="servico.html"` no site do Pages | | |
| 3 | Demo da aula: abrir `http://127.0.0.1:8000/` | | |
| 4 | Demo: `fetch('/api/solicitacoes', { method: 'POST', ... })` | | |
| 5 | Botão **Enviar pedido** do site de ontem: `<form action="contato.html" method="get">` | | |
| 6 | Mesmo botão, se o servidor tivesse a rota de criar orçamento | | |
| 7 | Pessoa cola na barra: `.../api/orcamentos/DEMO-0007` | | |
| 8 | Pessoa abre `.../contato#formulario` | | |
| 9 | `POST /contato` (alguém inventou no Postman) | | |
| 10 | `GET /api/orcamentos?status=aberta` | | |
| 11 | `DELETE /api/orcamentos/DEMO-0007` | | |
| 12 | `GET /enviarFormulario` | | |

Para cada linha em que a rota for `nenhuma`, escreva **o motivo em uma destas fórmulas**:

- *há URL, mas o servidor não registrou método + caminho*
- *é arquivo estático; Pages devolve o HTML, não despacha API*
- *o fragmento não entra na comparação*
- *o nome descreve a tela, não o recurso*

---

## Parte 4 — Dois testes (o que a correlação não é 1 para 1)

### 4.1 Mesmo caminho, rotas diferentes

```text
GET  /api/orcamentos
POST /api/orcamentos
```

Complete:

| Pergunta | Resposta |
|---|---|
| A URL do caminho é a mesma? | |
| A rota é a mesma? | |
| O que muda na intenção? | |
| Se o botão Enviar usar GET nesse caminho, que rota casa? | |

### 4.2 URLs diferentes, mesma rota

Rota registrada: `GET /api/orcamentos/{id}`

| URL (caminho) | Casa com a rota? | `id` extraído |
|---|---|---|
| `/api/orcamentos/DEMO-0001` | | |
| `/api/orcamentos/DEMO-0009` | | |
| `/api/orcamentos` | | |
| `/api/orcamentos/DEMO-0001/pdf` | | |
| `/orcamentos/DEMO-0001` | | |

Uma frase:

> Duas URLs correlacionam com a **mesma** rota quando ________________________________.

---

## Parte 5 — O seu site (obrigatório)

Abra o `contato.html` de ontem. Sem inventar JavaScript.

```text
href do menu Contato:          ________________
action do form:                ________________
method do form:                ________________
```

Agora as três setas, **como o site está hoje** (GitHub Pages):

```text
clique no menu Contato
  → pedido:  GET + URL ________________________________
  → rota do Pages:  (arquivo estático / sem API)

clique em Enviar pedido
  → pedido:  ________ + URL ________________________________
  → o que de fato acontece: ________________________________
  → rota de criação (POST /api/…): correlaciona?  sim / não
```

Terceira seta: **o contrato que a aula pede**, ainda não implementado:

```text
ação da pessoa: criar ________________________________
pedido desejado: POST /api/________________
sucesso: 201
isso correlaciona com o form atual?  sim / não
por quê?
```

---

## Parte 6 — Frase de correlação (exit ticket, individual)

Complete **as quatro lacunas**. Sem a quarta, a resposta está incompleta.

> A URL `________________` com o método `________` correlaciona com a rota `________________` porque ________________________________.  
> Não correlaciona com `________________` porque ________________________________.

---

## Conferência em dupla (5 min)

A dupla lê só o caderno, não o site.

1. Aponta uma linha da Parte 3 e pede: “qual caixa da seta está preenchida — tela, pedido ou rota?”
2. Cobra a Parte 5: o Enviar de ontem correlaciona com `POST`? Se a resposta for sim, a dupla marca erro.
3. Lê o exit ticket em voz alta. Se faltar método, devolve a folha.

---

## O que conta como feito

- Separou esquema, host, caminho, query e fragmento em pelo menos três URLs.
- Não chamou `contato.html` de rota.
- Preencheu a coluna **Rota** da Parte 3, inclusive com `nenhuma`.
- Mostrou um caso de mesmo caminho / duas rotas e um caso de duas URLs / uma rota.
- No site de ontem, o `method="get"` + `action="contato.html"` **não** foi desenhado como `POST /api/...`.

---

## Gabarito docente (não projetar no começo)

### Parte 1

| # | esquema | host | caminho | query | fragmento |
|---|---|---|---|---|---|
| 1 | `https` | `ana.github.io` | `/oficina/contato.html` | — | — |
| 2 | `https` | `ana.github.io` | `/oficina/contato.html` | `nome=Lia` | — |
| 3 | `http` | `127.0.0.1:8000` | `/api/solicitacoes` | — | — |
| 4 | `https` | `loja.exemplo` | `/contato` | — | `formulario` |
| 5 | — | — | `/api/orcamentos/DEMO-0007` | — | — |

Roteador: **método** e **caminho**. Query pode filtrar depois; fragmento fica no navegador.

### Parte 2

| # | Etiqueta |
|---|---|
| A | arquivo |
| B | URL |
| C | caminho |
| D | rota |
| E | rota |
| F | caminho (mal nomeado) / não é rota de domínio |
| G | não é nenhum (é HTML que gera um GET para arquivo) |
| H | rota |
| I | não é nenhum |
| J | não é nenhum (é atributo; vira método do pedido) |

### Parte 3

| # | Pedido HTTP | Rota | Motivo se nenhuma |
|---|---|---|---|
| 1 | `GET` + URL `.../contato.html` | **nenhuma** das R1–R6 | Pages serve o **arquivo**; não é `GET /contato` a menos que o servidor reescreva |
| 2 | `GET` + `.../servico.html` | **nenhuma** | idem |
| 3 | `GET /` | **R1** | demo local |
| 4 | `POST /api/solicitacoes` | **nenhuma** nesta tabela (a tabela é de orçamentos) | caminho diferente; na demo da aula essa rota existe, mas não é R4 |
| 5 | `GET .../contato.html?nome=...` | **nenhuma** | GET no arquivo; query na URL; **não cria** recurso |
| 6 | `POST /api/orcamentos` | **R4** | contrato desejado, ainda não é o form de ontem |
| 7 | `GET /api/orcamentos/DEMO-0007` | **R6** | `{id}` = `DEMO-0007` |
| 8 | `GET /contato` (fragmento retido no cliente) | **R2** | `#formulario` não entra na rota |
| 9 | `POST /contato` | **nenhuma** | existe R2 em GET, não em POST |
| 10 | `GET /api/orcamentos` | **R5** | query `status=aberta` não muda a rota |
| 11 | `DELETE ...` | **nenhuma** | método não registrado |
| 12 | `GET /enviarFormulario` | **nenhuma** | nome de botão; recurso não existe |

Ponto a marcar em voz alta: **1, 2 e 5** são o site de ontem. Correlação tela → arquivo, não tela → API.

Linha 4 é propositalmente traiçoeira: quem copiar `R4` misturou o recurso da demo (`/api/solicitacoes`) com o da tabela (`/api/orcamentos`). Caminho diferente = rota diferente.

### Parte 4

- 4.1: caminho igual, rotas diferentes; GET consulta, POST cria; botão com GET casa com a rota de consulta (ou com nenhuma, se só existir POST).
- 4.2: `DEMO-0001` e `DEMO-0009` sim; coleção `/api/orcamentos` não (é R5); `/pdf` só se o padrão aceitar barra (no `{id}` rígido, não); `/orcamentos/...` sem `/api` não casa.

> Duas URLs correlacionam com a mesma rota quando método e padrão de caminho batem, mesmo com identificadores diferentes.

### Parte 5

Site-padrão: `href="contato.html"` · `action="contato.html"` · `method="get"`.  
Enviar **não** correlaciona com `POST /api/...`. Recarrega o arquivo com query string.

### Parte 6 — exemplo aceitável

> A URL `/api/orcamentos/DEMO-0007` com o método `GET` correlaciona com a rota `GET /api/orcamentos/{id}` porque o caminho casa com o padrão e o método é o mesmo. Não correlaciona com `POST /api/orcamentos` porque a intenção é consultar, não criar.

---

## Como usar na aula

Encaixe depois de mom-002 (página ≠ URL ≠ rota) e **antes** da ficha longa de contrato. Se faltar tempo, faça Partes 3 e 5; o resto vira lição de caderno.

Não misture esta folha com o trace do `OliviaRouter`: aqui a tabela R1–R6 já está “compilada”. A correlação é só **casar o pedido com a regra**.
