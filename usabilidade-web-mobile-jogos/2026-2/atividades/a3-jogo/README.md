# A3 – Desenvolvimento de um Jogo

**UC:** Usabilidade, desenvolvimento web, mobile e jogos · **Professor:** Elzo Brito dos Santos Filho
**Grupos:** até 6 integrantes · **Valor:** 10,0 pontos
**Entrega:** [preencher] · **Apresentação:** [preencher]

Enunciado em PDF: [A3-Jogo-enunciado.pdf](A3-Jogo-enunciado.pdf)

## 1. Objetivo

Desenvolver, em grupo, um jogo digital **original e jogável**, aplicando o que vimos na disciplina (Snake, Pong, Breakout e Space Invaders em pygame) e cuidando do que torna um jogo bom de jogar: **gráfico, jogabilidade, som, documentação e história**.

Ao final, o grupo deve conseguir:

- estruturar um jogo com laço principal (entrada, atualização, desenho), estados e regras claras;
- aplicar usabilidade à interface e aos controles (feedback, clareza, consistência);
- integrar imagens e sons respeitando licenças de uso;
- documentar o projeto para que outra pessoa instale, rode e entenda o jogo;
- apresentar o jogo funcionando e explicar as decisões tomadas.

## 2. Grupos

- Até 6 integrantes.
- Informe ao professor o nome do grupo, o nome provisório do jogo e os integrantes (nome completo e RA) até [preencher].
- Todos participam. A divisão de tarefas vai no README do projeto.
- Na apresentação, qualquer integrante pode ser chamado a explicar qualquer parte do jogo.

## 3. O que entregar

Um jogo original que possa ser jogado do início ao fim (ou até vitória ou derrota), com:

- instruções para instalar e rodar a partir do código-fonte;
- tela inicial, partida e tela de fim de jogo, com opção de jogar de novo ou voltar ao menu;
- pelo menos uma mecânica principal clara (pular, atirar, desviar, coletar, rebater) e uma condição de vitória ou derrota;
- pontuação, vidas, tempo ou outro indicador de progresso na tela;
- gráfico, som e história conforme a seção 4, e documentação conforme a seção 5.

### Tecnologia

- **Sugerida:** Python + pygame (`pip install pygame-ce`), a mesma base das aulas.
- **Outras são aceitas** (HTML5 Canvas, Phaser, Godot, Unity, Love2D, Kivy...) se o grupo justificar a escolha no README e o professor conseguir rodar o jogo seguindo as instruções.
- Bibliotecas e engines podem ser usadas, mas a lógica do jogo é escrita pelo grupo.

### O que é "jogo original"

- Pode partir de um gênero conhecido, mas precisa ter identidade própria: regras, fases, personagens, tema ou mecânica criados pelo grupo.
- **Não vale:** o Pong, Snake, Breakout ou Space Invaders da aula com mudanças mínimas (só cor ou velocidade), nem jogo copiado de tutorial, repositório ou vídeo.
- Partir de um jogo da aula é permitido se o resultado for claramente diferente (por exemplo, Pong com fases, chefes, power-ups, história e modo contra IA).

## 4. Critérios

### 4.1 Gráfico
Visual coerente com o tema, legível e consistente. Não precisa ser arte profissional, precisa ser cuidado.
- Sprites ou formas próprias para personagens, inimigos e objetos.
- Paleta consistente e bom contraste entre fundo, personagem e textos.
- HUD legível (pontos, vidas, tempo) sem cobrir a ação.
- Animação em pelo menos um elemento (andar em 2 a 4 quadros, explosão, piscar ao levar dano).
- Feedback visual nas ações (tremor ao colidir, partículas ao coletar).
- Menu, pausa e fim de jogo no mesmo estilo da partida.

### 4.2 Jogabilidade
O jogo funciona, é compreensível e tem desafio. É aqui que a usabilidade mais aparece.
- Controles responsivos e explicados dentro do jogo.
- Regras claras: o jogador entende como ganhar, perder e pontuar sem ler o código.
- Dificuldade que cresce com o tempo ou por fases.
- Colisões corretas.
- Pausa (P ou ESC) e reinício sem fechar o programa.
- Sem travamentos na apresentação.
- Contam a favor: 2 jogadores, IA de oponente, power-ups, recorde salvo em arquivo, opções de volume ou dificuldade.

### 4.3 Som
- Efeitos para as ações principais (pulo, tiro, colisão, coleta, dano, vitória, derrota).
- Música de fundo em loop, de preferência diferente no menu e na partida.
- Volume equilibrado e opção de silenciar (tecla M) ou ajustar.
- Sons de terceiros com fonte e licença nos créditos.
- Em pygame: `pygame.mixer.Sound` para efeitos e `pygame.mixer.music` para a trilha.

### 4.4 Documentação
- README organizado, com os itens obrigatórios da seção 5.
- Nomes de variáveis e funções claros e comentários nos trechos menos óbvios.
- Pastas separando código e assets (`src/`, `assets/img/`, `assets/sons/`).
- `requirements.txt` (ou equivalente).
- Capturas de tela ou GIF no README.

### 4.5 História
Precisa estar **dentro do jogo**, não só no README.
- **Premissa:** quem é o personagem, onde está, qual o objetivo.
- **Conflito:** o que impede o objetivo.
- **Apresentação:** tela de introdução, textos entre fases, falas ou cenário.
- **Desfecho:** finais de vitória e derrota coerentes.
- **Coerência:** mecânica, gráfico e som combinam com a história.

## 5. Itens obrigatórios do README do jogo

| # | Item | O que colocar |
|---|---|---|
| 1 | Identificação | Nome do jogo e do grupo, disciplina, professor, integrantes (nome e RA) |
| 2 | Descrição | Resumo de 3 a 5 linhas e a premissa da história |
| 3 | Como rodar | Pré-requisitos, instalação (`pip install -r requirements.txt`) e comando (`python main.py`). Testar em outro computador |
| 4 | Controles | Tabela com cada tecla e sua ação |
| 5 | Regras | Como ganhar, perder e pontuar |
| 6 | Divisão de tarefas | O que cada integrante fez |
| 7 | Créditos | Para cada imagem, fonte e som de terceiros: arquivo, autor, link e licença (CC0, CC-BY...). Indicar o que o grupo criou |
| 8 | Tecnologia | Linguagem e bibliotecas; se não for pygame, a justificativa |
| 9 | Uso de IA | Declaração obrigatória (ver seção 6). Se não usou, escrever "Não foi utilizada IA" |
| 10 | Capturas de tela | Pelo menos 2 imagens do jogo rodando |

## 6. Regras de autoria

- A lógica do jogo é escrita pelo grupo. Trechos curtos de documentação ou exemplos podem ser adaptados se forem indicados no código e no README.
- Assets de terceiros só com licença que permita o uso e com crédito. Asset sem fonte é tratado como não autorizado.
- **IA é permitida somente se declarada no README:** qual ferramenta, para quê e em quais arquivos. O grupo precisa saber explicar tudo o que foi gerado.
- IA não declarada é violação de autoria.
- **Cópia entre grupos zera a nota de todos os grupos envolvidos.**
- O professor pode pedir que qualquer integrante explique ou altere um trecho do código na apresentação.

## 7. Rubrica

Pesos iguais de 2,0 por critério (total 10,0). O professor pode ajustar os pesos e, se fizer isso, avisa a turma antes da entrega.

| Critério | Insuficiente (0 a 0,5) | Básico (0,6 a 1,0) | Bom (1,1 a 1,5) | Excelente (1,6 a 2,0) |
|---|---|---|---|---|
| **Gráfico** | Formas genéricas ou visual confuso; textos ilegíveis; sem menu ou fim | Simples mas legível; HUD presente; pouca consistência; sem animação | Coerente com o tema; HUD claro; telas no mesmo estilo; ao menos uma animação | Identidade marcante; várias animações; feedback visual nas ações; ótima legibilidade |
| **Jogabilidade** | Não roda ou trava; sem vitória ou derrota; controles não funcionam | Roda com uma mecânica; regras pouco claras; sem progressão; bugs visíveis | Controles explicados; regras claras; dificuldade cresce; pausa e reinício; poucos bugs | Bom de jogar e desafiador; sem bugs; extras (fases, power-ups, IA, 2 jogadores, recorde) |
| **Som** | Sem som ou sons sem crédito | Música ou poucos efeitos; volume desequilibrado | Música e efeitos nas ações principais; volume ok; créditos completos | Trilhas por tela; efeitos em todas as ações; opção de silenciar; som reforça a história |
| **Documentação** | README ausente ou sem como rodar | Tem como rodar e controles, mas faltam itens obrigatórios | Todos os itens da seção 5; instruções funcionam; pastas organizadas | Tudo do Bom, mais código comentado, capturas ou GIF e README fácil para qualquer pessoa |
| **História** | Sem história ou só no README | Premissa curta no jogo, sem ligação com as mecânicas | Premissa, conflito e desfecho no jogo, coerentes | Integrada (intro, textos entre fases, finais diferentes); tudo conta a mesma história |

## 8. Entrega e apresentação

**Arquivos (escolha uma opção):**
- Repositório (GitHub ou GitLab): enviar o link. Se for privado, dar acesso ao professor. Vale o conteúdo da data de entrega.
- `.zip` no Google Drive com o nome `A3_Jogo_NomeDoGrupo.zip`, compartilhado com o professor.

O pacote tem código-fonte, assets, arquivo de dependências e README. Não envie `venv` nem arquivos temporários.
Local de envio do link: [preencher].

**Apresentação:** [preencher data], [preencher] minutos por grupo, com o jogo rodando ao vivo.
Roteiro sugerido: história e objetivo, demonstração jogando, o que cada um fez, uma dificuldade técnica e como foi resolvida, uso de IA se houve.

## 9. Checklist do grupo

- [ ] Até 6 integrantes, todos no README com nome e RA
- [ ] Jogo original (não é o jogo da aula com mudanças mínimas)
- [ ] Abre, roda do início ao fim e não trava
- [ ] Tela inicial, partida e fim de jogo com opção de jogar de novo
- [ ] Vitória ou derrota e indicador de pontos, vidas ou tempo
- [ ] Controles explicados no jogo e no README
- [ ] Pausa e reinício funcionam
- [ ] Gráficos coerentes, HUD legível e ao menos uma animação
- [ ] Música e efeitos com volume equilibrado
- [ ] História aparece dentro do jogo (introdução e final)
- [ ] README com como rodar, controles, regras, divisão de tarefas, créditos, tecnologia e declaração de IA
- [ ] Todo asset de terceiros com autor, link e licença
- [ ] Tecnologia justificada se não for pygame
- [ ] Instruções testadas em outro computador
- [ ] Link enviado com acesso liberado ao professor
- [ ] Apresentação ensaiada, com todos sabendo explicar o código
