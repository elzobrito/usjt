boolean[] resultados = {

    // =========================================================
    // CASOS NORMAIS
    // =========================================================

    verificar(
        "15% de 200",
        170.0,
        aplicarDesconto(200.0, 15.0)
    ),

    verificar(
        "10% de 100",
        90.0,
        aplicarDesconto(100.0, 10.0)
    ),

    verificar(
        "25% de 120",
        90.0,
        aplicarDesconto(120.0, 25.0)
    ),

    verificar(
        "50% de 300",
        150.0,
        aplicarDesconto(300.0, 50.0)
    ),

    verificar(
        "75% de 200",
        50.0,
        aplicarDesconto(200.0, 75.0)
    ),


    // =========================================================
    // TESTES DOS LIMITES DO PERCENTUAL
    // =========================================================

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


    // =========================================================
    // VALOR ORIGINAL IGUAL A ZERO
    // =========================================================

    verificar(
        "50% de valor zero",
        0.0,
        aplicarDesconto(0.0, 50.0)
    ),

    verificar(
        "0% de valor zero",
        0.0,
        aplicarDesconto(0.0, 0.0)
    ),

    verificar(
        "100% de valor zero",
        0.0,
        aplicarDesconto(0.0, 100.0)
    ),


    // =========================================================
    // PERCENTUAIS DECIMAIS
    // =========================================================

    verificar(
        "12.5% de 80",
        70.0,
        aplicarDesconto(80.0, 12.5)
    ),

    verificar(
        "2.5% de 200",
        195.0,
        aplicarDesconto(200.0, 2.5)
    ),

    verificar(
        "1% de 1000",
        990.0,
        aplicarDesconto(1000.0, 1.0)
    ),


    // =========================================================
    // PERCENTUAIS INVÁLIDOS
    // =========================================================

    verificar(
        "percentual 150 deve ser rejeitado",
        "Percentual deve estar entre 0 e 100.",
        mensagemDaExcecao(
            () -> aplicarDesconto(100.0, 150.0)
        )
    ),

    verificar(
        "percentual 101 deve ser rejeitado",
        "Percentual deve estar entre 0 e 100.",
        mensagemDaExcecao(
            () -> aplicarDesconto(100.0, 101.0)
        )
    ),

    verificar(
        "percentual 100.01 deve ser rejeitado",
        "Percentual deve estar entre 0 e 100.",
        mensagemDaExcecao(
            () -> aplicarDesconto(100.0, 100.01)
        )
    ),

    verificar(
        "percentual -1 deve ser rejeitado",
        "Percentual deve estar entre 0 e 100.",
        mensagemDaExcecao(
            () -> aplicarDesconto(100.0, -1.0)
        )
    ),

    verificar(
        "percentual -0.01 deve ser rejeitado",
        "Percentual deve estar entre 0 e 100.",
        mensagemDaExcecao(
            () -> aplicarDesconto(100.0, -0.01)
        )
    ),


    // =========================================================
    // VALORES ORIGINAIS INVÁLIDOS
    // =========================================================

    verificar(
        "valor negativo deve ser rejeitado",
        "O valor original não pode ser negativo.",
        mensagemDaExcecao(
            () -> aplicarDesconto(-10.0, 10.0)
        )
    ),

    verificar(
        "valor -0.01 deve ser rejeitado",
        "O valor original não pode ser negativo.",
        mensagemDaExcecao(
            () -> aplicarDesconto(-0.01, 10.0)
        )
    ),


    // =========================================================
    // DOIS DADOS INVÁLIDOS AO MESMO TEMPO
    // =========================================================

    verificar(
        "valor e percentual negativos",
        "O valor original não pode ser negativo.",
        mensagemDaExcecao(
            () -> aplicarDesconto(-100.0, -10.0)
        )
    )
};