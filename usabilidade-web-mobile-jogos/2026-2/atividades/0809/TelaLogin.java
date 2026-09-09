import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TelaLogin extends JFrame {

    private JTextField campoUsuario;
    private JPasswordField campoSenha;
    private JButton botaoEntrar;

    public TelaLogin() {
        // Configuração da janela
        setTitle("Login");
        setSize(420, 320);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // centraliza na tela
        setResizable(false);

        // Painel principal com GridBagLayout para controle preciso
        JPanel painel = new JPanel(new GridBagLayout());
        painel.setBackground(Color.WHITE);
        painel.setBorder(BorderFactory.createEmptyBorder(20, 40, 30, 40));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 0, 8, 0);
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.weightx = 1.0;

        // ----- Título LOGIN -----
        JLabel titulo = new JLabel("LOGIN", SwingConstants.CENTER);
        titulo.setFont(new Font("SansSerif", Font.BOLD, 28));
        titulo.setForeground(new Color(30, 60, 120));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.ipady = 10;
        painel.add(titulo, gbc);

        // ----- Campo Usuário -----
        campoUsuario = new JTextField();
        campoUsuario.setFont(new Font("SansSerif", Font.PLAIN, 14));
        campoUsuario.setPreferredSize(new Dimension(280, 38));
        campoUsuario.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true),
                BorderFactory.createEmptyBorder(4, 8, 4, 8)));
        gbc.gridy = 1;
        gbc.ipady = 6;
        painel.add(campoUsuario, gbc);

        // ----- Campo Senha -----
        campoSenha = new JPasswordField();
        campoSenha.setFont(new Font("SansSerif", Font.PLAIN, 14));
        campoSenha.setPreferredSize(new Dimension(280, 38));
        campoSenha.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true),
                BorderFactory.createEmptyBorder(4, 8, 4, 8)));
        gbc.gridy = 2;
        painel.add(campoSenha, gbc);

        // ----- Botão Entrar -----
        botaoEntrar = new JButton("Entrar");
        botaoEntrar.setFont(new Font("SansSerif", Font.BOLD, 14));
        botaoEntrar.setPreferredSize(new Dimension(140, 38));
        botaoEntrar.setBackground(new Color(30, 60, 120));
        botaoEntrar.setForeground(Color.WHITE);
        botaoEntrar.setFocusPainted(false);
        botaoEntrar.setCursor(new Cursor(Cursor.HAND_CURSOR));
        botaoEntrar.setBorder(BorderFactory.createLineBorder(new Color(30, 60, 120), 2, true));

        // Painel para centralizar o botão
        JPanel painelBotao = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 0));
        painelBotao.setBackground(Color.WHITE);
        painelBotao.add(botaoEntrar);

        gbc.gridy = 3;
        gbc.ipady = 0;
        painel.add(painelBotao, gbc);

        // ----- Ação do botão Entrar -----
        botaoEntrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String usuario = campoUsuario.getText().trim();
                String senha = new String(campoSenha.getPassword()).trim();

                if (usuario.isEmpty() || senha.isEmpty()) {
                    JOptionPane.showMessageDialog(
                            TelaLogin.this,
                            "Por favor, preencha o usuário e a senha.",
                            "Campos obrigatórios",
                            JOptionPane.WARNING_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(
                            TelaLogin.this,
                            "Login realizado com sucesso!\nUsuário: " + usuario,
                            "Bem-vindo!",
                            JOptionPane.INFORMATION_MESSAGE);

                    // Simulação de autenticação
                    if (usuario.equals("admin") && senha.equals("123")) {

                        JOptionPane.showMessageDialog(
                                TelaLogin.this,
                                "Login realizado com sucesso!",
                                "Bem-vindo!",
                                JOptionPane.INFORMATION_MESSAGE);

                        dispose(); // fecha a tela de login

                        new Dashboard(usuario); // abre o dashboard

                    } else {

                        JOptionPane.showMessageDialog(
                                TelaLogin.this,
                                "Usuário ou senha inválidos.",
                                "Erro de Login",
                                JOptionPane.ERROR_MESSAGE);
                    }
                }
            }
        });

        // Permite pressionar Enter para acionar o botão
        getRootPane().setDefaultButton(botaoEntrar);

        add(painel);
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaLogin());
    }
}
