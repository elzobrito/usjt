public class ConsultaEscolas {

    public static void main(String[] args) {

        String[] escolas = {
            "Etec São Paulo",
            "Etec Zona Leste",
            "Etec de Artes"
        };

        String regional = "NRA1";
        String periodo = "2026/2";

        if (regional == "NRA1") {
            System.out.println("Escolas encontradas:");
        }

        for (int i = 0; i <= escolas.length; i++) {
            System.out.println(i + 1 + " - " + escolas[i]);
        }

        if (periodo.equals("2026/1")) {
            System.out.println("Período atual: " + periodo);
        }

        int totalEscolas = "3";

        System.out.println("Total de escolas: " + totalEscola);
    }
}