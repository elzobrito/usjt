# Atividade: site no GitHub Pages (layout-contrato)

**UC:** Usabilidade, desenvolvimento web, mobile e jogos  
**Unidade de referência:** HTML, CSS e publicação estática  
**Status:** rascunho docente para uso em sala  
**Template:** [atividades/site-padrao/](site-padrao/)

---

## Objetivo

Publicar um site estático de **quatro páginas** no GitHub Pages, preenchendo um layout comum da turma. A nota de usabilidade recai sobre conteúdo, hierarquia, formulário e identidade — não sobre inventar outra estrutura.

### Objetivos de aprendizagem

| Competência | Nesta atividade |
|---|---|
| HTML estrutura, CSS veste | Sem JavaScript; páginas semânticas |
| Arquitetura de informação | Mesmo menu, mesmo conjunto de páginas |
| Qualidades de uso | Rótulos, contraste, alvo de toque, skip link |
| Publicação | Site no ar em `github.io` com caminhos relativos |

---

## Organização

| Item | Definição |
|---|---|
| **Formato** | Individual |
| **Produto** | Repositório público + URL do Pages |
| **Código-base** | Copiar `atividades/site-padrao/` |
| **Stack** | HTML + CSS apenas |

---

## Contrato (obrigatório)

1. Quatro páginas, arquivos com estes nomes: `index.html`, `sobre.html`, `servico.html`, `contato.html`.
2. Menu nesta ordem: Início, Sobre, Serviço, Contato.
3. Ordem do HTML: `header` → `nav` → `main` → `footer`.
4. Um `h1` por página. Títulos em sequência (`h1` depois `h2`, sem pular).
5. Formulário de contato com `label` visível, `for`/`id` ligados, `type="email"` no e-mail.
6. Links relativos (`contato.html`, `css/estilo.css`). Não use `/css/estilo.css`.
7. Identidade só pelos tokens em `:root` (`css/estilo.css`).
8. Sem JavaScript.

O aluno **escolhe o negócio** na [lista de 155](#lista-de-negócios-155) (ou um equivalente do mesmo perfil). Troca tudo o que está entre `[colchetes]`. Nomes, telefones e endereços no site devem ser fictícios.

## Extras (no máximo dois)

Lista fechada. Fora da lista = fora do escopo.

1. Página `404.html` (já vem no template — personalizar textos e identidade).
2. Uma página a mais (`faq.html` **ou** `equipe.html`), ligada no menu **depois** de Contato, sem reordenar os quatro itens.
3. Foto real em `img/` na home ou no Sobre, com `alt` descritivo.
4. Variação de identidade no `:root` (cores e fontes) com contraste WCAG AA no texto e no botão.

## O que não fazer

- SPA, React, Bootstrap, Jekyll, WordPress.
- Tirar `label` “para ficar limpo”.
- Menu em outra ordem.
- Caminho absoluto que quebra no Pages de projeto (`/estilo.css`).
- Inventar JavaScript (regra da UC).

---

## Publicação

Settings do repositório → **Pages** → **Deploy from a branch** → `main` + `/ (root)`.

Entregar no canal da disciplina:

1. URL do site publicado.
2. URL do repositório.
3. Quais extras foram usados (0 a 2).

---

## Critérios

| Camada | Evidência |
|---|---|
| **Publicação** | URL no ar; `index.html` na raiz; CSS carrega |
| **Contrato** | Quatro páginas; nav na ordem; labels; sem JS |
| **Usabilidade do conteúdo** | Oferta clara; perfis reais no Sobre; passos no Serviço; o que acontece depois do envio no Contato |
| **Acessibilidade mínima** | Contraste; `alt` se houver imagem; foco visível; um `h1` |
| **Extras** | Usáveis, não só existentes |

Não avaliar “site bonito” nem quantidade de animações. O template já traz o visual; a diferença está no texto e nas decisões de uso.

---

## Escala de turma numerosa

- Template único: o suporte é um só tipo de bug (path, Pages desligado, `index.html` dentro de pasta).
- Correção em duas passagens: (1) URL abre e o contrato está lá; (2) amostra de conteúdo/UX.
- Amostrar 3–4 sites em sala; o restante pelo canal da disciplina.

---

## Lista de negócios (155)

Estabelecimentos de bairro que raramente têm site próprio: vivem de boca a boca, WhatsApp, Instagram ou placa na calçada. Escolha **um**. O formulário deve pedir só o que aquela pessoa consegue informar agora, com segurança.

O produto continua somente em HTML e CSS. O site estático não conclui envio, reserva, orçamento ou agendamento real — deixe isso explícito no Contato.

### Oficina, rua e conserto

| # | Tipo | Usuário principal | O que o formulário pede |
|---|---|---|---|
| 1 | Mecânica de bairro | Dono do carro com barulho ou revisão | Orçamento / encaixe |
| 2 | Borracharia | Motorista com pneu furado ou gasto | Conserto, recape ou troca |
| 3 | Bicicletaria | Quem pedala no bairro | Revisão ou câmara |
| 4 | Autoelétrica | Carro que não pega ou está sem luz | Diagnóstico / horário |
| 5 | Funilaria e pintura | Motorista após batida leve | Orçamento |
| 6 | Alinhamento e balanceamento | Quem sentiu o carro puxando | Agendamento |
| 7 | Troca de óleo | Motorista na quilometragem | Tipo de óleo e horário |
| 8 | Radiadorista | Carro esquentando | Sintoma e encaixe |
| 9 | Escape e escapamento | Carro barulhento | Orçamento da peça |
| 10 | Oficina de suspensão | Quem sentiu tranco ou pendeu | Visita / orçamento |
| 11 | Ar-condicionado automotivo | Motorista no calor com ar morto | Carga ou reparo |
| 12 | Som automotivo | Quem quer rádio, alto-falante ou multimídia | Orçamento |
| 13 | Insulfilm | Dono do carro | Tipo de película e data |
| 14 | Tapeçaria automotiva | Banco rasgado ou teto solto | Reparo e prazo |
| 15 | Martelinho de ouro | Amassado sem pintura | Descrição do amassado e encaixe |
| 16 | Polimento de rua | Carro opaco ou com risco leve | Serviço e data |
| 17 | Guincho de bairro | Motorista parado na rua | Local, tipo de veículo, urgência |
| 18 | Oficina de moto | Motociclista | Revisão, pneu ou orçamento |
| 19 | Recauchutagem | Motorista ou frotinha | Medida do pneu |
| 20 | Loja de peças usadas | Quem precisa de uma peça específica | Peça, modelo e ano |
| 21 | Ferro-velho | Quem leva sucata ou busca peça | O que traz / o que busca |
| 22 | Capotaria | Caminhonete com capota ou lonas | Medida e prazo |
| 23 | Instalação de engate | Quem vai puxar reboque | Modelo do carro e data |
| 24 | Chaveiro automotivo | Quem perdeu ou quebrou a chave do carro | Urgência e modelo |
| 25 | Oficina de patinete e skate | Criança ou adulto com roda ou truck | Conserto |
| 26 | Conserto de carrinho de bebê | Família com roda ou travamento | Peça e prazo |
| 27 | Assistência de eletrodomésticos | Dono do aparelho parado | Marca, sintoma, visita |
| 28 | Recarga de cartucho e toner | Quem imprime em casa ou no comércio | Modelo da impressora |
| 29 | Conserto de fone e caixa de som | Cliente com fio, bluetooth ou chiado | Defeito resumido |
| 30 | Lan house / cabine de internet | Quem precisa imprimir, copiar ou acessar | Horário / serviço |
| 31 | Box de acessórios de celular | Dono do aparelho | Capa, película ou cabo |
| 32 | Película e troca de vidro (box) | Tela trincada | Modelo e horário |
| 33 | Conserto de máquina de costura | Costureira ou quem tem máquina em casa | Marca e defeito |
| 34 | Amolador de facas | Açougue, restaurante ou casa | Quantidade e prazo |
| 35 | Conserto de guarda-chuva e mala | Cliente com haste, zíper ou roda | Conserto e retirada |

### Ofício, costura e obra pequena

| # | Tipo | Usuário principal | O que o formulário pede |
|---|---|---|---|
| 36 | Costureira | Cliente com uma peça | Barra, ajuste, conserto, prazo |
| 37 | Alfaiate | Cliente de calça, paletó ou uniforme | Medida e prova |
| 38 | Sapateiro | Cliente com sapato, bolsa ou salto | Conserto e prazo |
| 39 | Chaveiro | Quem ficou do lado de fora ou quebrou a fechadura | Urgência / tipo de chave |
| 40 | Relojoeiro | Relógio parado | Bateria ou orçamento |
| 41 | Tapeceiro / estofador | Sofá, cadeira ou banco rasgado | Tecido, visita, prazo |
| 42 | Marceneiro | Porta, prateleira ou guarda-roupa | Medida e orçamento |
| 43 | Carpinteiro | Telhado, pergolado ou porta de madeira | Visita |
| 44 | Serralheiro | Portão, grade ou corrimão | Medida e prazo |
| 45 | Vidraceiro | Vidro quebrado, espelho ou box | Medida / urgência |
| 46 | Gesseiro | Sanca, drywall ou forro | Cômodo e visita |
| 47 | Pedreiro de pequeno reparo | Infiltração, piso ou parede | Descrição e visita |
| 48 | Encanador | Vazamento ou entupimento | Cômodo e urgência |
| 49 | Eletricista residencial | Chuveiro, tomada ou disjuntor | Sintoma e período |
| 50 | Pintor de parede | Um cômodo ou fachada | Metragem aproximada |
| 51 | Azulejista | Banheiro ou cozinha | Metragem e visita |
| 52 | Telhadista | Goteira ou telha quebrada | Urgência e tipo de telha |
| 53 | Calheiro | Calha entupida ou solta | Fachada e visita |
| 54 | Soldador de portão | Portão torto ou solda estourada | Descrição e encaixe |
| 55 | Instalador de box | Banheiro sem box ou vidro frouxo | Medida |
| 56 | Cortinas e persianas | Janela nova ou tecido gasto | Medida e tecido |
| 57 | Toldos | Frente de loja ou varanda | Largura e visita |
| 58 | Reforma de colchão | Colchão afundado | Medida e retirada |
| 59 | Restauração de móveis | Móvel de família ou peça gasta | Peça e prazo |
| 60 | Moldureiro | Quadro, diploma ou espelho | Medida e moldura |
| 61 | Bordadeira | Uniforme, toalha ou nome em peça | Texto, cor, prazo |
| 62 | Crocheteira | Encomenda de peça | Modelo, cor, prazo |
| 63 | Confecção de uniforme escolar | Família no início do ano | Tamanho e prazo |
| 64 | Conserto de bolsa e zíper | Cliente com zíper ou alça | Peça e prazo |
| 65 | Estamparia de camiseta de bairro | Time, família ou evento | Arte, quantidade, prazo |

### Casa, pátio e serviço local

| # | Tipo | Usuário principal | O que o formulário pede |
|---|---|---|---|
| 66 | Lavanderia de bairro | Quem precisa da peça no dia seguinte | Tipo de peça e prazo |
| 67 | Tinturaria | Roupa clara manchada ou tapeçaria | Peça e mancha |
| 68 | Passadeira | Roupa social ou uniforme | Quantidade e retirada |
| 69 | Dedetização de bairro | Morador com inseto ou rato | Cômodos e infestação |
| 70 | Desentupidora | Pia, vaso ou caixa de gordura | Urgência e ponto |
| 71 | Limpeza de caixa d'água | Morador na manutenção | Capacidade e data |
| 72 | Limpeza de calha | Depois da chuva ou da queda de folha | Fachada e data |
| 73 | Impermeabilizador | Laje molhando o vizinho de baixo | Área aproximada |
| 74 | Jardineiro / podador | Quintal alto ou árvore na calçada | Serviço e dia |
| 75 | Roçagem de terreno | Terreno baldio ou lote | Tamanho aproximado |
| 76 | Piscineiro | Casa com piscina verde | Frequência e visita |
| 77 | Cerca elétrica | Quem quer fechar o perímetro | Metragem e visita |
| 78 | Portão automático | Portão pesado ou motor queimado | Tipo de portão |
| 79 | Interfone e câmera | Casa ou pequeno comércio | Pontos e visita |
| 80 | Instalador de antena | TV sem sinal ou antena caída | Tipo de sinal |
| 81 | Caça-vazamentos | Conta de água alta ou parede úmida | Sintoma e visita |
| 82 | Bomba d'água / poço | Casa sem pressão ou bomba queimada | Sintoma |
| 83 | Limpeza pós-obra | Depois de reforma | Cômodos e data |
| 84 | Loja de embalagens | Doceria, brechó ou MEI | Tipo e quantidade |
| 85 | Produtos de limpeza a granel | Casa ou pequeno comércio | Produto e refil |
| 86 | Ervanária / casa de chás | Cliente de erva ou chá | Produto e dúvida |
| 87 | Recreação infantil | Aniversário em casa | Data, idade, número de crianças |
| 88 | Locação de inflável / pula-pula | Anfitrião do fim de semana | Data, bairro, tempo |
| 89 | Som para festa | Festa de quintal ou salão | Data, horas, bairro |
| 90 | DJ de bairro | Aniversário ou churrasco | Data e estilo |

### Comida, encomenda e retirada

| # | Tipo | Usuário principal | O que o formulário pede |
|---|---|---|---|
| 91 | Casa de bolo | Família ou colega de trabalho | Sabor, tamanho, data |
| 92 | Marmitaria | Trabalhador no intervalo | Prato do dia / retirada |
| 93 | Doceria de encomenda | Aniversário ou confraternização | Doce, quantidade, data |
| 94 | Salgados para festa | Anfitrião da semana | Kit e horário |
| 95 | Brigadeiria | Encomenda de cento | Sabor e data |
| 96 | Bolo no pote | Cliente da semana | Sabor e quantidade |
| 97 | Geladinho / sacolé | Quem compra no calor | Sabor e encomenda |
| 98 | Barraca de pastel | Cliente na hora do almoço | Recheio e horário |
| 99 | Cachorro-quente de esquina | Quem passa a pé à noite | Pedido e retirada |
| 100 | Espetinho / churrasquinho | Cliente depois do trabalho | Quantidade e ponto |
| 101 | Lanchonete de bairro | Vizinho rápido | Lanche e retirada |
| 102 | Café de esquina | Quem quer café e pão | Encomenda da manhã |
| 103 | Tapiocaria | Café da manhã ou lanche | Recheio e horário |
| 104 | Casa de pão de queijo | Encomenda da tarde | Quantidade e retirada |
| 105 | Açaí de bairro | Cliente no fim da tarde | Tamanho e adicionais |
| 106 | Sorveteria de esquina | Família no fim de semana | Encomenda ou horário |
| 107 | Pizzaria de WhatsApp | Jantar de sexta | Sabor, tamanho, retirada |
| 108 | Esfiharia | Pedido para várias pessoas | Sabor e quantidade |
| 109 | Rotisseria | Almoço de domingo | Prato e horário |
| 110 | Açougue | Quem cozinha no sábado | Corte e encomenda |
| 111 | Peixaria | Almoço de sexta | Peixe e limpeza |
| 112 | Hortifruti / sacolão | Vizinho a pé | Encomenda da semana |
| 113 | Mercearia | Quem falta um item no fim do dia | Encomenda / se tem |
| 114 | Quitanda | Fruta da estação | Pedido e retirada |
| 115 | Distribuidora de bebidas | Churrasco do fim de semana | Marca, quantidade, gelo |
| 116 | Fábrica de gelo | Bar, festa ou peixeiro | Saco e horário |
| 117 | Revenda de gás | Casa no fim do botijão | Troca / entrega no bairro |
| 118 | Galão de água | Casa ou escritório pequeno | Troca de galão |
| 119 | Torrefação de café | Quem compra grão ou moído | Tipo e quantidade |
| 120 | Ovos caipira / sítio | Cliente da semana | Cartela e dia |
| 121 | Mel e apiário | Cliente de pote ou encomenda | Quantidade |
| 122 | Queijaria artesanal | Cliente de peça ou fatia | Tipo e retirada |
| 123 | Kit festa / descartáveis | Aniversário em casa | Lista e data |
| 124 | Buffet caseiro | Almoço de família ou reunião | Número de pessoas e data |
| 125 | Marmita de obra | Pedreiro ou mestre de obras | Quantidade e horário |

### Comércio de rua

| # | Tipo | Usuário principal | O que o formulário pede |
|---|---|---|---|
| 126 | Material de construção | Quem está no meio da reforma | Lista / “tem isso?” |
| 127 | Madeireira | Marceneiro ou morador | Corte e medida |
| 128 | Casa de tinta | Pintor ou morador | Cor, tipo, litros |
| 129 | Ferragens / parafusos | Quem precisa de um parafuso específico | Peça e medida |
| 130 | Material hidráulico | Encanador ou morador | Conexão e bitola |
| 131 | Material elétrico | Eletricista ou morador | Disjuntor, fio, lâmpada |
| 132 | Depósito de areia, brita e cimento | Obra pequena | Volume e entrega no bairro |
| 133 | Casa de ração | Tutor que compra todo mês | Ração, porte, retirada |
| 134 | Agropecuária pequena | Quem cria galinha, horta ou cão | Produto e dúvida |
| 135 | Floricultura de esquina | Visita, luto ou aniversário | Arranjo e horário |
| 136 | Viveiro de mudas | Quintal ou calçada | Planta e retirada |
| 137 | Brechó | Quem busca tamanho ou peça | Reserva / dúvida de tamanho |
| 138 | Sebo | Leitor atrás de um título | Livro / reserva |
| 139 | Móveis e usados | Quem monta casa com pouco | Peça e retirada |
| 140 | Casa de pesca | Pescador da madrugada | Isca e o que tem hoje |
| 141 | Armarinho / aviamentos | Costureira | Linha, zíper, botão |
| 142 | Loja de tecidos | Costureira ou artesã | Metragem e tecido |
| 143 | Papelaria de bairro | Estudante ou MEI | Material e prazo de encadernação |
| 144 | Copiadora / encadernadora | Trabalho de escola ou documento | Quantidade e prazo |
| 145 | Gráfica rápida | Cartão, faixa, banner ou panfleto | Formato, quantidade, prazo |

### Serviço pessoal e ponto de bairro

| # | Tipo | Usuário principal | O que o formulário pede |
|---|---|---|---|
| 146 | Barbearia de esquina | Cliente da semana | Corte e horário |
| 147 | Salão de bairro | Escova, hidratação ou coloração | Serviço e horário |
| 148 | Manicure | Cliente da quinzena | Encaixe |
| 149 | Banho e tosa | Tutor do cão | Porte, dia, horário |
| 150 | Adestrador de bairro | Tutor com cão novo ou reativo | Objetivo e período |
| 151 | Fotógrafo de aniversário | Família da festa | Data, local, número de horas |
| 152 | Banca de jornal | Quem resolve recarga, conta ou revista | Horário / o que faz ali |
| 153 | Carreto e mudança de kombi | Mudança curta no bairro | Origem, destino, data |
| 154 | Locação de mesas, cadeiras e tenda | Churrasco ou festa | Data, quantidade, bairro |
| 155 | Loja de 1,99 / variedades | Quem busca um item barato do dia | Dúvida de produto / reserva |
