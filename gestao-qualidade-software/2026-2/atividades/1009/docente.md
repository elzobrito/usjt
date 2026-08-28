# Aula 04 — Folha docente

## Decisão didática

Bartié é a fonte principal. A aula adapta o percurso de verificação dos capítulos 8–10 para uma revisão de código curta: foco, questão, discussão, confirmação, registro e continuidade. O capítulo 11 fornece a ponte para a validação com execução.

Não diga “teste é sempre dinâmico” como definição universal; interprete FAIL como divergência observada, não como conclusão automática. PASS e FAIL são resultados úteis quando existe um oráculo; ambos exigem interpretação e têm alcance limitado.

## Relógio de 200 minutos

| Min | Ação |
|---|---|
| 0–10 | Problema: onde mora o FAIL? |
| 10–25 | Bartié: verificar antes de executar |
| 25–40 | Demonstração de uma hipótese rastreável |
| 40–90 | Revisão estática das cinco funções |
| 90–110 | Validação dinâmica dos cinco casos |
| 110–120 | Oráculo independente para `contar` |
| 120–140 | Intervalo |
| 140–180 | Recuperação e conferência cruzada |
| 180–195 | Ticket individual |
| 195–200 | Fechamento e ponte para níveis de teste |

## Gabarito — não projetar

| Tópico | Defeito no artefato | Efeito observado esperado nesta versão |
|---|---|---|
| `buscar` | compara o período com `2026/1` | lista vazia e FAIL em `2026/2` |
| `contar` | ignora a consulta e retorna `3` | regional `XXX` também produz `3` |
| `listar` | laço aceita índice igual ao tamanho | exceção após as três linhas |
| normalização | comparação literal, sem retirar espaços ou normalizar caixa | `NRA1` retorna 3; variantes retornam 0 em `2026/1` |
| `ativas` | devolve sempre a lista completa | `XXX` ainda recebe três escolas |

## Oráculo independente

```text
obtido = contar("XXX", "2026/2")
esperado = 0
resultado = PASS se obtido == esperado; senão FAIL
```

A saída atual é FAIL porque `3 != 0`. Não compare com `buscar`: o erro de período em `buscar` poderia desaparecer depois, e duas funções defeituosas podem concordar em outros cenários.

## Intervenções rápidas

- “Está errado.” → “Qual critério? Qual fragmento? Qual efeito você prevê?”
- “Deu PASS, então está certo.” → “Qual entrada passou? Quais entradas não foram examinadas?”
- “Deu FAIL, encontramos a causa.” → “FAIL mostra divergência. Que evidência localiza a causa?”
- “Vou corrigir agora.” → “Preserve a evidência. A correção começa com FAIL na aula de TDD.”
- “Buscar confirma contar.” → “Quem valida buscar? Volte ao requisito da regional inexistente.”

## Corte se houver atraso

Reduza a conferência cruzada de 140–180. Não corte a revisão estática, os cinco casos, o oráculo independente ou o ticket.
