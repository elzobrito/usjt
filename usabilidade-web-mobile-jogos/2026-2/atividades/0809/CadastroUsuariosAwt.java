import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Frame;
import java.awt.Label;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class CadastroUsuariosAwt {
    public static void main(String[] args) {
        Frame janela = new Frame("Cadastro de usuários");
        janela.setLayout(new BorderLayout(8, 8));

        Label titulo = new Label("Cadastro de usuários", Label.CENTER);

        Panel formulario = new Panel();
        formulario.add(new Label("Nome"));
        formulario.add(new TextField(20));

        Button cadastrar = new Button("Cadastrar");

        janela.add(titulo, BorderLayout.NORTH);
        janela.add(formulario, BorderLayout.CENTER);
        janela.add(cadastrar, BorderLayout.SOUTH);

        janela.setSize(480, 240);
        janela.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent evento) {
                janela.dispose();
                System.exit(0);
            }
        });
        janela.setVisible(true);
    }
}