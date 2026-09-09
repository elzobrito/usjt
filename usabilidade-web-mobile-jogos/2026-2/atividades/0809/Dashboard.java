import javax.swing.*;
import java.awt.*;

public class Dashboard extends JFrame {

    public Dashboard(String usuario) {

        setTitle("Sistema Acadêmico");
        setSize(1024, 600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        JPanel menu = new JPanel();
        menu.setPreferredSize(new Dimension(220, 0));
        menu.setBackground(new Color(30, 60, 120));

        menu.setLayout(new GridLayout(6, 1, 10, 10));

        JButton btnAlunos = new JButton("Alunos");
        JButton btnProfessores = new JButton("Professores");
        JButton btnTurmas = new JButton("Turmas");
        JButton btnRelatorios = new JButton("Relatórios");
        JButton btnSair = new JButton("Sair");

        menu.add(btnAlunos);
        menu.add(btnProfessores);
        menu.add(btnTurmas);
        menu.add(btnRelatorios);
        menu.add(btnSair);

        JPanel conteudo = new JPanel(new BorderLayout());

        JLabel lblUsuario = new JLabel(
                "Usuário logado: " + usuario,
                SwingConstants.CENTER);

        lblUsuario.setFont(new Font("SansSerif", Font.BOLD, 22));

        conteudo.add(lblUsuario, BorderLayout.CENTER);

        setLayout(new BorderLayout());
        add(menu, BorderLayout.WEST);
        add(conteudo, BorderLayout.CENTER);

        btnSair.addActionListener(e -> {
            dispose();
            new TelaLogin();
        });

        setVisible(true);
    }
}