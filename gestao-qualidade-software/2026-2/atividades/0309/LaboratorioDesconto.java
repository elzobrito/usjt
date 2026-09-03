// Declaração da classe principal.
// O nome da classe é LaboratorioDesconto.
public class LaboratorioDesconto {

    // Método responsável por calcular o valor final depois de aplicar um desconto.
    // O método é "static", portanto pode ser chamado diretamente dentro da classe,
    // sem precisar criar um objeto de LaboratorioDesconto.
    //
    // Ele recebe dois valores:
    // valorOriginal -> preço antes do desconto
    // percentual    -> porcentagem de desconto que será aplicada
    //
    // O método retorna um valor do tipo double.
    static double aplicarDesconto(double valorOriginal, double percentual) {

        // Verifica se o valor original informado é menor que zero.
        if (valorOriginal < 0) {

            // Se o valor for negativo, o método interrompe sua execução
            // e lança uma exceção indicando que o valor é inválido.
            throw new IllegalArgumentException(
                "O valor original não pode ser negativo."
            );
        }

        // Verifica se o percentual está fora do intervalo permitido.
        //
        // percentual < 0   -> desconto negativo
        // percentual > 100 -> desconto maior que 100%
        //
        // O operador || significa "OU".
        if (percentual < 0 || percentual > 100) {

            // Se uma das condições acima for verdadeira,
            // uma exceção é lançada.
            throw new IllegalArgumentException(
                "Percentual deve estar entre 0 e 100."
            );
        }

        // Calcula e retorna o valor final com desconto.
        //
        // percentual / 100.0 transforma a porcentagem em valor decimal.
        // Exemplo:
        // 15 / 100.0 = 0.15
        //
        // valorOriginal * 0.15 calcula o valor do desconto.
        //
        // Depois, o desconto é subtraído do valor original.
        //
        // Exemplo:
        // 200 - (200 * 0.15)
        // 200 - 30
        // 170
        return valorOriginal - (valorOriginal * (percentual / 100.0));
    }


    // Método utilizado para verificar se o resultado de um teste
    // corresponde ao resultado esperado.
    //
    // nome     -> descrição do teste
    // esperado -> resultado que deveria ser produzido
    // obtido   -> resultado realmente produzido pelo programa
    //
    // O método retorna true se o teste passar
    // e false se o teste falhar.
    static boolean verificar(String nome, Object esperado, Object obtido) {

        // Compara o valor esperado com o valor obtido.
        //
        // Objects.equals() retorna true quando os dois valores são iguais
        // e false quando são diferentes.
        //
        // A variável "passou" guardará o resultado dessa comparação.
        boolean passou = java.util.Objects.equals(esperado, obtido);

        // Exibe o resultado do teste no terminal.
        System.out.println(

            // Operador ternário:
            //
            // Se "passou" for true, mostra "PASS".
            // Caso contrário, mostra "FAIL".
            (passou ? "PASS" : "FAIL")

            // Adiciona o nome do teste à mensagem.
            + " | " + nome

            // Exibe o valor que era esperado.
            + " | esperado=" + esperado

            // Exibe o valor realmente obtido.
            + " | obtido=" + obtido
        );

        // Retorna true ou false para indicar
        // se o teste passou ou falhou.
        return passou;
    }


    // Método auxiliar utilizado nos testes que esperam uma exceção.
    //
    // Ele recebe uma ação do tipo Runnable.
    //
    // Runnable representa uma ação que pode ser executada
    // e que não retorna nenhum valor.
    static String mensagemDaExcecao(Runnable acao) {

        // O bloco try contém o código que será executado
        // e que pode eventualmente lançar uma exceção.
        try {

            // Executa a ação recebida como parâmetro.
            acao.run();

            // Se nenhuma exceção ocorrer,
            // significa que a ação terminou normalmente.
            return "(nenhuma exceção)";

        // O bloco catch é executado caso ocorra
        // alguma exceção do tipo RuntimeException.
        } catch (RuntimeException erro) {

            // Retorna apenas a mensagem da exceção.
            //
            // Exemplo:
            // "Percentual deve estar entre 0 e 100."
            return erro.getMessage();
        }
    }


    // Método que analisa todos os resultados dos testes
    // e determina qual será o código de saída do programa.
    //
    // boolean... significa que o método pode receber
    // vários valores booleanos.
    //
    // Exemplo:
    // codigoSaida(true, true, false)
    static int codigoSaida(boolean... resultados) {

        // Percorre todos os resultados recebidos.
        //
        // A cada repetição, a variável "passou"
        // recebe um dos valores do array resultados.
        for (boolean passou : resultados) {

            // Verifica se algum teste falhou.
            //
            // ! significa negação.
            //
            // Se passou == false,
            // então !passou será true.
            if (!passou) {

                // Retorna 1 para indicar que houve
                // pelo menos uma falha nos testes.
                return 1;
            }
        }

        // Se o laço terminou e nenhum teste falhou,
        // retorna 0.
        //
        // Por convenção:
        // 0 -> execução bem-sucedida
        // 1 -> ocorreu alguma falha
        return 0;
    }


    // Método principal do programa.
    //
    // A execução da aplicação começa aqui.
    public static void main(String[] args) {

        // Cria um array de valores booleanos chamado "resultados".
        //
        // Cada posição do array receberá true ou false,
        // dependendo do resultado de cada teste.
        boolean[] resultados = {

            // TESTE 1
            //
            // Verifica se 15% de desconto sobre 200
            // produz o resultado 170.
            verificar(
                "15% de 200",
                170.0,
                aplicarDesconto(200.0, 15.0)
            ),

            // TESTE 2
            //
            // Verifica o limite inferior do percentual.
            //
            // Um desconto de 0% não deve alterar o valor.
            verificar(
                "0% de 80",
                80.0,
                aplicarDesconto(80.0, 0.0)
            ),

            // TESTE 3
            //
            // Verifica o limite superior permitido.
            //
            // Um desconto de 100% deve resultar em zero.
            verificar(
                "100% de 50",
                0.0,
                aplicarDesconto(50.0, 100.0)
            ),

            // TESTE 4
            //
            // Verifica se um percentual acima de 100
            // é corretamente rejeitado.
            verificar(

                // Nome do teste.
                "percentual 150 deve ser rejeitado",

                // Mensagem que esperamos receber.
                "Percentual deve estar entre 0 e 100.",

                // Executa aplicarDesconto com um percentual inválido.
                //
                // A expressão:
                //
                // () -> aplicarDesconto(100.0, 150.0)
                //
                // é uma expressão lambda.
                //
                // Ela representa uma ação que será passada
                // para o método mensagemDaExcecao.
                mensagemDaExcecao(
                    () -> aplicarDesconto(100.0, 150.0)
                )
            ),

            // TESTE 5
            //
            // Verifica se um valor original negativo
            // é corretamente rejeitado.
            verificar(

                // Nome do teste.
                "valor negativo deve ser rejeitado",

                // Mensagem esperada.
                "O valor original não pode ser negativo.",

                // Executa o método com um valor inválido
                // e captura a mensagem da exceção.
                mensagemDaExcecao(
                    () -> aplicarDesconto(-10.0, 10.0)
                )
            )
        };

        // Encerra a execução do programa.
        //
        // codigoSaida(resultados) verificará todos os testes.
        //
        // Se todos passarem:
        // System.exit(0)
        //
        // Se pelo menos um falhar:
        // System.exit(1)
        //
        // Isso é útil principalmente quando os testes
        // são executados automaticamente por scripts
        // ou ferramentas de integração contínua.
        System.exit(
            codigoSaida(resultados)
        );
    }
}