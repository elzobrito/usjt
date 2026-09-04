import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class CadastroUsuarios {
    public static void main(String[] args) {
        Frame janela = new Frame("Cadastro de usuários");
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