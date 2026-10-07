# Plano de Testes - Jogo Snake

**Aluno:** ______________________________________
**Turma:** ______________________________________
**Data:** ****/****/______

## 1. Objetivo

O objetivo deste teste é verificar se o jogo Snake funciona corretamente, garantindo que a movimentação da cobra, a geração da comida, o sistema de pontuação e as colisões estejam funcionando conforme o esperado.

---

## 2. Casos de Teste

### Teste 1 - Iniciar o jogo

**Passos:**

1. Executar o arquivo do jogo.
2. Observar a tela inicial.

**Resultado Esperado:**

- O jogo abre sem erros.
- A cobra aparece na tela com 3 partes.
- A pontuação inicia em 0.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 2 - Movimento automático

**Passos:**

1. Iniciar o jogo.
2. Não pressionar nenhuma tecla.

**Resultado Esperado:**

- A cobra deve se mover sozinha para a direita.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 3 - Movimento para cima

**Passos:**

1. Pressionar a tecla ↑.

**Resultado Esperado:**

- A cobra deve se mover para cima.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 4 - Movimento para baixo

**Passos:**

1. Pressionar a tecla ↓ enquanto a cobra estiver indo para a direita.

**Resultado Esperado:**

- A cobra deve se mover para baixo.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 5 - Movimento para esquerda

**Passos:**

1. Mover a cobra para cima.
2. Pressionar a tecla ←.

**Resultado Esperado:**

- A cobra deve se mover para a esquerda.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 6 - Movimento para direita

**Passos:**

1. Mover a cobra para cima.
2. Pressionar a tecla →.

**Resultado Esperado:**

- A cobra deve se mover para a direita.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 7 - Impedir inversão de direção

**Passos:**

1. Com a cobra indo para a direita, pressionar ←.

**Resultado Esperado:**

- A cobra deve continuar indo para a direita.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 8 - Comer a comida

**Passos:**

1. Levar a cobra até a comida.

**Resultado Esperado:**

- A comida desaparece.
- Outra comida aparece em uma nova posição.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 9 - Crescimento da cobra

**Passos:**

1. Comer uma comida.

**Resultado Esperado:**

- A cobra aumenta de tamanho.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 10 - Atualização da pontuação

**Passos:**

1. Comer uma comida.

**Resultado Esperado:**

- A pontuação aumenta em 10 pontos.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 11 - Aumento da velocidade

**Passos:**

1. Comer várias comidas.

**Resultado Esperado:**

- O jogo fica gradualmente mais rápido.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 12 - Colisão com a parede

**Passos:**

1. Conduzir a cobra até qualquer borda da tela.

**Resultado Esperado:**

- O jogo encerra.
- A tela de Game Over aparece.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 13 - Colisão com o próprio corpo

**Passos:**

1. Fazer a cobra crescer.
2. Fazer a cabeça encostar no corpo.

**Resultado Esperado:**

- A tela de Game Over deve aparecer.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 14 - Exibição da pontuação final

**Passos:**

1. Fazer pontos.
2. Perder o jogo.

**Resultado Esperado:**

- A pontuação final aparece na tela de Game Over.

**Status:** ( ) Aprovado ( ) Reprovado

---

### Teste 15 - Fechar o jogo

**Passos:**

1. Clicar no botão "X" da janela.

**Resultado Esperado:**

- O jogo fecha sem apresentar erros.

**Status:** ( ) Aprovado ( ) Reprovado

---

## 3. Problemas Encontrados

| Nº problema | Encontrado | Gravidade |
| --- | --- | --- |
|  1  | -   | -   |
|  2  | -   | -   |
|  3  | -   | -   |

NºProblema ---

## 4. Conclusão

Após a execução dos testes, foi possível verificar se as principais funcionalidades do jogo Snake estão funcionando corretamente. Foram avaliados os movimentos da cobra, o sistema de pontuação, o crescimento da cobra, as colisões e o encerramento do jogo. Caso todos os testes sejam aprovados, o jogo pode ser considerado apto para entrega e utilização pelos usuários.