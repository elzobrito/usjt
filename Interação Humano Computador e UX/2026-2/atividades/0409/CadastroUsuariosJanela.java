import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class CadastroUsuariosJanela {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(CadastroUsuariosJanela::criarTela);
    }

    private static void criarTela() {
        DefaultListModel<String> usuarios = new DefaultListModel<>();
        usuarios.addElement("1 — Ana");
        usuarios.addElement("2 — Carlos");
        int[] proximoId = {3};

        JFrame janela = new JFrame("Cadastro de usuários");
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        janela.setLayout(new BorderLayout(8, 8));

        JLabel titulo = new JLabel("Cadastro de usuários", JLabel.CENTER);

        JPanel formulario = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JLabel rotuloNome = new JLabel("Nome");
        JTextField campoNome = new JTextField(20);
        rotuloNome.setLabelFor(campoNome);
        JButton botaoCadastrar = new JButton("Cadastrar");
        JButton botaoExcluir = new JButton("Excluir selecionado");
        formulario.add(rotuloNome);
        formulario.add(campoNome);
        formulario.add(botaoCadastrar);
        formulario.add(botaoExcluir);

        JLabel mensagem = new JLabel(" ");

        JList<String> lista = new JList<>(usuarios);
        lista.setVisibleRowCount(8);

        JPanel norte = new JPanel(new BorderLayout());
        norte.add(titulo, BorderLayout.NORTH);
        norte.add(formulario, BorderLayout.CENTER);
        norte.add(mensagem, BorderLayout.SOUTH);

        janela.add(norte, BorderLayout.NORTH);
        janela.add(new JScrollPane(lista), BorderLayout.CENTER);

        botaoCadastrar.addActionListener(evento -> {
            String nome = campoNome.getText().strip();
            if (nome.isEmpty()) {
                mensagem.setText("O campo nome é obrigatório.");
                return;
            }
            usuarios.addElement(proximoId[0] + " — " + nome);
            proximoId[0] += 1;
            campoNome.setText("");
            mensagem.setText("Usuário cadastrado.");
        });

        botaoExcluir.addActionListener(evento -> {
            int indice = lista.getSelectedIndex();
            if (indice < 0) {
                mensagem.setText("Selecione um nome na lista.");
                return;
            }
            usuarios.remove(indice);
            mensagem.setText("Usuário excluído.");
        });

        janela.setSize(560, 360);
        janela.setLocationRelativeTo(null);
        janela.setVisible(true);
    }
}