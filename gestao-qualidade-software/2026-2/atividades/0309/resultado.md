# Gabarito — Laboratório de Testes: Sistema de Desconto

## Parte 1 — Cálculos antes da execução

A fórmula utilizada pelo programa é:

```text
valor do desconto = valor original × percentual / 100

valor final = valor original - valor do desconto
```

### Teste 1 — 10% de 100

```text
100 × 10 / 100 = 10

100 - 10 = 90
```

Resultado esperado:

```text
90,00
```

---

### Teste 2 — 25% de 200

```text
200 × 25 / 100 = 50

200 - 50 = 150
```

Resultado esperado:

```text
150,00
```

---

### Teste 3 — 0% de 80

```text
80 × 0 / 100 = 0

80 - 0 = 80
```

Resultado esperado:

```text
80,00
```

---

### Teste 4 — 100% de 50

```text
50 × 100 / 100 = 50

50 - 50 = 0
```

Resultado esperado:

```text
0,00
```

---

### Teste 5 — 20% de 150

```text
150 × 20 / 100 = 30

150 - 30 = 120
```

Resultado esperado:

```text
120,00
```

---

### Teste 6 — 50% de 300

```text
300 × 50 / 100 = 150

300 - 150 = 150
```

Resultado esperado:

```text
150,00
```

---

### Teste 7 — 15% de 120

```text
120 × 15 / 100 = 18

120 - 18 = 102
```

Resultado esperado:

```text
102,00
```

---

### Teste 8 — 12,5% de 80

```text
80 × 12,5 / 100 = 10

80 - 10 = 70
```

Resultado esperado:

```text
70,00
```

---

### Teste 9 — 1% de 1000

```text
1000 × 1 / 100 = 10

1000 - 10 = 990
```

Resultado esperado:

```text
990,00
```

---

### Teste 10 — 10% de 99,90

```text
99,90 × 10 / 100 = 9,99

99,90 - 9,99 = 89,91
```

Resultado esperado:

```text
89,91
```

---

### Teste 11 — 30% de 0

```text
0 × 30 / 100 = 0

0 - 0 = 0
```

Resultado esperado:

```text
0,00
```

---

## Tabela preenchida

| Teste | Valor original | Desconto | Resultado esperado | Resultado obtido | PASS ou FAIL |
| ----- | -------------: | -------: | -----------------: | ---------------: | ------------ |
| 1     |         100,00 |      10% |              90,00 |            90,00 | PASS         |
| 2     |         200,00 |      25% |             150,00 |           150,00 | PASS         |
| 3     |          80,00 |       0% |              80,00 |            80,00 | PASS         |
| 4     |          50,00 |     100% |               0,00 |             0,00 | PASS         |
| 5     |         150,00 |      20% |             120,00 |           120,00 | PASS         |
| 6     |         300,00 |      50% |             150,00 |           150,00 | PASS         |
| 7     |         120,00 |      15% |             102,00 |           102,00 | PASS         |
| 8     |          80,00 |    12,5% |              70,00 |            70,00 | PASS         |
| 9     |        1000,00 |       1% |             990,00 |           990,00 | PASS         |
| 10    |          99,90 |      10% |              89,91 |            89,91 | PASS         |
| 11    |           0,00 |      30% |               0,00 |             0,00 | PASS         |

---

# Parte 2 — Implementação dos testes

Os testes podem ser adicionados ao método `main` da seguinte forma:

```java
public static void main(String[] args) {

    boolean[] resultados = {

        verificar(
            "10% de 100",
            90.0,
            aplicarDesconto(100.0, 10.0)
        ),

        verificar(
            "25% de 200",
            150.0,
            aplicarDesconto(200.0, 25.0)
        ),

        verificar(
            "0% de 80",
            80.0,
            aplicarDesconto(80.0, 0.0)
        ),

        verificar(
            "100% de 50",
            0.0,
            aplicarDesconto(50.0, 100.0)
        ),

        verificar(
            "20% de 150",
            120.0,
            aplicarDesconto(150.0, 20.0)
        ),

        verificar(
            "50% de 300",
            150.0,
            aplicarDesconto(300.0, 50.0)
        ),

        verificar(
            "15% de 120",
            102.0,
            aplicarDesconto(120.0, 15.0)
        ),

        verificar(
            "12.5% de 80",
            70.0,
            aplicarDesconto(80.0, 12.5)
        ),

        verificar(
            "1% de 1000",
            990.0,
            aplicarDesconto(1000.0, 1.0)
        ),

        verificar(
            "10% de 99.90",
            89.91,
            aplicarDesconto(99.90, 10.0)
        ),

        verificar(
            "30% de zero",
            0.0,
            aplicarDesconto(0.0, 30.0)
        )
    };

    System.exit(codigoSaida(resultados));
}
```

---

# Parte 3 — Entradas inválidas

Agora não estamos apenas verificando o cálculo.

Estamos verificando se o programa rejeita dados que não deveriam ser aceitos.

## Teste 12

Entrada:

```text
Valor original: 100
Percentual: 101%
```

O percentual permitido deve estar entre `0` e `100`.

Portanto:

```text
DEVE GERAR ERRO
```

Mensagem esperada:

```text
Percentual deve estar entre 0 e 100.
```

---

## Teste 13

Entrada:

```text
Valor original: 100
Percentual: -10%
```

Um percentual negativo não é permitido.

Portanto:

```text
DEVE GERAR ERRO
```

Mensagem esperada:

```text
Percentual deve estar entre 0 e 100.
```

---

## Teste 14

Entrada:

```text
Valor original: -50
Percentual: 10%
```

O valor original não pode ser negativo.

Portanto:

```text
DEVE GERAR ERRO
```

Mensagem esperada:

```text
O valor original não pode ser negativo.
```

---

## Teste 15

Entrada:

```text
Valor original: 100
Percentual: 150%
```

O percentual ultrapassa o limite máximo permitido.

Portanto:

```text
DEVE GERAR ERRO
```

Mensagem esperada:

```text
Percentual deve estar entre 0 e 100.
```

---

## Tabela preenchida

| Teste | Valor original | Percentual | O que deveria acontecer?          |
| ----- | -------------: | ---------: | --------------------------------- |
| 12    |         100,00 |       101% | Deve gerar erro de percentual     |
| 13    |         100,00 |       -10% | Deve gerar erro de percentual     |
| 14    |         -50,00 |        10% | Deve gerar erro de valor original |
| 15    |         100,00 |       150% | Deve gerar erro de percentual     |

---

# Parte 4 — Testando as exceções

Os testes podem ser escritos assim:

```java
verificar(
    "percentual 101 deve ser rejeitado",
    "Percentual deve estar entre 0 e 100.",
    mensagemDaExcecao(
        () -> aplicarDesconto(100.0, 101.0)
    )
);
```

```java
verificar(
    "percentual -10 deve ser rejeitado",
    "Percentual deve estar entre 0 e 100.",
    mensagemDaExcecao(
        () -> aplicarDesconto(100.0, -10.0)
    )
);
```

```java
verificar(
    "valor -50 deve ser rejeitado",
    "O valor original não pode ser negativo.",
    mensagemDaExcecao(
        () -> aplicarDesconto(-50.0, 10.0)
    )
);
```

```java
verificar(
    "percentual 150 deve ser rejeitado",
    "Percentual deve estar entre 0 e 100.",
    mensagemDaExcecao(
        () -> aplicarDesconto(100.0, 150.0)
    )
);
```

Todos esses testes devem produzir:

```text
PASS
```

Isso ocorre porque o comportamento esperado pelo teste é justamente que o sistema rejeite essas entradas.

---

# Parte 5 — Descubra quais testes estão errados

## Teste A

```java
verificar(
    "10% de 100",
    90.0,
    aplicarDesconto(100.0, 10.0)
);
```

Cálculo:

```text
100 × 10% = 10

100 - 10 = 90
```

Esperado:

```text
90
```

Obtido:

```text
90
```

Resultado:

```text
PASS
```

---

## Teste B

```java
verificar(
    "20% de 200",
    150.0,
    aplicarDesconto(200.0, 20.0)
);
```

Cálculo correto:

```text
200 × 20% = 40

200 - 40 = 160
```

O teste afirma que deveria ser:

```text
150
```

Mas o programa retorna:

```text
160
```

Resultado:

```text
FAIL
```

Neste caso, o método está correto.

O erro está no resultado esperado escrito no teste.

---

## Teste C

```java
verificar(
    "50% de 80",
    40.0,
    aplicarDesconto(80.0, 50.0)
);
```

Cálculo:

```text
80 × 50% = 40

80 - 40 = 40
```

Esperado:

```text
40
```

Obtido:

```text
40
```

Resultado:

```text
PASS
```

---

## Teste D

```java
verificar(
    "25% de 100",
    80.0,
    aplicarDesconto(100.0, 25.0)
);
```

Cálculo correto:

```text
100 × 25% = 25

100 - 25 = 75
```

O teste espera:

```text
80
```

Mas o método retorna:

```text
75
```

Resultado:

```text
FAIL
```

Novamente, o erro está no teste e não no método.

---

## Teste E

```java
verificar(
    "5% de 200",
    190.0,
    aplicarDesconto(200.0, 5.0)
);
```

Cálculo:

```text
200 × 5% = 10

200 - 10 = 190
```

Esperado:

```text
190
```

Obtido:

```text
190
```

Resultado:

```text
PASS
```

---

## Resultado da rodada

```text
Teste A: PASS

Teste B: FAIL

Teste C: PASS

Teste D: FAIL

Teste E: PASS
```

O resultado aproximado no terminal seria:

```text
PASS | 10% de 100 | esperado=90.0 | obtido=90.0

FAIL | 20% de 200 | esperado=150.0 | obtido=160.0

PASS | 50% de 80 | esperado=40.0 | obtido=40.0

FAIL | 25% de 100 | esperado=80.0 | obtido=75.0

PASS | 5% de 200 | esperado=190.0 | obtido=190.0
```

---

# Parte 6 — Questões

## 1. Quais testes passaram?

Passaram:

```text
Teste A
Teste C
Teste E
```

---

## 2. Quais testes falharam?

Falharam:

```text
Teste B
Teste D
```

---

## 3. Nos testes que falharam, o problema estava no programa ou no valor esperado pelo teste?

O problema estava no valor esperado definido pelo teste.

No Teste B:

```text
Esperado pelo teste: 150
Resultado correto: 160
```

No Teste D:

```text
Esperado pelo teste: 80
Resultado correto: 75
```

O método `aplicarDesconto` produziu o resultado correto nos dois casos.

---

## 4. Um teste pode estar errado mesmo quando o programa está correto?

Sim.

Um teste também é código e pode conter erros.

Se o desenvolvedor informar um resultado esperado incorreto, o teste poderá apresentar `FAIL` mesmo que o programa esteja funcionando corretamente.

Por exemplo:

```java
verificar(
    "50% de 100",
    60.0,
    aplicarDesconto(100.0, 50.0)
);
```

O programa corretamente retorna:

```text
50
```

Mas o teste espera:

```text
60
```

Portanto, o resultado será:

```text
FAIL
```

Isso não significa necessariamente que o método esteja errado.

---

## 5. Um programa que executa sem apresentar erro necessariamente está correto?

Não.

Um programa pode:

* compilar;
* executar;
* não apresentar nenhuma exceção;

e ainda assim produzir um resultado incorreto.

Por exemplo, imagine que o método estivesse escrito assim:

```java
return valorOriginal -
       (valorOriginal * (percentual / 10.0));
```

O código poderia compilar normalmente.

Porém, o cálculo estaria errado porque o percentual deveria ser dividido por `100`, e não por `10`.

Portanto:

```text
Compilar não significa estar correto.

Executar não significa estar correto.

Não gerar exceção não significa estar correto.
```

Os testes ajudam a verificar se o comportamento do programa corresponde ao comportamento esperado.

---

## 6. Por que é importante testar valores próximos aos limites permitidos?

Porque muitos defeitos aparecem justamente nos limites das regras.

Neste programa, o percentual permitido é:

```text
0 até 100
```

Por isso é importante testar:

```text
0
1

99
100
```

E também valores inválidos próximos ao limite:

```text
-1
101
```

Podemos ser ainda mais rigorosos:

```text
-0,01
0
0,01

99,99
100
100,01
```

Isso permite verificar se a regra foi implementada corretamente.

Por exemplo, este código estaria errado:

```java
if (percentual <= 0 || percentual >= 100)
```

Ele rejeitaria `0%` e `100%`, embora ambos sejam permitidos pela regra.

Testar exatamente os limites ajuda a identificar esse tipo de problema.

---

# Desafio — Cinco novos casos de teste

## Caso 1 — Valor muito alto

Entrada:

```text
Valor original: 100000
Percentual: 10
```

Cálculo:

```text
100000 × 10 / 100 = 10000

100000 - 10000 = 90000
```

Resultado esperado:

```text
90000
```

Resultado obtido:

```text
90000
```

PASS ou FAIL:

```text
PASS
```

Justificativa:

O método deve funcionar também com valores maiores.

Código:

```java
verificar(
    "10% de 100000",
    90000.0,
    aplicarDesconto(100000.0, 10.0)
);
```

---

## Caso 2 — Desconto decimal

Entrada:

```text
Valor original: 240
Percentual: 12,5
```

Cálculo:

```text
240 × 12,5 / 100 = 30

240 - 30 = 210
```

Resultado esperado:

```text
210
```

Resultado obtido:

```text
210
```

PASS ou FAIL:

```text
PASS
```

Justificativa:

O percentual é `double`, portanto deve aceitar valores decimais.

Código:

```java
verificar(
    "12.5% de 240",
    210.0,
    aplicarDesconto(240.0, 12.5)
);
```

---

## Caso 3 — Desconto de 0%

Entrada:

```text
Valor original: 75
Percentual: 0
```

Cálculo:

```text
75 × 0 / 100 = 0

75 - 0 = 75
```

Resultado esperado:

```text
75
```

Resultado obtido:

```text
75
```

PASS ou FAIL:

```text
PASS
```

Justificativa:

`0%` representa o menor percentual permitido.

O valor não deve sofrer alteração.

Código:

```java
verificar(
    "0% de 75",
    75.0,
    aplicarDesconto(75.0, 0.0)
);
```

---

## Caso 4 — Desconto de 100%

Entrada:

```text
Valor original: 350
Percentual: 100
```

Cálculo:

```text
350 × 100 / 100 = 350

350 - 350 = 0
```

Resultado esperado:

```text
0
```

Resultado obtido:

```text
0
```

PASS ou FAIL:

```text
PASS
```

Justificativa:

`100%` representa o maior percentual permitido.

Um desconto de 100% deve deixar o valor final igual a zero.

Código:

```java
verificar(
    "100% de 350",
    0.0,
    aplicarDesconto(350.0, 100.0)
);
```

---

## Caso 5 — Percentual inválido

Entrada:

```text
Valor original: 500
Percentual: -1
```

Resultado esperado:

```text
DEVE GERAR ERRO
```

Mensagem esperada:

```text
Percentual deve estar entre 0 e 100.
```

Resultado obtido:

```text
Percentual deve estar entre 0 e 100.
```

PASS ou FAIL:

```text
PASS
```

Justificativa:

O percentual está abaixo do limite mínimo permitido.

Código:

```java
verificar(
    "percentual -1 deve ser rejeitado",
    "Percentual deve estar entre 0 e 100.",
    mensagemDaExcecao(
        () -> aplicarDesconto(500.0, -1.0)
    )
);
```

---

# Reflexão final

## Afirmação

> "O programa compilou e executou sem apresentar nenhum erro."

Isso é suficiente para afirmar que o software está correto?

### Resposta

Não.

A compilação verifica principalmente se o código está de acordo com as regras da linguagem Java.

Um programa que compilou pode ainda conter erros de lógica.

Além disso, um programa pode executar sem lançar exceções e mesmo assim produzir resultados incorretos.

Por exemplo, imagine um programa que deveria calcular:

```text
10% de desconto sobre 100
```

O resultado correto seria:

```text
90
```

Porém, se o programa retornar:

```text
95
```

ele pode ter:

```text
compilado corretamente;
executado corretamente;
terminado sem nenhuma exceção;
```

mas ainda assim apresentar um comportamento incorreto.

Por isso, qualidade de software não significa apenas verificar se o programa compila ou executa.

É necessário comparar o comportamento obtido com o comportamento esperado.

Os testes ajudam justamente nessa comparação:

```text
ENTRADA
   ↓
PROGRAMA
   ↓
RESULTADO OBTIDO
   ↓
COMPARAÇÃO
   ↓
RESULTADO ESPERADO
   ↓
PASS ou FAIL
```

---

# Código completo com todos os testes principais

```java
public class LaboratorioDesconto {

    static double aplicarDesconto(
        double valorOriginal,
        double percentual
    ) {

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

        boolean[] resultados = {

            // Casos normais

            verificar(
                "10% de 100",
                90.0,
                aplicarDesconto(100.0, 10.0)
            ),

            verificar(
                "25% de 200",
                150.0,
                aplicarDesconto(200.0, 25.0)
            ),

            verificar(
                "0% de 80",
                80.0,
                aplicarDesconto(80.0, 0.0)
            ),

            verificar(
                "100% de 50",
                0.0,
                aplicarDesconto(50.0, 100.0)
            ),

            verificar(
                "20% de 150",
                120.0,
                aplicarDesconto(150.0, 20.0)
            ),

            verificar(
                "50% de 300",
                150.0,
                aplicarDesconto(300.0, 50.0)
            ),

            verificar(
                "15% de 120",
                102.0,
                aplicarDesconto(120.0, 15.0)
            ),

            verificar(
                "12.5% de 80",
                70.0,
                aplicarDesconto(80.0, 12.5)
            ),

            verificar(
                "1% de 1000",
                990.0,
                aplicarDesconto(1000.0, 1.0)
            ),

            verificar(
                "10% de 99.90",
                89.91,
                aplicarDesconto(99.90, 10.0)
            ),

            verificar(
                "30% de zero",
                0.0,
                aplicarDesconto(0.0, 30.0)
            ),


            // Entradas inválidas

            verificar(
                "percentual 101 deve ser rejeitado",
                "Percentual deve estar entre 0 e 100.",
                mensagemDaExcecao(
                    () -> aplicarDesconto(100.0, 101.0)
                )
            ),

            verificar(
                "percentual -10 deve ser rejeitado",
                "Percentual deve estar entre 0 e 100.",
                mensagemDaExcecao(
                    () -> aplicarDesconto(100.0, -10.0)
                )
            ),

            verificar(
                "valor -50 deve ser rejeitado",
                "O valor original não pode ser negativo.",
                mensagemDaExcecao(
                    () -> aplicarDesconto(-50.0, 10.0)
                )
            ),

            verificar(
                "percentual 150 deve ser rejeitado",
                "Percentual deve estar entre 0 e 100.",
                mensagemDaExcecao(
                    () -> aplicarDesconto(100.0, 150.0)
                )
            ),


            // Desafios

            verificar(
                "10% de 100000",
                90000.0,
                aplicarDesconto(100000.0, 10.0)
            ),

            verificar(
                "12.5% de 240",
                210.0,
                aplicarDesconto(240.0, 12.5)
            ),

            verificar(
                "0% de 75",
                75.0,
                aplicarDesconto(75.0, 0.0)
            ),

            verificar(
                "100% de 350",
                0.0,
                aplicarDesconto(350.0, 100.0)
            ),

            verificar(
                "percentual -1 deve ser rejeitado",
                "Percentual deve estar entre 0 e 100.",
                mensagemDaExcecao(
                    () -> aplicarDesconto(500.0, -1.0)
                )
            )
        };

        System.exit(
            codigoSaida(resultados)
        );
    }
}
```

Os testes realizados mostraram três situações diferentes:

1. **Testes que passam porque o programa produz o resultado esperado.**
2. **Testes que passam porque o programa rejeita corretamente uma entrada inválida.**
3. **Testes que falham porque o próprio resultado esperado foi escrito incorretamente.**

Portanto, um `FAIL` não significa automaticamente que o código testado possui um defeito.

É necessário investigar:

```text
O requisito está correto?

O resultado esperado está correto?

O caso de teste está correto?

O código está correto?
```

Somente após essa análise podemos determinar a origem da falha.

Esse é um dos princípios fundamentais do teste e da garantia da qualidade de software.
