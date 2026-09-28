# Estudo de Caso — SOS Usabilidade
## Painel de Registro de Problemas de Interface

---

**Disciplina:** Usabilidade, desenvolvimento web, mobile e jogos (0011109)  
**Aula:** 09 — Persistência com Python, Flask e SQLite  
**Modalidade:** Dupla (driver + navegador)  
**Duração estimada:** 200 minutos  
**Status:** ativo

---

## 1. Narrativa

A coordenação da disciplina de Usabilidade quer coletar, de forma sistemática,
os problemas de interface encontrados pelos próprios alunos em sistemas reais do
dia a dia — apps de banco, sistemas acadêmicos, e-commerces, plataformas de
streaming, redes sociais.

O problema: toda vez que alguém tenta usar uma planilha compartilhada para
registrar os achados, ela é sobrescrita, fica desatualizada ou simplesmente
**desaparece quando o computador fecha**.

Sua dupla foi escalada para construir o **SOS Usabilidade**: um painel web
Flask + SQLite onde qualquer membro da turma pode registrar, listar, atualizar
e remover problemas de usabilidade encontrados em sistemas reais.

A regra de ouro do cliente é clara:

> *"Se o servidor cair no meio da aula, eu quero que todos os problemas que
> a turma cadastrou continuem lá quando o sistema voltar."*

---

## 2. Missão da dupla

Construir uma aplicação Flask integrada a um banco SQLite local que satisfaça
os contratos e os testes de aceitação desta folha.

- Os dados devem persistir além do ciclo de vida do processo Flask.
- Todo comando SQL de escrita deve usar parâmetros `?` — concatenação de
  strings em SQL é **proibida**.
- Somente dados fictícios ou exemplos inventados; nenhum dado real de colega.
- O banco `problemas.db` não é distribuído pronto: **ele nasce durante a
  execução da dupla**.

---

## 3. Entidade central — `Problema de Usabilidade`

A dupla deve criar a tabela `problemas` respeitando as seguintes regras:

| Campo | Tipo | Regra |
|---|---|---|
| `id` | inteiro | chave primária, autoincremento |
| `titulo` | texto | obrigatório, máximo 120 caracteres |
| `sistema` | texto | obrigatório — nome do app ou site analisado |
| `categoria` | texto | obrigatório — um dos valores do vocabulário controlado abaixo |
| `gravidade` | texto | obrigatório — `baixa`, `media` ou `alta` |
| `descricao` | texto | obrigatório — relato objetivo do problema encontrado |
| `criado_em` | texto | preenchido automaticamente com data e hora da inserção |

**Vocabulário de categorias:**

```
navegacao | formulario | feedback | acessibilidade | outro
```

> **Decisão da dupla:** vocês escolhem se vão validar a categoria e a
> gravidade no Python ou via restrição SQL `CHECK`. Registrem a escolha e
> justifiquem.

---

## 4. Rotas que a aplicação deve ter

| Rota | Método | Responsabilidade |
|---|---|---|
| `/` | GET | Listar todos os problemas, ordenados do mais recente ao mais antigo |
| `/problemas` | POST | Receber e gravar um novo problema no banco |
| `/problemas/<id>/editar` | GET | Exibir formulário pré-preenchido com os dados do problema |
| `/problemas/<id>/editar` | POST | Aplicar a atualização de título, categoria, gravidade e descrição |
| `/problemas/<id>/excluir` | POST | Remover o problema pelo identificador |

> **Decisão da dupla:** vocês decidem se as rotas GET e POST de edição
> ficam em funções separadas ou na mesma função com lógica condicional.
> Registrem a escolha.

---

## 5. Contratos de comportamento

### 5.1 Banco e inicialização
- Arquivo `problemas.db` criado no mesmo diretório do script principal.
- A função de inicialização pode ser chamada mais de uma vez sem duplicar
  dados nem gerar erro.
- Toda conexão aberta deve ser fechada, inclusive em caso de erro.

### 5.2 GET `/`
- Retorna página válida mesmo quando o banco está vazio.
- Lista título, sistema, categoria, gravidade e data de criação de cada problema.
- Exibe problemas do mais recente para o mais antigo.

### 5.3 POST `/problemas`
- Remove espaços desnecessários (`strip()`) de todos os campos antes de
  qualquer validação.
- Recusa qualquer campo obrigatório em branco com mensagem textual explicativa.
- Recusa categoria fora do vocabulário controlado com mensagem textual.
- Recusa gravidade fora de `baixa | media | alta` com mensagem textual.
- Persiste o registro com commit antes de redirecionar.
- Após o cadastro, atualizar a página não repete a inserção (padrão PRG).

### 5.4 GET e POST `/problemas/<id>/editar`
- GET: carrega os dados atuais do banco e pré-preenche o formulário.
- POST: aplica as mesmas validações do cadastro antes de executar o UPDATE.
- Identificador inexistente produz resposta explícita (HTTP 404 ou mensagem
  de erro clara na tela).
- A alteração sobrevive ao reinício do servidor.

### 5.5 POST `/problemas/<id>/excluir`
- Executa `DELETE FROM problemas WHERE id = ?` com o identificador recebido.
- Identificador inexistente produz comportamento explícito e compreensível.
- A remoção sobrevive ao reinício do servidor.

### 5.6 Invariantes globais
- Nenhum valor de formulário é interpolado diretamente na string SQL.
- Somente dados fictícios no banco durante toda a aula.
- Servidor executado exclusivamente em `localhost` / `127.0.0.1`.
- Mensagens de sucesso e erro possuem **texto legível** — não apenas cor.

---

## 6. Tabela de testes de aceitação

Preencha **Previsto** antes de executar. Preencha **Obtido** depois.
Um teste que falha abre diagnóstico e reteste — não autoriza copiar solução.

| ID | Teste | Previsto | Obtido | Diagnóstico / correção | Reteste |
|---|---|---|---|---|---|
| T1 | Banco criado com `inicializar_banco()` duas vezes sem erro | | | | |
| T2 | GET `/` com banco vazio retorna página sem erro 500 | | | | |
| T3 | POST com título em branco recusa e exibe mensagem | | | | |
| T4 | POST com categoria inválida recusa e exibe mensagem | | | | |
| T5 | POST com gravidade inválida recusa e exibe mensagem | | | | |
| T6 | POST válido cadastra "App Banco — botão invisível" (gravidade alta) | | | | |
| T7 | GET `/` lista o problema cadastrado em T6 | | | | |
| T8 | POST com nome contendo aspas simples não quebra o SQL | | | | |
| T9 | Ctrl+C + reinício do Flask → problema de T6 ainda aparece | | | | |
| T10 | GET editar por ID existente exibe formulário pré-preenchido | | | | |
| T11 | POST editar altera a gravidade de `alta` para `media` | | | | |
| T12 | Alteração de T11 sobrevive ao reinício do servidor | | | | |
| T13 | POST excluir remove o registro pelo ID | | | | |
| T14 | POST excluir com ID inexistente produz resposta explícita | | | | |
| T15 | Remoção de T13 sobrevive ao reinício do servidor | | | | |

### Revisão cruzada (no mínimo T8, T9, T12 e T15)

O revisor **não lê o código primeiro**. Ele executa os testes, registra
uma divergência ou risco e só então pede que a dupla explique a decisão
correspondente.

---

## 7. Ciclo obrigatório para cada checkpoint

```
1. Escreva a previsão na tabela antes de qualquer execução.
2. Registre a decisão que a dupla tomou e por quê.
3. Implemente a menor mudança necessária para satisfazer o contrato.
4. Execute o teste.
5. Compare Previsto × Obtido.
6. Se divergir: diagnostique a causa, corrija e execute novamente.
7. Registre a evidência do reteste.
```

---

## 8. Checkpoints e papéis

**Driver:** escreve, executa e narra o raciocínio em voz alta.  
**Navegador:** confronta cada mudança com o contrato, preenche a tabela de
testes e impede que um teste seja pulado.

Troquem os papéis nos marcos abaixo:

| Marco | Quando trocar |
|---|---|
| Após T2 (banco criado, GET vazio ok) | Troca 1 |
| Após T9 (clímax do restart com cadastro) | Troca 2 |
| Após T15 (remoção persistida) | Troca 3 |

---

## 9. Decisões que precisam ser registradas e justificadas

Antes de implementar, a dupla anota a decisão. Depois, anota se mudou e por quê.

1. **Onde a conexão abre e fecha?**
   Dentro da função de rota, com `g` do Flask, ou com `closing`?

2. **Como validar categoria e gravidade?**
   Python com `if valor not in [...]` ou restrição `CHECK` no `CREATE TABLE`?

3. **Como tratar ID inexistente na edição e na exclusão?**
   `abort(404)` ou mensagem na página? Qual a diferença de UX para o usuário?

4. **Como o sistema informa sucesso e erro?**
   `flash()` com redirect, variável no template ou outro mecanismo?

5. **Como o usuário confirma uma exclusão?**
   Botão direto ou algum aviso antes? Justifique a decisão de UX.

---

## 10. Documentação

Documente o código fonte

## 11. Referências rápidas

- Use a aula do dia 21/09 como guia. 