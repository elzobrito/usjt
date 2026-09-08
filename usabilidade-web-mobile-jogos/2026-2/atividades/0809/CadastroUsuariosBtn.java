import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Label;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class CadastroUsuariosBtn {
    public static void main(String[] args) {
        Frame janela = new Frame("Cadastro de usuários");
        janela.setLayout(new FlowLayout());

        Label rotulo = new Label("Nenhum clique ainda");
        Button botao = new Button("Clicar");
        janela.add(rotulo);
        janela.add(botao);
        janela.setSize(480, 240);
       
         botao.addActionListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent evento) {
                janela.dispose();
                System.exit(0);
            }
        });
        janela.setVisible(true);
    }
}