import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;   // importação incompleta para o uso do botão
import java.awt.event.WindowEvent;

public class TelaCadastro extends JFrame {

    private JTextField campoNome;
    private JTextField campoSenha;        // ERRO 3
    private JButton botaoCadastrar;

    public TelaCadastro() {
        setTitle("Cadastro de Usuários");
        setSize(420, 320);
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);   // ERRO 4
        setLocationRelativeTo(null);
        setResizable(false);

        JPanel painel = new JPanel(new GridBagLayout());
        painel.setBackground(Color.WHITE);
        painel.setBorder(BorderFactory.createEmptyBorder(20, 40, 30, 40));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 0, 8, 0);
        gbc.fill = GridBagConstraints.VERTICAL;   // ERRO 1
        gbc.weightx = 1.0;

        JLabel titulo = new JLabel("CADASTRO", SwingConstants.LEFT);   // ERRO 2
        titulo.setFont(new Font("SansSerif", Font.BOLD, 28));
        titulo.setForeground(new Color(30, 60, 120));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.ipady = 10;
        painel.add(titulo, gbc);

        campoNome = new JTextField();
        campoNome.setFont(new Font("SansSerif", Font.PLAIN, 14));
        campoNome.setPreferredSize(new Dimension(280, 38));
        campoNome.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true),
                BorderFactory.createEmptyBorder(4, 8, 4, 8)));
        gbc.gridy = 1;
        gbc.ipady = 6;
        painel.add(campoNome, gbc);

        campoSenha = new JTextField();    // ERRO 3
        campoSenha.setFont(new Font("SansSerif", Font.PLAIN, 14));
        campoSenha.setPreferredSize(new Dimension(280, 38));
        campoSenha.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true),
                BorderFactory.createEmptyBorder(4, 8, 4, 8)));
        gbc.gridy = 2;
        painel.add(campoSenha, gbc);

        botaoCadastrar = new JButton("Cadastrar");
        botaoCadastrar.setFont(new Font("SansSerif", Font.BOLD, 14));
        botaoCadastrar.setPreferredSize(new Dimension(140, 38));
        botaoCadastrar.setBackground(new Color(30, 60, 120));
        botaoCadastrar.setForeground(Color.WHITE);
        botaoCadastrar.setFocusPainted(false);
        botaoCadastrar.setCursor(new Cursor(Cursor.HAND_CURSOR));
        botaoCadastrar.setBorder(BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true));

        JPanel painelBotao = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 0));
        painelBotao.setBackground(Color.WHITE);
        painelBotao.add(botaoCadastrar);

        gbc.gridy = 3;
        gbc.ipady = 0;
        painel.add(painelBotao, gbc);

        // ERRO 5: listener e método errados para um botão
        botaoCadastrar.addActionListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                String nome  = campoNome.getText().trim();
                String senha = campoSenha.getText().trim();

                if (nome.isEmpty() && senha.isEmpty()) {   // ERRO 6
                    JOptionPane.showMessageDialog(
                            TelaCadastro.this,
                            "Por favor, preencha o nome e a senha.",
                            "Campos obrigatórios",
                            JOptionPane.WARNING_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(
                            TelaCadastro.this,
                            "Cadastro realizado com sucesso!\nNome: " + nome,
                            "Sucesso!",
                            JOptionPane.INFORMATION_MESSAGE);
                }
            }
        });

        getRootPane().setDefaultButton(botaoCadastrar);

        add(painel);
        setVisible(false);   // ERRO 7
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaCadastro());
    }
}