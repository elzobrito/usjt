// Importa a classe Frame da biblioteca AWT.
// Frame representa uma janela gráfica simples.
import java.awt.Frame;

// Importa a classe WindowAdapter.
// Ela permite tratar eventos relacionados à janela,
// como fechar, abrir, minimizar etc.
import java.awt.event.WindowAdapter;

// Importa a classe WindowEvent.
// Essa classe representa um evento ocorrido em uma janela.
import java.awt.event.WindowEvent;


// Declara a classe principal do programa.
// O nome da classe é CadastroUsuarios.
public class CadastroUsuarios {

    // Método principal do programa.
    // A execução da aplicação começa por este método.
    public static void main(String[] args) {

        // Cria um objeto chamado "janela".
        // O objeto é do tipo Frame.
        //
        // O texto "Cadastro de usuários" será exibido
        // na barra de título da janela.
        Frame janela = new Frame("Cadastro de usuários");


        // Define o tamanho da janela.
        //
        // O primeiro valor representa a largura: 480 pixels.
        // O segundo valor representa a altura: 240 pixels.
        janela.setSize(480, 240);


        // Adiciona um "ouvinte" de eventos à janela.
        //
        // Esse ouvinte ficará observando acontecimentos
        // relacionados à janela, como o usuário clicar
        // no botão de fechar.
        janela.addWindowListener(new WindowAdapter() {

            // A anotação @Override informa que estamos
            // sobrescrevendo um método existente na
            // classe WindowAdapter.
            @Override

            // Este método é executado automaticamente
            // quando o usuário tenta fechar a janela.
            //
            // O parâmetro "evento" contém informações
            // sobre o evento ocorrido.
            public void windowClosing(WindowEvent evento) {

                // Fecha e libera os recursos utilizados
                // pela janela.
                janela.dispose();


                // Encerra completamente a execução
                // do programa Java.
                //
                // O valor 0 indica que o programa
                // terminou normalmente, sem erros.
                System.exit(0);

            } // Fim do método windowClosing.

        }); // Fim da configuração do ouvinte da janela.


        // Torna a janela visível na tela.
        //
        // Sem esta linha, a janela seria criada,
        // mas não apareceria para o usuário.
        janela.setVisible(true);

    } // Fim do método main.

} // Fim da classe CadastroUsuarios.