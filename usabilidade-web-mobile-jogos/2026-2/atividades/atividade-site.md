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

O aluno **escolhe o negócio** (clínica, ONG, padaria, portfólio, oficina…). Troca tudo o que está entre `[colchetes]`.

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
