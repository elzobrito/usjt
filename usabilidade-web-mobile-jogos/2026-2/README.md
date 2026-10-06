# Usabilidade, desenvolvimento web, mobile e jogos — 2026-2

Material de sala da UC **0011109**. Não é um sistema pronto: é uma sequência de atividades que começa em **IHC** e em **HTML e CSS**, passa por **rotas HTTP** e **interfaces Java**, e chega a aplicações **Flask + SQLite** e a um jogo em **Pygame**.

As aulas ficam em `atividades/`, uma pasta por aula no formato **DDMM** (dia e mês: `2408` = 24/08).

## Mapa das aulas

| Pasta | Data | Tema | Ferramentas |
|---|---|---|---|
| [2408](atividades/2408/) | 24/08 | IHC no cotidiano; quebra-cabeças "Consulta de escolas"; site no GitHub Pages (layout-contrato) | navegador, GitHub |
| [2508](atividades/2508/) | 25/08 | Arquivo, GET e POST não são a mesma coisa: rotas do seu site | caderno |
| [3108](atividades/3108/) | 31/08 | CRUD de usuários em Flask, construído em etapas (dados em memória) | Python + Flask |
| [0109](atividades/0109/) | 01/09 | Aula 07: wireframes em papel e ficha-contrato da reserva | papel |
| [0809](atividades/0809/) | 08/09 | Interfaces Java (AWT/Swing): login, dashboard e cadastro com erros | JDK |
| [2109](atividades/2109/) | 21/09 | CRUD de usuários em Flask com SQLite (os dados ficam salvos) | Python + Flask |
| [2209](atividades/2209/) | 22/09 | Cadastrar os produtos do seu site com SQLite; lista dos 155 negócios | Python + Flask |
| [2809](atividades/2809/) | 28/09 | Estudo de caso "SOS Usabilidade": Flask + SQLite em dupla | Python + Flask |
| [2909](atividades/2909/) | 29/09 | Jogo Snake em Python | Python + pygame-ce |
| [0510](atividades/0510/) | 05/10 | Carrinho de compras com Flask + SQLite | Python + Flask |

### Como as aulas se ligam

```text
2408 site estático (HTML+CSS) ──► 2508 rotas: o que o botão "Enviar" deveria fazer
        └──────────────────────► 0109 wireframes do recurso principal do seu site

3108 CRUD em memória ──► 2109 CRUD com SQLite ──┬──► 2209 produtos do seu site no SQLite
                                                └──► 2809 SOS Usabilidade (o enunciado usa 21/09 como guia)

0510 carrinho de compras: Flask + SQLite com vitrine e carrinho (cadastro de produtos em construção)
```

O HTML do CRUD final de 31/08 (`3108/final/crud_usuarios.html`) é o mesmo de 21/09 (`2109/site/crud_usuarios.html`). O que muda é o `main.py`: a lista em memória vira a tabela `usuarios` no SQLite, e a API JSON passa de `/usuarios` para `/api/usuarios`.

## Preparar o computador

- **Páginas HTML:** basta abrir o arquivo no navegador (duplo clique ou arrastar para o Chrome/Firefox).
- **Flask:** Python 3 e o pacote Flask. Não há `requirements.txt`; instale assim:

  ```bash
  python -m venv .venv
  # Windows:      .venv\Scripts\activate
  # Linux/macOS:  source .venv/bin/activate
  pip install flask
  ```

  Ao rodar o app, abra `http://127.0.0.1:5000/` no navegador. Para parar o servidor: `Ctrl+C`.
- **Snake:** `pip install pygame-ce` (o código usa `import pygame`).
- **Java:** JDK 11 ou mais novo (`javac` e `java` no terminal).

---

## 24/08 — IHC, HTML e o site no GitHub Pages (`atividades/2408/`)

| Arquivo | O que é |
|---|---|
| [atividade1.md](atividades/2408/atividade1.md) | Atividade 1 — mapeamento da IHC em um sistema que você já usa (30 min, plano B de 20 min) |
| [codigo.html](atividades/2408/codigo.html) | Quebra-cabeça 1 — a tela mente |
| [cpdogp2.html](atividades/2408/cpdogp2.html) | Quebra-cabeça 2 — a lista está na página |
| [codigo3.html](atividades/2408/codigo3.html) | Quebra-cabeça 3 — parece certo no papel |
| [atividade-site.md](atividades/2408/atividade-site.md) | Enunciado do site no GitHub Pages, critérios e a lista dos 155 negócios |
| [site-padrao/](atividades/2408/site-padrao/) | Layout-contrato do site (HTML + CSS, sem JavaScript). Tem o próprio [README](atividades/2408/site-padrao/README.md) |
| `site-padrao.zip` | O mesmo layout compactado, para baixar de uma vez |
| [redesenho.md](atividades/2408/redesenho.md) | Redesenhar no papel as telas do site-padrão e simular a navegação com outra equipe |
| [ficha_evidencias_grupo.md](atividades/2408/ficha_evidencias_grupo.md) | Mapa de decisões do grupo: antes, durante e depois de construir o site |
| `router.php` | Classe de roteador em PHP (`OliviaRouter\Router`) para ler como exemplo de rotas `get`/`post` |
| `html.pdf` | Apostila de HTML (só na cópia local e no Drive; não vai para o GitHub) |

**Atividade 1 (IHC):** individual. Escolha um sistema que você **já usa**, não um sistema ideal, e avalie as qualidades de uso com evidência na interface. Não exponha dados da sua conta.

**Quebra-cabeças "Consulta de escolas":** a tela pedida tem o título **Consulta de escolas**, uma caixa **Núcleo Regional** e uma caixa **Período**. Abra os três `.html` nesta ordem; há erros de propósito. Em cada rodada, circule o problema, diga o que quebra na tela e proponha o conserto em uma linha. Tese da aula: o HTML estrutura e o CSS veste, mas nenhum dos dois fabrica a lista do Período.

**Site no GitHub Pages:** copie `site-padrao/`, troque os textos entre `[colchetes]`, altere só o `:root` das cores e publique a pasta como raiz do repositório. Layout travado; sem JavaScript.

## 25/08 — Rotas: arquivo, GET e POST (`atividades/2508/`)

| Arquivo | O que é |
|---|---|
| [atividade.md](atividades/2508/atividade.md) | Tabela de correlação: para cada situação (link do menu, formulário, `fetch`, URL colada), qual pedido HTTP o navegador monta e qual rota R1–R6 responde, ou "nenhuma" |
| [atividade-rotas.md](atividades/2508/atividade-rotas.md) | Com o **seu** site: arquivo da tela × pedido de página × criação no sistema; a ação que o botão promete; a tabela de rotas com substantivos do domínio (`/orcamentos`, `/reservas`…) |

Atividade de caderno, sem código.

## 31/08 — CRUD em Flask, passo a passo (`atividades/3108/`)

Cinco etapas, da variável ao CRUD completo com API JSON. Veja o [README da pasta](atividades/3108/README.md).

## 01/09 — Aula 07: o contrato da reserva (`atividades/0109/`)

| Arquivo | O que é |
|---|---|
| [aluno.md](atividades/0109/aluno.md) | Enunciado: três wireframes em papel (pedido, depois do envio, lista de quem atende), protótipo de papel e ficha-contrato (substantivo, campos, rotas, papéis e estados) |

Sem Flask, sem Canva e sem HTML novo: o que estiver na foto da mesa no fim da aula é o que entra no código depois.

## 08/09 — Interfaces Java (`atividades/0809/`)

Login → dashboard → cadastro, com uma atividade para tornar o dashboard funcional. Veja o [README da pasta](atividades/0809/README.md).

## 21/09 — CRUD com SQLite (`atividades/2109/`)

O CRUD da aula 31/08, agora gravando em `usuarios.db`. Veja o [README da pasta](atividades/2109/README.md).

## 22/09 — Produtos do seu site no SQLite (`atividades/2209/`)

| Arquivo | O que é |
|---|---|
| [links.md](atividades/2209/links.md) | A tarefa ("cadastre os produtos disponíveis no seu site usando SQLite"), a lista dos 155 negócios por categoria e os links do Drive (CRUD em Python, site padrão, mockup, CRUD com SQLite) |

Use o [CRUD com SQLite de 21/09](atividades/2109/) como ponto de partida.

## 28/09 — Estudo de caso SOS Usabilidade (`atividades/2809/`)

| Arquivo | O que é |
|---|---|
| [atividade-python-sqlite.md](atividades/2809/atividade-python-sqlite.md) | Enunciado: painel Flask + SQLite para registrar problemas de usabilidade. Traz a entidade, as rotas, os contratos, os testes de aceitação, os checkpoints e as decisões a justificar |
| `wireframe-sos-usabilidade.html` | Wireframe das telas; abra no navegador |

Em dupla (driver + navegador). Rotas pedidas: `GET /`, `POST /problemas`, `GET` e `POST /problemas/<id>/editar` e `POST /problemas/<id>/excluir`. O próprio enunciado indica a [aula de 21/09](atividades/2109/) como guia.

## 29/09 — Jogo Snake (`atividades/2909/`)

Veja o [README da pasta](atividades/2909/README.md). Materiais extras em [link.md](atividades/2909/link.md) (Drive).

## 05/10 — Carrinho de compras com Flask + SQLite (`atividades/0510/`)

Vitrine lida do banco, carrinho gravado no SQLite e três atividades de extensão. Veja o [README da pasta](atividades/0510/README.md).

---

## Para quem conduz a aula

- Não projetar gabarito no começo dos votos.
- Os enunciados com gabarito ficam fora deste repositório (caderno da disciplina), para o estudante clonar o GitHub sem a resposta.
- Amostrar 3–4 mapas da Atividade 1 em sala; o restante pelo canal da disciplina.
