# Site padrão — layout-contrato

Esqueleto obrigatório da atividade de publicação no GitHub Pages. O enunciado completo está em [../atividade-site.md](../atividade-site.md), com o contrato, os extras permitidos, os critérios e a lista dos 155 negócios.

**Regra da UC:** só HTML e CSS. Sem JavaScript.

Abra `index.html` no navegador (duplo clique ou arrastar o arquivo). Os textos entre `[colchetes]` são o que você troca.

> Esta mesma pasta também está compactada em [`../site-padrao.zip`](../site-padrao.zip), para baixar de uma vez.

## Páginas (não apague, não renomeie)

| Arquivo | Página | O que tem |
|---|---|---|
| `index.html` | Início | Promessa (`h1`), dois botões de ação e a grade de três cards |
| `sobre.html` | Sobre | O que é o negócio, para quem, como trabalha e o que não faz |
| `servico.html` | Serviço | Resultado do serviço, como funciona (3 passos), quanto custa e o botão "Quero este serviço" |
| `contato.html` | Contato | Formulário: Nome, E-mail, Assunto e Mensagem, todos com `label` |
| `404.html` | Página não encontrada | Extra já pronto |
| `css/estilo.css` | Visual do contrato | Cores e fontes no bloco `:root` |
| `img/` | Imagens | Vazia por enquanto; veja o [README da pasta](img/README.md) |
| `.nojekyll` | Arquivo vazio | Manda o GitHub Pages servir os arquivos sem o Jekyll. Precisa ir junto |

Menu nesta ordem: **Início · Sobre · Serviço · Contato**. Todas as páginas têm o link "Saltar para o conteúdo", que aparece ao navegar com a tecla Tab.

> No `index.html`, o `<title>` está como "Faxineira - GERTRUDES" (um exemplo preenchido). Nas outras páginas ele segue o modelo `Página — [Nome do negócio]`. Troque o título de todas pelo nome do **seu** negócio.

## O que você pode mudar

- Todo texto entre `[colchetes]`: nome, promessa, benefícios, passos e rodapé. Nomes, telefones e endereços devem ser fictícios.
- Cores e fontes no bloco `:root` de `css/estilo.css`.
- Fotos em `img/`, com `alt` descritivo.
- Os textos de ajuda e as opções do campo Assunto no formulário.
- Até **dois extras** da lista do enunciado.

## O que você não pode mudar

- A ordem do HTML: `header` → `nav` → `main` → `footer`.
- A ordem dos itens do menu.
- Os `label` ligados aos campos (`for` / `id`).
- A grade de três cards na home.
- Links internos: use `sobre.html`, não `/sobre.html`.

## Sobre o formulário

O formulário usa `action="contato.html" method="get"`: ao enviar, o navegador só recarrega a página com os dados na URL. **Nada é gravado**, porque o GitHub Pages só entrega arquivos. Aqui o que conta é a usabilidade do formulário (rótulos, tipos de campo, ajuda), não o envio. O que o botão "Enviar pedido" deveria fazer num servidor de verdade é o assunto da [aula de 25/08](../../2508/).

## Publicar no GitHub Pages

1. Crie um repositório **público** (Classroom da turma ou `ux-site` na sua conta).
2. Envie **esta pasta** como raiz do repositório (`index.html` na raiz, não dentro de outra pasta).
3. No GitHub: **Settings → Pages → Build and deployment**.
4. Source: **Deploy from a branch**. Branch: `main`. Pasta: `/ (root)`.
5. Espere até 10 minutos. O endereço fica:

   `https://SEU-USUARIO.github.io/NOME-DO-REPO/`

   (ou o da organização da Classroom).

## Conferência rápida

- Cada página tem um `h1`.
- No celular, o menu continua usável e não há rolagem horizontal.
- O formulário tem rótulo visível em todos os campos.
- O contraste do texto e do botão continua legível depois de mudar as cores.
