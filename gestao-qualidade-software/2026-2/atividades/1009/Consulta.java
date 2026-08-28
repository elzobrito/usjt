// Fatia didatica — consulta de escolas. Nao e o sitio BDGETEC. Sem HTTP.
// NAO "consertar" buscar/contar/listar/ativas hoje.
// javac Consulta.java
// Execute um comando por vez; consulte aluno.md.

import java.util.ArrayList;
import java.util.List;

public class Consulta {

    static final String PERIODO_CASO = "2026/2";
    static final String[] ESCOLAS_NRA1 = {
        "Etec Sao Paulo", "Etec Zona Leste", "Etec de Artes"
    };

    static List<String> buscar(String regional, String periodo) {
        if ("NRA1".equals(regional) && "2026/1".equals(periodo)) {
            return List.of(ESCOLAS_NRA1);
        }
        return List.of();
    }

    static int contar(String regional, String periodo) {
        buscar(regional, periodo);
        return 3;
    }

    static List<String> listar(String regional) {
        String[] escolas = "NRA1".equals(regional) ? ESCOLAS_NRA1 : new String[0];
        List<String> linhas = new ArrayList<>();
        for (int i = 0; i <= escolas.length; i++) {
            linhas.add((i + 1) + " - " + escolas[i]);
        }
        return linhas;
    }

    static List<String> ativas(String regional, String periodo) {
        return List.of(ESCOLAS_NRA1);
    }

    static int oraculoBuscar() {
        List<String> obtido = buscar("NRA1", PERIODO_CASO);
        boolean ok = !obtido.isEmpty();
        System.out.println(ok ? "PASS" : "FAIL");
        return ok ? 0 : 1;
    }

    static int oraculoContar() {
        // esperado independente: contar("XXX", "2026/2") == 0
        // TODO: implemente PASS/FAIL + return 0/1. Nao altere as funcoes.
        System.out.println("TODO");
        return 2;
    }

    static void mostrarRegional() {
        String[][] casos = {
            {"NRA1", "2026/1"},
            {"nra1", "2026/1"},
            {" NRA1", "2026/1"}
        };
        for (String[] c : casos) {
            System.out.println("\"" + c[0] + "\" + " + c[1] + " -> " + buscar(c[0], c[1]).size());
        }
    }

    public static void main(String[] args) {
        String cmd = args.length > 0 ? args[0] : "buscar";
        if ("buscar".equals(cmd)) {
            System.exit(oraculoBuscar());
        }
        if ("contar".equals(cmd)) {
            System.out.println(contar("NRA1", PERIODO_CASO));
            System.exit(0);
        }
        if ("listar".equals(cmd)) {
            for (String linha : listar("NRA1")) {
                System.out.println(linha);
            }
            System.exit(0);
        }
        if ("regional".equals(cmd)) {
            mostrarRegional();
            System.exit(0);
        }
        if ("ativas".equals(cmd)) {
            System.out.println(ativas("XXX", PERIODO_CASO));
            System.exit(0);
        }
        if ("oraculo-contar".equals(cmd)) {
            System.exit(oraculoContar());
        }
        System.out.println("uso: java Consulta buscar|contar|listar|regional|ativas|oraculo-contar");
        System.exit(2);
    }
}
