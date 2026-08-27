package br.usjt.gqs.bdgetec;

import static org.junit.jupiter.api.Assertions.assertFalse;

import org.junit.jupiter.api.Test;

class ConsultaEscolasTest {

    private final ConsultaEscolas consulta = new ConsultaEscolas();

    @Test
    void periodoAtualDevolveEscolas() {
        // Este teste usa literal internado e o período atual do caso (2026/2).
        // Com o código entregue deve falhar: a classe compara o período com 2026/1.
        // Barra vermelha aqui não é erro de setup — é evidência.
        var escolas = consulta.buscar("NRA1", ConsultaEscolas.PERIODO_ATUAL);
        assertFalse(escolas.isEmpty(), "período 2026/2 deveria devolver escolas da NRA1");
    }

    // TODO 1: buscar(new String("NRA1"), "2026/2") devolve as três escolas.

    // TODO 2: contar(regional, periodo) == buscar(regional, periodo).size()
    //         no período atual e num período vazio.

    // TODO 3: listarLinhas("NRA1") tem 3 linhas e não lança exceção.
}
