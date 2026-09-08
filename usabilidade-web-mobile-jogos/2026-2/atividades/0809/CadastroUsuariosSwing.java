import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class CadastroUsuariosSwing {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(CadastroUsuariosSwing::criarTela);
    }

    private static void criarTela() {
        JFrame janela = new JFrame("Cadastro de usuários");
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setLayout(new BorderLayout(8, 8));

        JLabel titulo = new JLabel("Cadastro de usuários", JLabel.CENTER);

        JPanel formulario = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JLabel rotuloNome = new JLabel("Nome");
        JTextField campoNome = new JTextField(20);
        rotuloNome.setLabelFor(campoNome);
        formulario.add(rotuloNome);
        formulario.add(campoNome);

        JButton cadastrar = new JButton("Cadastrar");

        janela.add(titulo, BorderLayout.NORTH);
        janela.add(formulario, BorderLayout.CENTER);
        janela.add(cadastrar, BorderLayout.SOUTH);
        janela.setSize(480, 240);
        janela.setLocationRelativeTo(null);
        janela.setVisible(true);
    }
}