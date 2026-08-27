# Gabarito — laboratório Java/JUnit (docente)

Não projetar. Não imprimir para a turma.

## Defeitos na fatia didática

| Onde | Tipo | Efeito | Teste que pega |
|---|---|---|---|
| `regional == "NRA1"` | lógica | Com `new String("NRA1")` a busca não encontra | TODO 1 |
| `periodo.equals("2026/1")` | lógica | Período atual `2026/2` devolve lista vazia | teste de exemplo |
| `contar` sempre `3` | dados | Total não bate com a lista | TODO 2 |
| `for (i = 0; i <= length; i++)` | execução | `ArrayIndexOutOfBoundsException` | TODO 3 |

`==` com literal internado pode **passar**. Por isso o TODO 1 obriga `new String("NRA1")`. É o mesmo truque da Aula 02: a consulta que “funciona” no computador da gerência não é o caso geral.

## Parte 1 — teste de exemplo

Deve **falhar**: espera escolas em `2026/2`; o código só entra no `if` de `2026/1`. Não prova qualidade suficiente (Aula 02). Compilar também não prova.

## Parte 2 — testes esperados

```java
@Test
void regionalNaoInternadaNoPeriodoAtualDevolveTresEscolas() {
    List<String> escolas = consulta.buscar(new String("NRA1"), "2026/2");
    assertEquals(List.of("Etec São Paulo", "Etec Zona Leste", "Etec de Artes"), escolas);
}

@Test
void contarBateComTamanhoDaBusca() {
    assertEquals(
            consulta.buscar("NRA1", "2026/2").size(),
            consulta.contar("NRA1", "2026/2"));
    assertEquals(
            consulta.buscar("NRA1", "").size(),
            consulta.contar("NRA1", ""));
}

@Test
void listarLinhasNra1TemTresItensENaoLanca() {
    assertDoesNotThrow(() -> consulta.listarLinhas("NRA1"));
    assertEquals(3, consulta.listarLinhas("NRA1").size());
}
```

Com o código entregue, os três falham (ou o terceiro lança). Só depois disso a equipe pode corrigir `ConsultaEscolas`.

## Parte 3 — classificação

| # | Letra | Por quê |
|---|---|---|
| 1 | **P** | Resultado da função no código (produto). |
| 2 | **U** | Pessoa no contexto (teclado). JUnit desta fatia não mede isso. |
| 3 | **D** | Número publicado (total) não corresponde ao conjunto retornado. |

## Parte 4 — limite aceitável

Qualquer frase que recuse extrapolar para o sítio em produção, para LBI/eMAG, ou para “qualidade suficiente do BDGETEC”.

## Correção mínima do produto (opcional, depois dos testes)

- `Objects.equals(regional, "NRA1")` (ou `equals` com null-check).
- Comparar período com `PERIODO_ATUAL` (`2026/2`).
- `contar` retorna `buscar(...).size()`.
- Laço `i < escolas.length`.

## Ponte com a Aula 03

O JUnit é evidência de **produto**. O processo é: quem escreve o teste, quem vê a barra vermelha, quem autoriza a correção, onde o resultado fica guardado até o próximo período.
