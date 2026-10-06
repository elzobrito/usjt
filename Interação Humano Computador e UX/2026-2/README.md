# Interação Humano-Computador e UX — 2026-2

Material de sala da oferta 2026-2. As aulas estão em `atividades/`, uma pasta por aula no formato **DDMM** (dia e mês).

O fio condutor é sempre o mesmo: **um programa que abre e funciona não é, só por isso, uma boa interface.** Você vai observar, registrar problemas com evidência e propor melhorias antes de mexer em código.

Materiais extras (slides, apostila): [atividades/materiais.md](atividades/materiais.md), com o link para a pasta do Drive.

## Aulas

| Pasta | Data | Tema | Formato |
|---|---|---|---|
| [atividades/2808](atividades/2808/) | 28/08 | Estudo de caso: achados e perdidos da universidade | grupo, caderno |
| [atividades/0409](atividades/0409/) | 04/09 | Caça aos problemas de uma interface de cadastro + redesenho | individual, caderno + computador |
| [atividades/1109](atividades/1109/) | 11/09 | Ergonomia cognitiva: ler código Swing, desenhar a tela e investigar o "Incidente 074" | caderno + computador |

---

## 28/08 — Achados e perdidos (`atividades/2808/`)

| Arquivo | O que é |
|---|---|
| `estudo-caso-achados-perdidos.md` | Enunciado completo do estudo de caso |

A universidade quer "um aplicativo" para o setor de achados e perdidos, que hoje funciona com cadernos em três prédios. Antes de escolher tecnologia, o grupo:

1. **Etapa 1:** entende o processo analógico (objetivo humano, pessoas, informações, esperas e erros, o que preservar);
2. **Etapa 2:** decide, elemento por elemento, o que fica analógico, o que vira digital, o que muda de processo e o que nem deveria ser coletado;
3. **Parecer do grupo:** responde se um aplicativo é mesmo a melhor saída e completa a síntese para a socialização.

Não há código nesta aula.

---

## 04/09 — Caça aos problemas da interface (`atividades/0409/`)

| Arquivo | O que é |
|---|---|
| `atividade problema.md` | Enunciado: Parte 1 (registrar problemas) e Parte 2 (redesenhar a janela no caderno) |
| `CadastroUsuariosComProblemas.java` | **A tela da atividade.** Cadastro de usuários em Swing com problemas de propósito |
| `CadastroUsuarios.java` | Exemplo mínimo comentado: uma janela AWT vazia que fecha corretamente |
| `CadastroUsuariosJanela.java` | Outra versão do cadastro em Swing, com visual Nimbus, botões e painéis arredondados |
| `cadastro_usuarios.py` | Versão do cadastro em Python com `customtkinter` (cadastrar, excluir, mensagens de sucesso e erro) |
| `TelaLogin.java` | Tela de login em Swing (usuário, senha e botão Entrar com mensagens) |

### Como executar

Java (precisa do JDK 11 ou mais novo):

```bash
cd "Interação Humano Computador e UX/2026-2/atividades/0409"
javac CadastroUsuariosComProblemas.java
java CadastroUsuariosComProblemas
```

Troque o nome da classe para abrir os outros exemplos (`CadastroUsuarios`, `CadastroUsuariosJanela`, `TelaLogin`).

Python (precisa do Tkinter e do pacote `customtkinter`):

```bash
pip install customtkinter
python cadastro_usuarios.py
```

> No Linux, se aparecer `No module named 'tkinter'`, instale o pacote do sistema (por exemplo, `sudo apt install python3-tk`).

### O que entregar no caderno

- A tabela de problemas (o enunciado traz 10 linhas): o problema, a consequência, a categoria (funcionalidade, usabilidade, acessibilidade, aparência, validação ou outra) e a solução proposta.
- O desenho da nova janela de **Cadastro de usuários** e a justificativa de pelo menos 5 alterações.
- As duas questões de reflexão do enunciado.

---

## 11/09 — Ergonomia cognitiva (`atividades/1109/`)

| Arquivo | O que é |
|---|---|
| `Atividade A/B .md` | Enunciado da atividade de leitura de código (dentro da pasta `Atividade A/`, arquivo `B .md`) |
| `ErgonomiaJava.java` | Programa Swing analisado na atividade: formulário com as condições **A — códigos** e **B — reconhecimento** |
| `ergonomia.py` | A mesma prática em Python/Tkinter, sem gravar nada |
| `incidente_074.py` | Investigação em 12 telas, no terminal: um guarda-chuva azul foi registrado no prédio errado |
| `incidente_074_web.html` | Versão para navegador da mesma investigação |

### Atividade A/B — ler o código e desenhar a tela

1. **Parte A:** leia `ErgonomiaJava.java` e responda as questões A1 a A7 no caderno, **sem abrir o computador**. O enunciado explica antes `BorderLayout`, `CardLayout`, `GridBagLayout`, `ButtonGroup` e `addActionListener`.
2. **Parte B:** desenhe dois esboços da tela, um com a condição A e outro com a condição B.
3. **Parte C:** execute o programa e compare com o seu desenho.

```bash
cd "Interação Humano Computador e UX/2026-2/atividades/1109"
javac ErgonomiaJava.java
java ErgonomiaJava
```

Versão em Python: `python ergonomia.py`.

Os dois programas têm um teste automático rápido: `java ErgonomiaJava --smoke-test` e `python ergonomia.py --smoke-test`.

### Incidente 074 — investigação em dupla

No terminal:

```bash
python incidente_074.py          # abre (nova investigação ou continua a salva)
python incidente_074.py --novo   # força uma investigação nova
python incidente_074.py --teste  # teste automático
```

O progresso de cada equipe fica em `saves_074/<equipe>.json`, criado na pasta de onde você rodou o comando.

No navegador: abra `incidente_074_web.html` com duplo clique. Essa versão guarda o progresso da equipe no próprio navegador (`localStorage`); se trocar de computador ou de navegador, o progresso não vai junto.
