# Aula 03 — 03/09/2026 · Laboratório de testes: sistema de desconto

Nesta aula você testa o método `aplicarDesconto(valorOriginal, percentual)` comparando três coisas: o resultado que **você espera**, o resultado que o **programa produz** e se o teste deu `PASS` ou `FAIL`.

O programa é um **oráculo**: imprime uma linha `PASS`/`FAIL` por caso e termina com código de saída **0** se todos passaram ou **1** se algum falhou.

## Arquivos

| Arquivo | O que é |
|---|---|
| [atividade.md](atividade.md) | **Enunciado.** Partes 1 a 6, desafio, reflexão final e o que entregar |
| [LaboratorioDesconto.java](LaboratorioDesconto.java) | Código comentado: `aplicarDesconto`, o verificador `verificar(...)`, `mensagemDaExcecao(...)` e 5 casos de teste já prontos |
| [boolean.md](boolean.md) | Trecho Java do vetor `boolean[] resultados`, com casos normais para usar como modelo |
| [resultado.md](resultado.md) | Gabarito comentado das Partes 1 a 6 e do desafio |

## Como executar

Precisa do JDK 11 ou mais novo.

```bash
cd gestao-qualidade-software/2026-2/atividades/0309
javac LaboratorioDesconto.java
java LaboratorioDesconto
```

Para ver o código de saída depois de rodar:

- Linux/macOS: `echo $?`
- Windows (PowerShell): `echo $LASTEXITCODE`

Com o código como está, os 5 testes imprimem `PASS` e a saída é `0`.

## Roteiro da aula

1. **Parte 1:** calcule no caderno, **antes de executar**, o valor final de cada caso.
2. **Parte 2:** acrescente os seus casos ao vetor `resultados` no `main`.
3. **Parte 3:** pense em entradas inválidas (valor negativo, percentual fora de 0 a 100).
4. **Parte 4:** teste as exceções com `mensagemDaExcecao`.
5. **Parte 5:** descubra quais dos testes A a E estão errados: o defeito está no programa ou no valor esperado?
6. **Parte 6:** execute, compare e responda as questões.

Depois: desafio com cinco novos casos e a reflexão final.

## Entrega (conforme o enunciado)

1. Os cálculos feitos no caderno.
2. O código Java com os testes implementados.
3. As respostas das questões.
4. Os cinco novos casos de teste do desafio.
