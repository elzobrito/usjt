# Atividade A/B — Leitura de Código e Desenho de Interface

## 🎯 Objetivo

Dado o código-fonte da classe `ErgonomiaJava`, você deve ser capaz de:

- **Parte A** → Ler o código e entender como a interface é montada
- **Parte B** → Desenhar no caderno a interface que o código produz, **sem abrir o computador**

> Ao final, você executa o programa e compara seu desenho com a tela real.

---

## 📚 Conceitos que você precisa entender antes de ler o código

---

## 1. Como o Java/Swing organiza uma janela

Pense na janela como uma **folha dividida em regiões**. O `BorderLayout` define cinco zonas fixas:

```
┌─────────────────────────────┐
│           NORTH             │  ← barra de topo
├──────┬──────────────┬───────┤
│      │              │       │
│ WEST │    CENTER    │ EAST  │
│      │              │       │
├──────┴──────────────┴───────┤
│           SOUTH             │  ← rodapé
└─────────────────────────────┘
```

No código, você verá:
```java
frame.add(toolbar, BorderLayout.NORTH);   // toolbar vai para o topo
frame.add(center, BorderLayout.CENTER);   // center vai para o meio
frame.add(status, BorderLayout.SOUTH);    // status vai para o rodapé
```

---

## 2. O que é `CardLayout`

`CardLayout` funciona como um **baralho de cartas**:
- Vários painéis empilhados no mesmo espaço
- Apenas **um** fica visível por vez
- Você troca de carta chamando `cards.show(painel, "nome")`

No código:
```java
formCards.add(buildFormA(), "A");   // carta "A" = formulário de texto
formCards.add(buildFormB(), "B");   // carta "B" = formulário de listas
```

Quando o usuário seleciona a condição **A**, aparece o formulário de texto.
Quando seleciona **B**, aparece o formulário de listas.

---

## 3. O que é `GridBagLayout`

`GridBagLayout` organiza componentes em uma **grade invisível** de linhas e colunas.
Cada componente recebe coordenadas (`gridx`, `gridy`):

```
        gridx=0         gridx=1
gridy=0  [Prédio/código]  [____________]   ← JLabel + JTextField
gridy=1  [Categoria/cod]  [____________]
gridy=2  [Local/código ]  [____________]
gridy=3  [Descrição    ]  [____________]
```

No código, o método `addRow(panel, row, label, component)` faz exatamente isso:
- `gridx=0` → rótulo (`JLabel`)
- `gridx=1` → campo de entrada (`JTextField` ou `JComboBox`)

---

## 4. Componentes visuais usados

| Classe Java | O que aparece na tela |
|---|---|
| `JFrame` | A janela inteira |
| `JPanel` | Uma área invisível que agrupa outros componentes |
| `JLabel` | Um texto simples (não clicável) |
| `JTextField` | Uma caixinha para digitar texto |
| `JComboBox` | Uma lista suspensa para selecionar uma opção |
| `JRadioButton` | Um botão circular de seleção única |
| `JButton` | Um botão clicável |

---

## 5. O que é `ButtonGroup`

`ButtonGroup` agrupa `JRadioButton` para que **apenas um** possa estar selecionado:

```java
ButtonGroup modes = new ButtonGroup();
modes.add(modeA);   // "A — códigos"
modes.add(modeB);   // "B — reconhecimento"
```

Se o usuário clicar em B, o A é desmarcado automaticamente.

---

## 6. Como ler um `addActionListener`

Todo botão ou opção tem um `addActionListener` que define **o que acontece quando o usuário interage**:

```java
modeA.addActionListener(e -> showMode("A"));
//    ↑                       ↑
//  quando A for clicado    chama showMode("A")

confirm.addActionListener(e -> confirm());
//      ↑                      ↑
//  quando Confirmar for clicado   chama confirm()
```

Você **não precisa** entender o `lambda` (`e ->`) em detalhes agora.
O que importa é: **o que dispara** e **o que executa**.

---

## ✏️ PARTE A — Leia o código e responda no caderno

Responda **sem abrir o computador**.

---

### Questão A1 — Regiões da janela

O `frame` usa `BorderLayout`. Identifique o que vai para cada região:

| Região | O que é adicionado |
|---|---|
| `NORTH` | |
| `CENTER` | |
| `SOUTH` | |

> **Dica:** Procure as três linhas `frame.add(..., BorderLayout.XXX)` no método `buildUi()`.

---

### Questão A2 — Conteúdo do painel `toolbar`

Liste, **na ordem em que aparecem**, todos os componentes adicionados ao `toolbar`:

1. _______________
2. _______________
3. _______________
4. _______________

> **Dica:** Procure as chamadas `toolbar.add(...)`.

---

### Questão A3 — Formulário A

O método `buildFormA()` adiciona quatro campos de texto.
Complete a tabela:

| Linha (`row`) | Rótulo exibido | Tipo de componente |
|---|---|---|
| 0 | | |
| 1 | | |
| 2 | | |
| 3 | | |

---

### Questão A4 — Formulário B

O método `buildFormB()` adiciona quatro listas suspensas.
Para cada campo, escreva as opções disponíveis:

**Prédio:**
`[ ] ____________  [ ] ____________  [ ] ____________`

**Categoria:**
`[ ] ____________  [ ] ____________  [ ] ____________`

**Local:**
`[ ] ____________  [ ] ____________  [ ] ____________`

**Descrição:**
`[ ] ____________  [ ] ____________  [ ] ____________`

> **Dica:** Procure os arrays `new String[]{...}` dentro de `buildFormB()`.

---

### Questão A5 — Botões de ação

Quais dois botões ficam no painel `actions`?

1. _______________
2. _______________

---

### Questão A6 — Instruções exibidas

O método `showMode()` define o texto da `instruction`.
Escreva o texto que aparece para cada condição:

**Condição A:**

> _______________________________________________________________

**Condição B:**

> _______________________________________________________________

---

### Questão A7 — Status inicial

Qual é o texto do `status` quando a aplicação é iniciada?

> _______________________________________________________________

---

## ✏️ PARTE B — Desenhe no caderno

Com base nas respostas da Parte A, desenhe **dois esboços** no caderno:

---

### Esboço 1 — Interface com condição A selecionada

Use retângulos para representar cada componente.
Siga o modelo abaixo como ponto de partida:

```
┌──────────────────────────────────────────────────────┐
│  Ergonomia da interação — Java/Swing                 │  ← barra de título
├──────────────────────────────────────────────────────┤
│                                                      │
│  [NORTE — toolbar: escreva os componentes aqui]      │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [instrução: escreva o texto aqui]                   │
│                                                      │
│  ┌──── Registro interno ───────────────────────────┐ │
│  │                                                 │ │
│  │  [linha 0: rótulo]   [campo de entrada]         │ │
│  │  [linha 1: rótulo]   [campo de entrada]         │ │
│  │  [linha 2: rótulo]   [campo de entrada]         │ │
│  │  [linha 3: rótulo]   [campo de entrada]         │ │
│  │                                                 │ │
│  └─────────────────────────────────────────────────┘ │
│                                                      │
│  [botão 1]  [botão 2]                                │
│                                                      │
├──────────────────────────────────────────────────────┤
│  [SOUTH — status: escreva o texto inicial aqui]      │
└──────────────────────────────────────────────────────┘
```

Preencha:
- Os componentes do `toolbar` com seus rótulos reais
- O texto da instrução da condição A
- Os rótulos e tipos de campo do formulário A
- Os nomes dos botões de ação
- O texto do status inicial

---

### Esboço 2 — Interface com condição B selecionada

Repita o esboço, mas agora:
- O rádio **B — reconhecimento** está marcado
- O formulário mostra **listas suspensas** em vez de campos de texto
- O texto da instrução é o da condição B
- Dentro de cada lista, indique as opções disponíveis entre parênteses

**Exemplo de como representar uma lista suspensa:**

```
[▼ Prédio A | Prédio B | Prédio C]
```

---

## 💻 PARTE C — Verifique no computador

Após terminar os dois esboços:

1. **Compile e execute** o programa:

```bash
javac ErgonomiaJava.java
java ErgonomiaJava
```

2. **Compare** sua janela desenhada com a janela real.

3. **Responda no caderno:**

| Pergunta | Sua resposta |
|---|---|
| Quantos componentes você identificou corretamente no toolbar? | /4 |
| Os rótulos do formulário A estavam corretos? | Sim / Não |
| As opções das listas do formulário B estavam corretas? | Sim / Não |
| O texto da instrução da condição A estava correto? | Sim / Não |
| O que você não havia percebido ao ler o código? | |

---

## 🧠 Questão de reflexão (responda no caderno)

O programa implementa um experimento de **ergonomia cognitiva**:

- Na **condição A**, o usuário precisa **recordar e digitar** códigos como `74`, `K` e `19`.
- Na **condição B**, o usuário precisa apenas **reconhecer e selecionar** opções em listas.

Com base nisso, responda:

> **Qual das duas condições exige mais esforço mental do usuário? Por quê?**
> **O que acontece com esse esforço quando ocorre uma interrupção (botão "Simular interrupção")?**

---

## 🎯 Critérios de Avaliação

| Critério | Pontos |
|---|---|
| Parte A — 7 questões respondidas corretamente | 3,5 |
| Parte B — Esboço 1 com todos os componentes identificados | 2,5 |
| Parte B — Esboço 2 com listas e opções corretas | 2,5 |
| Parte C — Reflexão sobre ergonomia cognitiva | 1,5 |
| **Total** | **10,0** |

---

## 💡 Dica Final

> Ler código e visualizar a interface **sem executar** é uma das habilidades mais valiosas de um desenvolvedor.
> Ela permite revisar o trabalho de colegas, encontrar erros antes de compilar e entender sistemas legados muito mais rápido.