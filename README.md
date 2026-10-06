# USJT — atividades de sala

Repositório comum das turmas do professor Elzo Brito na USJT. Cada matéria (UC) tem a sua pasta, e cada oferta fica dentro do semestre.

```text
<materia>/<AAAA-S>/atividades/<DDMM>/
```

- `<materia>`: pasta da UC (o padrão é um nome ASCII, sem acento e sem espaço);
- `<AAAA-S>`: ano e semestre, por exemplo `2026-2`;
- `atividades/`: o que você abre em aula (enunciados, HTML, código);
- `<DDMM>`: uma pasta por aula, com o **dia e o mês** da aula (`2408` = 24/08, `0510` = 05/10).

Apostilas, PDFs e slides (`.pdf`, `.pptx`, `.docx`, `.xlsx`) e bancos `.db` **não vão para o GitHub**: estão no `.gitignore`. Quando um README citar um desses arquivos, procure-o no link do Drive indicado pelo professor.

## Matérias

| Pasta | UC | Oferta 2026-2 |
|---|---|---|
| [usabilidade-web-mobile-jogos](usabilidade-web-mobile-jogos/) | Usabilidade, desenvolvimento web, mobile e jogos (0011109) | [10 aulas com material](usabilidade-web-mobile-jogos/2026-2/) |
| [Interação Humano Computador e UX](Intera%C3%A7%C3%A3o%20Humano%20Computador%20e%20UX/) | Interação Humano-Computador e UX | [3 aulas com material](Intera%C3%A7%C3%A3o%20Humano%20Computador%20e%20UX/2026-2/) |
| [gestao-qualidade-software](gestao-qualidade-software/) | Gestão da qualidade de software (0006960) | [cronograma e 5 pastas de aula](gestao-qualidade-software/2026-2/) |
| [gerencia-servicos-ti](gerencia-servicos-ti/) | Gerência e serviços de TI | pasta criada, ainda sem atividades |
| [modelos-metodos-engenharia-software](modelos-metodos-engenharia-software/) | Modelos, métodos e técnicas da engenharia de software | pasta criada, ainda sem atividades |

> A pasta `Interação Humano Computador e UX` tem espaços e acentos no nome. No terminal, use aspas: `cd "Interação Humano Computador e UX"`.

Outras pastas na raiz:

- `saves_074/`: progresso salvo pelo jogo de investigação `incidente_074.py` (IHC, aula 11/09). O programa cria essa pasta no diretório de onde é executado.
- `.github/`: arquivos de ferramenta do editor. Não é material de aula.

## O que você precisa instalar

Depende da aula; cada README diz o que usar. Em geral:

| Ferramenta | Usada em |
|---|---|
| Navegador (Chrome, Firefox, Edge) | páginas `.html` e sites estáticos |
| Python 3 + `pip install flask` | aplicações Flask (CRUD, carrinho) |
| Python 3 + `pip install pygame-ce` | jogo Snake |
| Python 3 com Tkinter (e `customtkinter` em um exemplo) | interfaces desktop em Python |
| JDK 11 ou mais novo (o material foi conferido com o JDK 21) | telas Swing/AWT e laboratórios Java |

Não existe `requirements.txt` neste repositório: instale os pacotes indicados no README da aula.

## Como o estudante usa

1. Clone o repositório ou baixe o ZIP.
2. Entre na pasta da **sua** matéria e do **seu** semestre.
3. Abra o `README.md` da oferta (por exemplo, `usabilidade-web-mobile-jogos/2026-2/README.md`). Ele lista as aulas em ordem e aponta para os arquivos.

## Como acrescentar uma atividade

1. Abra `<materia>/<AAAA-S>/atividades/` e crie a pasta da aula no formato `DDMM`.
2. Se a matéria ou o semestre ainda não existirem, crie a pasta no mesmo padrão.
3. Atualize o README da oferta e, se for oferta nova, o README da matéria e esta tabela.
