public class LaboratorioDesconto {

    static double aplicarDesconto(double valorOriginal, double percentual) {
        if (valorOriginal < 0) {
            throw new IllegalArgumentException("O valor original não pode ser negativo.");
        }
        if (percentual < 0 || percentual > 100) {
            throw new IllegalArgumentException("Percentual deve estar entre 0 e 100.");
        }
        return valorOriginal - (valorOriginal * (percentual / 100.0));
    }

    static boolean verificar(String nome, Object esperado, Object obtido) {
        boolean passou = java.util.Objects.equals(esperado, obtido);
        System.out.println(
            (passou ? "PASS" : "FAIL") + " | " + nome
            + " | esperado=" + esperado + " | obtido=" + obtido
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
            verificar("15% de 200", 170.0, aplicarDesconto(200.0, 15.0)),
            verificar("0% de 80", 80.0, aplicarDesconto(80.0, 0.0)),
            verificar("100% de 50", 0.0, aplicarDesconto(50.0, 100.0)),
            verificar(
                "percentual 150 deve ser rejeitado",
                "Percentual deve estar entre 0 e 100.",
                mensagemDaExcecao(() -> aplicarDesconto(100.0, 150.0))
            ),
            verificar(
                "valor negativo deve ser rejeitado",
                "O valor original não pode ser negativo.",
                mensagemDaExcecao(() -> aplicarDesconto(-10.0, 10.0))
            )
        };
        System.exit(codigoSaida(resultados));
    }
}