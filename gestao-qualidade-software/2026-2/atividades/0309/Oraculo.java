// esperado: consultar("NRA1", "2026/2") devolve escolas (lista nao vazia)
// Fatia didatica. Nao e o sitio BDGETEC. Sem HTTP.
// javac Oraculo.java && java Oraculo

import java.util.List;

public class Oraculo {

    static List<String> consultar(String regional, String periodo) {
        if ("NRA1".equals(regional) && "2026/1".equals(periodo)) {
            return List.of("Etec Sao Paulo", "Etec Zona Leste", "Etec de Artes");
        }
        return List.of();
    }

    public static void main(String[] args) {
        String periodoCaso = "2026/2";
        List<String> obtido = consultar("NRA1", periodoCaso);
        boolean ok = !obtido.isEmpty();
        System.out.println(ok ? "PASS" : "FAIL");
        System.exit(ok ? 0 : 1);
    }
}
