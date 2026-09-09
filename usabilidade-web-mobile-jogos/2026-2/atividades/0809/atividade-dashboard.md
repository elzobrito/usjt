# Atividade — Tornando o Dashboard funcional

## Objetivo

Completar a classe `Dashboard` para que todos os botões do menu executem uma ação. Utilize apenas os componentes, layouts, eventos e recursos visuais trabalhados em aula.

## Situação-problema

O sistema acadêmico já possui uma tela de login e um dashboard, mas somente o botão **Sair** funciona. Sua tarefa é implementar as ações restantes e melhorar o comportamento do menu.

## Requisitos obrigatórios

Implemente, no mínimo, as cinco ações abaixo:

1. **Alunos:** ao clicar, fechar o dashboard e abrir a tela `TelaCadastro`.
2. **Professores:** ao clicar, exibir uma mensagem informando que o módulo de professores foi selecionado.
3. **Turmas:** ao clicar, trocar o texto da área central para **Gerenciamento de turmas**.
4. **Relatórios:** ao clicar, solicitar uma confirmação antes de exibir a mensagem **Relatório gerado com sucesso**.
5. **Sair:** antes de fechar o dashboard, solicitar a confirmação do usuário. Se a resposta for positiva, fechar a janela e retornar para `TelaLogin`. Se for negativa, permanecer no dashboard.

## Regras

- Utilize eventos nos cinco botões.
- Mantenha o nome do usuário visível no dashboard.
- Use mensagens adequadas para informação, confirmação e sucesso.
- Não remova os botões nem altere os nomes apresentados no menu.
- O programa deve continuar funcionando caso o usuário cancele uma confirmação.

## Entrega

Entregue:

- o arquivo `Dashboard.java` atualizado;
- os demais arquivos necessários para executar o sistema;
- uma captura de tela do dashboard aberto;
- uma captura de tela mostrando pelo menos uma das novas ações funcionando.

## Critérios de avaliação — 10 pontos

| Critério |
|---|---:|
| Botão **Alunos** abre a tela correta |
| Botão **Professores** apresenta a mensagem solicitada |
| Botão **Turmas** atualiza a área central | 
| Botão **Relatórios** solicita confirmação e apresenta o resultado |
| Botão **Sair** confirma a ação e respeita a escolha do usuário |

## Desafio opcional

Altere a cor do botão selecionado para indicar visualmente qual módulo está ativo.
