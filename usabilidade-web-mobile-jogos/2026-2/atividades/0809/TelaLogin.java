import javax.swing.*;
import java.awt.*;

public class TelaLogin extends JFrame {

    private final JTextField campoUsuario;
    private final JPasswordField campoSenha;
    private final JButton botaoEntrar;

    public TelaLogin() {
        setTitle("Login");
        setSize(420, 320);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        JPanel painel = new JPanel(new GridBagLayout());
        painel.setBackground(Color.WHITE);
        painel.setBorder(BorderFactory.createEmptyBorder(20, 40, 30, 40));

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 0, 8, 0);
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;

        JLabel titulo = new JLabel("LOGIN", SwingConstants.CENTER);
        titulo.setFont(new Font("SansSerif", Font.BOLD, 28));
        titulo.setForeground(new Color(30, 60, 120));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.ipady = 10;
        painel.add(titulo, gbc);

        campoUsuario = new JTextField();
        campoUsuario.setFont(new Font("SansSerif", Font.PLAIN, 14));
        campoUsuario.setPreferredSize(new Dimension(280, 38));
        campoUsuario.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true),
                BorderFactory.createEmptyBorder(4, 8, 4, 8)));
        gbc.gridy = 1;
        gbc.ipady = 6;
        painel.add(campoUsuario, gbc);

        campoSenha = new JPasswordField();
        campoSenha.setFont(new Font("SansSerif", Font.PLAIN, 14));
        campoSenha.setPreferredSize(new Dimension(280, 38));
        campoSenha.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true),
                BorderFactory.createEmptyBorder(4, 8, 4, 8)));
        gbc.gridy = 2;
        painel.add(campoSenha, gbc);

        botaoEntrar = new JButton("Entrar");
        botaoEntrar.setFont(new Font("SansSerif", Font.BOLD, 14));
        botaoEntrar.setPreferredSize(new Dimension(140, 38));
        botaoEntrar.setBackground(new Color(30, 60, 120));
        botaoEntrar.setForeground(Color.WHITE);
        botaoEntrar.setFocusPainted(false);
        botaoEntrar.setCursor(new Cursor(Cursor.HAND_CURSOR));
        botaoEntrar.setBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true));

        JPanel painelBotao = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 0));
        painelBotao.setBackground(Color.WHITE);
        painelBotao.add(botaoEntrar);

        gbc.gridy = 3;
        gbc.ipady = 0;
        painel.add(painelBotao, gbc);

        botaoEntrar.addActionListener(e -> autenticar());
        getRootPane().setDefaultButton(botaoEntrar);

        add(painel);
        setVisible(true);
    }

    private void autenticar() {
        String usuario = campoUsuario.getText().trim();
        String senha = new String(campoSenha.getPassword());

        if (usuario.isEmpty() || senha.isEmpty()) {
            JOptionPane.showMessageDialog(
                    this,
                    "Por favor, preencha o usuário e a senha.",
                    "Campos obrigatórios",
                    JOptionPane.WARNING_MESSAGE);
        } else if (usuario.equals("admin") && senha.equals("123")) {
            JOptionPane.showMessageDialog(
                    this,
                    "Login realizado com sucesso!",
                    "Bem-vindo!",
                    JOptionPane.INFORMATION_MESSAGE);

            dispose();
            new Dashboard(usuario);
        } else {
            JOptionPane.showMessageDialog(
                    this,
                    "Usuário ou senha inválidos.",
                    "Erro de Login",
                    JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TelaLogin::new);
    }
}
