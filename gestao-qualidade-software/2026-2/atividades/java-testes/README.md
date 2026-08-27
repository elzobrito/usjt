# Laboratório Java/JUnit — consulta de escolas

Primeiro laboratório de testes automatizados da UC. Continua o caso BDGETEC da Aula 02 **sem** bater no sítio de produção.

## Quando usar

- **Não** na Aula 02 (papel e caneta).
- A partir da aula em que a turma tiver computador (Aula 03 ou a aula de testes/V&V).
- Ponte natural: o ticket da Parte 5 da Aula 02 (“qual processo produz essa evidência de novo?”) vira “escrever e rodar o JUnit”.

## O que já existia

| Artefato | Papel |
|---|---|
| `atividades/2008/main.java` + `busca_defeito_java.md` | Inspeção: achar defeito no código |
| este diretório | Evidência: um teste que **falha** quando o defeito existe |

## Como abrir

Java 17 ou superior. JUnit 5 via Maven.

```bash
cd consulta-escolas
mvn test
```

No IntelliJ / NetBeans / VS Code: abrir a pasta `consulta-escolas` (há `pom.xml`) e rodar a classe `ConsultaEscolasTest`.

O primeiro teste **deve falhar**: o período atual do caso é `2026/2` e o código compara com `2026/1`. Barra vermelha é o ponto de partida, não um erro de setup.

## Sequência sugerida em sala (50–70 min)

1. Lembrar a Aula 02: consulta que conclui ≠ qualidade suficiente.
2. Mostrar `ConsultaEscolas` no projetor (não o sítio).
3. Rodar o teste de exemplo → falha.
4. Alunos completam os TODOs do enunciado.
5. Classificar cada teste: P, U ou D. O percurso de teclado da LBI **não** entra neste JUnit.
6. Opcional: corrigir o código até a barra verde **depois** dos testes existirem.

## O que este laboratório não faz

- Não testa o menu Mapeamento nem teclado (qualidade em uso).
- Não autentica, não envia cookie, não chama `bdcgetec.cps.sp.gov.br`.
- Não substitui a Aula 03 de processos: o JUnit é o *artefato*; o processo é quem o gera, revisa e guarda.
