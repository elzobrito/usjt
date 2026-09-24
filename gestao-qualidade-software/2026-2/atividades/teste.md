
## 2. Linha de Base e Escopo do MD Studio (Release v0.2.2)

A investigação técnica toma como referência o commit oficial `3fceeec` (versão 0.2.2):

### 2.1 Requisitos Funcionais Implementados

* **Editor:** CodeMirror 6 com numeração de linhas, quebra suave (*soft wrap*), desfazer/refazer e documento ativo único. Inclui barra de ferramentas Markdown e de tabela, comandos slash (`/`), *smart paste* (URLs sobre texto e conversão de tabelas HTML/Excel para Markdown), 7 modelos estruturados acessíveis via `Ctrl+N` e hub de formatação via IPC com fallback seguro.
* **Preview:** Pipeline Unified (CommonMark + GFM com tabelas, task lists, notas de rodapé e alertas), front matter YAML com validação de esquema, KaTeX local para equações matemáticas (sem requisições CDN externas), Shiki com temas claro/escuro, diagramas Mermaid com suporte a pan/zoom, alternância fonte/diagrama e exportação gráfica em SVG/PNG. Suporta modos *source*, *preview*, *split* sincronizado e *zen*. Outline de cabeçalhos navegável.
* **Workspace e Navegação:** Abertura de pastas e arquivos por diálogos nativos do sistema operacional, associação de arquivos `.md` em instância única, árvore de arquivos lateral, busca global no workspace, Quick Switcher (`Ctrl+P`), wiki links com preenchimento automático e resolução, backlinks sob demanda, links relativos no preview, abertura de links externos pelo navegador padrão, histórico de recentes e sessão mantida em `.mdstudio/index.json`.
* **Persistência:** Salvamento e *Salvar Como* atômicos, auto-save com debounce ativo por padrão, detecção de concorrência e conflitos por hash SHA-256 (com opções: *Recarregar*, *Manter local* ou *Salvar como*), watcher de disco com filtro de eco de auto-save e recuperação de rascunhos no `localStorage` por até 90 dias.
* **Exportação:** Geração de HTML autossuficiente pelo mesmo pipeline sanitizado de preview. Suporte a PDF através da impressão nativa do sistema operacional (`window.print()`). Exportação de blocos Mermaid para arquivos SVG ou PNG.
* **Plataformas:** Distribuição para Windows em instaladores oficiais NSIS (EXE) e MSI.



### 2.2 Requisitos Não Funcionais Críticos

* Arquitetura *local-first*, funcionamento offline, ausência de serviços de nuvem e sem telemetria em segundo plano.
* Acesso ao disco executado exclusivamente pelo backend em Rust via IPC tipado com contenção estrita no diretório do workspace (*path fencing*).
* Sanitização completa contra Cross-Site Scripting (XSS) no preview e na exportação HTML.
* Gravação atômica garantida por rotina de arquivo temporário, `fsync` e substituição renomeada (*atomic rename*).

### 2.3 Fronteiras e Recursos Fora de Escopo (Falsos Bugs)

* **Em Testes (fora da release 0.2.2):** O *Presentation Mode* (F5 / Reveal.js local) possui código inicial na árvore, mas está oficialmente agendado para a v0.2.3. Não deve ser reportado como defeito na v0.2.2.
* **Explicitamente fora do produto v1:** Edição visual WYSIWYG, colaboração concorrente em tempo real, sincronização em nuvem, sistema de plugins JavaScript externos, visualização em grafo de conhecimento, abas com múltiplos documentos simultâneos e gerador tipográfico avançado de PDF via Pandoc/LaTeX.

### 2.4 Divergências Conhecidas entre Documentação (PRD) e Implementação

1. **Drag-and-Drop:** O PRD prevê arrastar arquivos e pastas do Explorador do Windows diretamente para a janela, mas a interface implementa apenas abertura por diálogo nativo ou associação de extensão no sistema operacional.
2. **Modal de Conflito:** O PRD menciona um botão para *"Comparar"* versões conflitantes, contudo a interface real restringe-se a: *Recarregar*, *Manter local* e *Salvar como*.
3. **Faixa do Auto-Save:** A documentação especifica o atraso do auto-save na faixa de 1.000 a 5.000 ms, enquanto a validação no código e na interface aceita limites entre 500 e 10.000 ms.
4. **Política de Segurança (CSP):** O documento de qualidade prevê proibição estrita de `unsafe-eval`, enquanto a configuração real do runtime Tauri (`tauri.conf.json`) inclui `unsafe-eval` e `wasm-unsafe-eval`.

---

## 3. Matriz Consolidada de Métricas de Qualidade para o MD Studio

| Dimensão de Qualidade | Métrica / Indicador | Natureza | Instrumento / Fórmula de Cálculo | Critério e Interpretação Técnica |
| --- | --- | --- | --- | --- |
| **Desempenho (Tempo)** | Tempo de inicialização (*cold start*) | Dinâmica (Direta) | Cronômetro / Gerenciador de Tarefas | Tempo até a janela apresentar interface interativa a frio. |
| **Desempenho (Tempo)** | Tempo por tarefa operacional | Dinâmica (Direta) | Cronômetro (mediana das repetições da equipe) | Eficiência e fluidez dos fluxos básicos de trabalho. |
| **Eficiência de Recursos** | Consumo de memória RAM | Dinâmica (Direta) | Gerenciador de Tarefas (Processos do Windows) | Consumo em repouso e com `notas.md` aberto no editor. |
| **Capacidade de Carga** | Estabilidade sob carga (500 linhas) | Dinâmica (Direta) | Observação de fluidez e latência de rolagem | Atraso aceitável de sincronização do preview $\le 1{,}0\text{ s}$. |
| **Confiabilidade** | Integridade após salvar e reabrir | Dinâmica (Direta) | $\frac{\text{casos com divergência de texto}}{\text{total de casos executados}} \times 100$ | Manutenção exata do conteúdo persistido (meta: $0\%$ de perda). |
| **Conformidade Funcional** | Fidelidade da visualização | Dinâmica (Direta) | $\frac{\text{elementos renderizados corretamente}}{\text{total de elementos testados}} \times 100$ | Aderência do preview à sintaxe GFM, KaTeX e Mermaid (meta: $100\%$). |
| **Eficácia de Uso** | Taxa de conclusão da tarefa | Dinâmica (Indireta) | $\frac{\text{tarefas concluídas com sucesso}}{\text{total de tentativas}} \times 100$ | Capacidade do usuário de finalizar fluxos funcionais sem bloqueios. |
| **Operabilidade** | Erros ou bloqueios operacionais | Dinâmica (Direta) | Contagem de impasses, travamentos e falhas de comando | Identificação de pontos de atrito no fluxo de uso. |
| **Operabilidade** | Esforço mínimo de interação | Estática (Indireta) | Contagem de passos mínimos (cliques / atalhos) | Ergonomia de comandos e facilidade de navegação por teclado. |
| **Satisfação** | Usabilidade percebida | Subjetiva quantificada | Escala Likert de 1 a 5 (1: difícil; 5: fácil) | Percepção de conforto do usuário (indicador, não prova de defeito). |
| **Rigor de Investigação** | Taxa de reprodutibilidade | Metamétrica de Teste | $\frac{\text{repetições com mesma falha}}{\text{total de tentativas de repetição}}$ (ex.: 3 de 4) | Separação de anomalias efêmeras de comportamentos deterministas. |
| **Cobertura de Teste** | Cobertura do plano de teste | Métrica de Processo | $\frac{\text{casos de teste executados}}{\text{casos planejados}} \times 100$ | Extensão do plano coberta (100% não garante ausência de falhas). |


## Trilha 01: Editor, Formatação e Templates
- Requisito Base: CodeMirror 6 com numeração, soft wrap, slash commands (/), inserção de 7 templates via Ctrl+N e atalhos de formatação sem corrupção de blocos.
- Massa de Dados: Ficheiro limpo notas.md
