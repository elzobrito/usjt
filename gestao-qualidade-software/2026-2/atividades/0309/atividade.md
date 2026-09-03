# Laboratório de Testes — Sistema de Desconto

## Objetivo

Nesta atividade, você irá analisar diferentes casos de teste para o método `aplicarDesconto`.

O objetivo é comparar:

- o resultado que você espera;
- o resultado produzido pelo programa;
- se o teste passou (`PASS`) ou falhou (`FAIL`).

Antes de executar o código, faça os cálculos no caderno.

---

## Código utilizado

```java
public class LaboratorioDesconto {

    static double aplicarDesconto(double valorOriginal, double percentual) {
        if (valorOriginal < 0) {
            throw new IllegalArgumentException(
                "O valor original não pode ser negativo."
            );
        }

        if (percentual < 0 || percentual > 100) {
            throw new IllegalArgumentException(
                "Percentual deve estar entre 0 e 100."
            );
        }

        return valorOriginal -
               (valorOriginal * (percentual / 100.0));
    }

    static boolean verificar(
        String nome,
        Object esperado,
        Object obtido
    ) {
        boolean passou =
            java.util.Objects.equals(esperado, obtido);

        System.out.println(
            (passou ? "PASS" : "FAIL")
            + " | " + nome
            + " | esperado=" + esperado
            + " | obtido=" + obtido
        );

        return passou;
    }

    static String mensagemDaExcecao(Runnable acao) {
        try {
            acao.run();
            return "(nenhuma exceção)";
        } catch (RuntimeException erro) {
            return erro.getMessage();
        }
    }

    static int codigoSaida(boolean... resultados) {
        for (boolean passou : resultados) {
            if (!passou) {
                return 1;
            }
        }

        return 0;
    }

    public static void main(String[] args) {

        // Os testes serão adicionados aqui.

    }
}
```

---

# Parte 1 — Calcule antes de executar

Para cada situação abaixo:

1. Faça o cálculo no caderno.
2. Escreva o resultado que você espera.
3. Depois execute o programa.
4. Compare o resultado esperado com o resultado obtido.

| Teste | Valor original | Desconto | Resultado esperado | Resultado obtido | PASS ou FAIL |
|---|---:|---:|---:|---:|---|
| 1 | 100,00 | 10% | | | |
| 2 | 200,00 | 25% | | | |
| 3 | 80,00 | 0% | | | |
| 4 | 50,00 | 100% | | | |
| 5 | 150,00 | 20% | | | |
| 6 | 300,00 | 50% | | | |
| 7 | 120,00 | 15% | | | |
| 8 | 80,00 | 12,5% | | | |
| 9 | 1000,00 | 1% | | | |
| 10 | 99,90 | 10% | | | |
| 11 | 0,00 | 30% | | | |

---

## Como calcular

Utilize:

```text
valor do desconto =
valor original × percentual / 100
```

Depois:

```text
valor final =
valor original - valor do desconto
```

Exemplo:

```text
Valor original: 200
Desconto: 15%

200 × 15 / 100 = 30

200 - 30 = 170
```

Portanto:

```text
Resultado esperado = 170
```

---

# Parte 2 — Crie os testes

Depois de fazer os cálculos no caderno, adicione os testes ao método `main`.

Utilize o seguinte formato:

```java
verificar(
    "descrição do teste",
    RESULTADO_ESPERADO,
    aplicarDesconto(VALOR, PERCENTUAL)
)
```

Exemplo:

```java
verificar(
    "10% de 100",
    90.0,
    aplicarDesconto(100.0, 10.0)
)
```

Crie testes para todas as situações da tabela anterior.

---

# Parte 3 — Entradas inválidas

Agora analise os seguintes casos:

| Teste | Valor original | Percentual | O que deveria acontecer? |
|---|---:|---:|---|
| 12 | 100,00 | 101% | |
| 13 | 100,00 | -10% | |
| 14 | -50,00 | 10% | |
| 15 | 100,00 | 150% | |

Para esses casos, não procure apenas um resultado numérico.

Pergunte:

> O sistema deveria aceitar essa entrada?

Quando considerar que a entrada é inválida, escreva no caderno:

```text
DEVE GERAR ERRO
```

Depois indique também qual mensagem você acredita que deveria aparecer.

---

# Parte 4 — Testando exceções

Para verificar situações inválidas, podemos utilizar o método:

```java
mensagemDaExcecao()
```

Exemplo:

```java
verificar(
    "percentual 150 deve ser rejeitado",
    "Percentual deve estar entre 0 e 100.",
    mensagemDaExcecao(
        () -> aplicarDesconto(100.0, 150.0)
    )
)
```

Crie testes semelhantes para:

```text
Percentual = 101

Percentual = -10

Valor original = -50
```

---

# Parte 5 — Descubra quais testes estão errados

Sem executar o programa primeiro, analise os testes abaixo.

Indique no caderno quais você acredita que produzirão:

```text
PASS
```

ou

```text
FAIL
```

### Teste A

```java
verificar(
    "10% de 100",
    90.0,
    aplicarDesconto(100.0, 10.0)
);
```

Resultado previsto:

```text
____________________
```

---

### Teste B

```java
verificar(
    "20% de 200",
    150.0,
    aplicarDesconto(200.0, 20.0)
);
```

Resultado previsto:

```text
____________________
```

---

### Teste C

```java
verificar(
    "50% de 80",
    40.0,
    aplicarDesconto(80.0, 50.0)
);
```

Resultado previsto:

```text
____________________
```

---

### Teste D

```java
verificar(
    "25% de 100",
    80.0,
    aplicarDesconto(100.0, 25.0)
);
```

Resultado previsto:

```text
____________________
```

---

### Teste E

```java
verificar(
    "5% de 200",
    190.0,
    aplicarDesconto(200.0, 5.0)
);
```

Resultado previsto:

```text
____________________
```

---

# Parte 6 — Execute e compare

Agora execute os testes.

Compare aquilo que você escreveu no caderno com o resultado do programa.

Exemplo de saída:

```text
PASS | 10% de 100 | esperado=90.0 | obtido=90.0

FAIL | 20% de 200 | esperado=150.0 | obtido=160.0
```

Responda:

1. Quais testes passaram?
2. Quais testes falharam?
3. Nos testes que falharam, o problema estava no programa ou no valor esperado pelo teste?
4. Um teste pode estar errado mesmo quando o programa está correto?
5. Um programa que executa sem apresentar erro necessariamente está correto?
6. Por que é importante testar valores próximos aos limites permitidos?

---

# Desafio

Crie pelo menos **5 novos casos de teste** que não aparecem nesta atividade.

Tente incluir:

- um valor muito alto;
- um desconto decimal;
- um desconto de `0%`;
- um desconto de `100%`;
- uma entrada inválida.

Registre cada caso no seguinte formato:

```text
Entrada:

Valor original:
Percentual:

Resultado esperado:

Resultado obtido:

PASS ou FAIL:

Justificativa:
```

---

# Reflexão final

Considere a seguinte afirmação:

> "O programa compilou e executou sem apresentar nenhum erro."

Isso é suficiente para afirmar que o software está correto?

Explique sua resposta no caderno.

---

## Conceitos trabalhados

Nesta atividade foram utilizados conceitos relacionados a:

- teste de software;
- caso de teste;
- entrada;
- saída esperada;
- saída obtida;
- `PASS`;
- `FAIL`;
- valores limite;
- tratamento de exceções;
- validação de entrada;
- defeitos de software;
- comparação entre resultado esperado e resultado obtido.

---

## Entrega

Entregue:

1. os cálculos realizados no caderno;
2. o código Java com os testes implementados;
3. as respostas das questões;
4. os cinco novos casos de teste criados no desafio.