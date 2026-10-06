# 08/09 — Interfaces gráficas em Java (AWT e Swing)

Exemplos curtos de janelas em Java e um pequeno "sistema acadêmico" com login, dashboard e cadastro. A atividade da aula é **tornar o dashboard funcional**.

## Arquivos

Exemplos de introdução (cada um abre uma janela "Cadastro de usuários"):

| Arquivo | O que mostra |
|---|---|
| `CadastroUsuarios.java` | A janela AWT mais simples (`Frame`) |
| `CadastroUsuariosAwt.java` | AWT com título, campo "Nome" e botão "Cadastrar" |
| `CadastroUsuariosBtn.java` | Evento de clique: o botão "Clicar" muda o texto de um rótulo |
| `CadastroUsuariosSwing.java` | A mesma ideia em Swing (`JFrame`, `JLabel` ligado ao campo com `setLabelFor`) |

O sistema acadêmico:

| Arquivo | O que é |
|---|---|
| `TelaLogin.java` | Tela de login. Usuário `admin` e senha `123` abrem o dashboard |
| `Dashboard.java` | Menu com Alunos, Professores, Turmas, Relatórios e Sair. **Só o Sair funciona**: é o que você vai completar |
| `TelaCadastro.java` | Tela de cadastro com **7 erros marcados de propósito** (`// ERRO 1` a `// ERRO 7`). Do jeito que está, ela **não compila** (o ERRO 5 usa o listener errado no botão) |
| [atividade-dashboard.md](atividade-dashboard.md) | **Enunciado** da atividade, com o link do Drive no final |

## Como executar

Precisa do JDK 11 ou mais novo.

```bash
cd usabilidade-web-mobile-jogos/2026-2/atividades/0809
javac TelaLogin.java Dashboard.java
java TelaLogin
```

Os exemplos de introdução rodam sozinhos, por exemplo:

```bash
javac CadastroUsuariosSwing.java
java CadastroUsuariosSwing
```

`TelaCadastro.java` só compila depois que você corrigir os erros marcados. Isso é necessário para o botão **Alunos** do dashboard abrir essa tela.

## A atividade (resumo de `atividade-dashboard.md`)

Faça os cinco botões do `Dashboard` executarem uma ação:

1. **Alunos:** fecha o dashboard e abre a `TelaCadastro`.
2. **Professores:** mostra uma mensagem dizendo que o módulo de professores foi selecionado.
3. **Turmas:** troca o texto da área central para **Gerenciamento de turmas**.
4. **Relatórios:** pede confirmação antes de mostrar **Relatório gerado com sucesso**.
5. **Sair:** pede confirmação; se for "sim", fecha e volta para a `TelaLogin`; se for "não", continua no dashboard.

Regras: o nome do usuário continua visível, os botões não mudam de nome e o programa continua funcionando quando o usuário cancela uma confirmação.

**Entrega:** o `Dashboard.java` atualizado, os demais arquivos necessários para executar, uma captura do dashboard aberto e uma captura de pelo menos uma das novas ações.

**Desafio opcional:** mudar a cor do botão selecionado para indicar o módulo ativo.
