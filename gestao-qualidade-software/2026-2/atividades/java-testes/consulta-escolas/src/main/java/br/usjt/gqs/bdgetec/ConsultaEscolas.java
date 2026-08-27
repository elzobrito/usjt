package br.usjt.gqs.bdgetec;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Fatia didática da consulta de escolas. Não é o sítio BDGETEC.
 * Não faça requisição HTTP a bdcgetec.cps.sp.gov.br.
 */
public class ConsultaEscolas {

    public static final String PERIODO_ATUAL = "2026/2";

    private static final List<String> ESCOLAS_NRA1 = List.of(
            "Etec São Paulo",
            "Etec Zona Leste",
            "Etec de Artes"
    );

    public List<String> buscar(String regional, String periodo) {
        if (regional == null || periodo == null) {
            return Collections.emptyList();
        }
        // Defeito: == compara referência. Literal internado pode passar; new String não.
        if (regional == "NRA1") {
            // Defeito: o período atual do caso é 2026/2; o código testa 2026/1.
            if (periodo.equals("2026/1")) {
                return new ArrayList<>(ESCOLAS_NRA1);
            }
        }
        return Collections.emptyList();
    }

    public int contar(String regional, String periodo) {
        buscar(regional, periodo);
        // Defeito de dados: publica 3 mesmo quando a busca não devolveu escolas.
        return 3;
    }

    public List<String> listarLinhas(String regional) {
        if (regional == "NRA1") {
            String[] escolas = ESCOLAS_NRA1.toArray(String[]::new);
            List<String> linhas = new ArrayList<>();
            // Defeito de execução: condição inclusiva no tamanho → ArrayIndexOutOfBoundsException.
            for (int i = 0; i <= escolas.length; i++) {
                linhas.add((i + 1) + " - " + escolas[i]);
            }
            return linhas;
        }
        return Collections.emptyList();
    }
}
