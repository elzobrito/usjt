# Site padrão — layout-contrato

Esqueleto obrigatório da atividade de publicação no GitHub Pages.

**Regra da UC:** só HTML e CSS. Sem JavaScript.

Abra `index.html` no navegador (duplo clique ou arrastar o arquivo). Os textos entre `[colchetes]` são o que você troca.

## Páginas (não apague, não renomeie)

| Arquivo | Página |
|---|---|
| `index.html` | Início |
| `sobre.html` | Sobre |
| `servico.html` | Serviço |
| `contato.html` | Contato |
| `404.html` | Página não encontrada (extra já pronto) |
| `css/estilo.css` | Visual do contrato |

Menu nesta ordem: **Início · Sobre · Serviço · Contato**.

## O que você pode mudar

- Todo texto entre `[colchetes]` (nome, promessa, benefícios, passos, rodapé).
- Cores e fontes no bloco `:root` de `css/estilo.css`.
- Fotos em `img/`, com `alt` descritivo.
- Até **dois extras** da lista do enunciado (`atividade-site.md`).

## O que você não pode mudar

- A ordem do HTML: `header` → `nav` → `main` → `footer`.
- A ordem dos itens do menu.
- Os `label` ligados aos campos (`for` / `id`).
- A grade de três cards na home.
- Links internos: use `sobre.html`, não `/sobre.html`.

## Publicar no GitHub Pages

1. Crie um repositório **público** (Classroom da turma ou `ux-site` na sua conta).
2. Envie **esta pasta** como raiz do repositório (`index.html` na raiz, não dentro de outra pasta).
3. No GitHub: **Settings → Pages → Build and deployment**.
4. Source: **Deploy from a branch**. Branch: `main`. Pasta: `/ (root)`.
5. Espere até 10 minutos. O endereço fica:

   `https://SEU-USUARIO.github.io/NOME-DO-REPO/`

   (ou o da organização da Classroom).

O arquivo `.nojekyll` precisa ir junto. Ele manda o GitHub Pages servir os arquivos sem passar pelo Jekyll.

## Conferência rápida

- Cada página tem um `h1`.
- No celular, o menu continua usável e não há rolagem horizontal.
- O formulário tem rótulo visível em todos os campos.
- Contraste do texto e do botão permanece legível depois de mudar as cores.
