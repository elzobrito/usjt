import java.awt.BasicStroke;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Insets;
import java.awt.RenderingHints;

import javax.swing.BorderFactory;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.border.AbstractBorder;
import javax.swing.border.EmptyBorder;

public class CadastroUsuariosJanela {

    public static void main(String[] args) {

        // Executa a criação da interface na thread apropriada do Swing.
        SwingUtilities.invokeLater(CadastroUsuariosJanela::criarTela);
    }


    private static void criarTela() {

        // ---------------------------------------------------------
        // APARÊNCIA DO SWING
        // ---------------------------------------------------------

        // Tenta utilizar o tema Nimbus, caso esteja disponível.
        try {

            for (UIManager.LookAndFeelInfo info
                    : UIManager.getInstalledLookAndFeels()) {

                if ("Nimbus".equals(info.getName())) {

                    UIManager.setLookAndFeel(
                            info.getClassName()
                    );

                    break;
                }
            }

        } catch (Exception erro) {

            System.out.println(
                    "Não foi possível aplicar o tema Nimbus."
            );
        }


        // ---------------------------------------------------------
        // CORES
        // ---------------------------------------------------------

        Color corFundo = new Color(245, 247, 250);

        Color corTexto = new Color(40, 40, 40);

        Color corBorda = new Color(205, 210, 218);

        // Verde do botão Cadastrar.
        Color corCadastrar = new Color(46, 125, 50);

        // Vermelho do botão Excluir.
        Color corExcluir = new Color(183, 28, 28);

        // Azul utilizado na seleção da lista.
        Color corSelecao = new Color(40, 90, 150);

        // Verde usado nas mensagens de sucesso.
        Color corSucesso = new Color(35, 110, 60);

        // Vermelho usado nas mensagens de erro.
        Color corErro = new Color(180, 40, 40);


        // ---------------------------------------------------------
        // DADOS DOS USUÁRIOS
        // ---------------------------------------------------------

        // Cria o modelo que armazenará os usuários da lista.
        DefaultListModel<String> usuarios =
                new DefaultListModel<>();

        // Adiciona usuários iniciais.
        usuarios.addElement("1 — Ana");
        usuarios.addElement("2 — Carlos");

        // Guarda o ID que será utilizado no próximo cadastro.
        int[] proximoId = {3};


        // ---------------------------------------------------------
        // JANELA PRINCIPAL
        // ---------------------------------------------------------

        JFrame janela =
                new JFrame("Cadastro de usuários");

        // Encerra o programa quando a janela for fechada.
        janela.setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE
        );

        // Define o layout principal.
        janela.setLayout(
                new BorderLayout()
        );

        // Define a cor de fundo.
        janela.getContentPane()
                .setBackground(corFundo);


        // ---------------------------------------------------------
        // PAINEL PRINCIPAL
        // ---------------------------------------------------------

        JPanel painelPrincipal =
                new JPanel(
                        new BorderLayout(15, 15)
                );

        painelPrincipal.setBackground(corFundo);

        // Cria espaço ao redor de todo o conteúdo.
        painelPrincipal.setBorder(
                new EmptyBorder(
                        20,
                        25,
                        20,
                        25
                )
        );


        // ---------------------------------------------------------
        // TÍTULO
        // ---------------------------------------------------------

        JLabel titulo =
                new JLabel(
                        "Cadastro de usuários",
                        SwingConstants.CENTER
                );

        titulo.setFont(
                new Font(
                        "SansSerif",
                        Font.BOLD,
                        24
                )
        );

        titulo.setForeground(corTexto);

        titulo.setBorder(
                new EmptyBorder(
                        0,
                        0,
                        10,
                        0
                )
        );

        // Nome acessível para leitores de tela.
        titulo.getAccessibleContext()
                .setAccessibleName(
                        "Cadastro de usuários"
                );


        // ---------------------------------------------------------
        // FORMULÁRIO
        // ---------------------------------------------------------

        PainelArredondado formulario =
                new PainelArredondado(
                        18,
                        Color.WHITE
                );

        formulario.setLayout(
                new FlowLayout(
                        FlowLayout.LEFT,
                        10,
                        12
                )
        );

        formulario.setBorder(
                new EmptyBorder(
                        8,
                        10,
                        8,
                        10
                )
        );


        // ---------------------------------------------------------
        // RÓTULO NOME
        // ---------------------------------------------------------

        JLabel rotuloNome =
                new JLabel("Nome:");

        rotuloNome.setFont(
                new Font(
                        "SansSerif",
                        Font.BOLD,
                        14
                )
        );


        // ---------------------------------------------------------
        // CAMPO NOME
        // ---------------------------------------------------------

        JTextField campoNome =
                new JTextField(20);

        campoNome.setFont(
                new Font(
                        "SansSerif",
                        Font.PLAIN,
                        14
                )
        );

        campoNome.setPreferredSize(
                new Dimension(
                        220,
                        36
                )
        );

        // Cria uma borda arredondada no campo.
        campoNome.setBorder(
                BorderFactory.createCompoundBorder(

                        new BordaArredondada(
                                corBorda,
                                12
                        ),

                        new EmptyBorder(
                                5,
                                10,
                                5,
                                10
                        )
                )
        );


        // ---------------------------------------------------------
        // ACESSIBILIDADE DO CAMPO
        // ---------------------------------------------------------

        // Informa que o rótulo "Nome" pertence ao campo.
        rotuloNome.setLabelFor(campoNome);

        // Alt + N coloca o foco no campo Nome.
        rotuloNome.setDisplayedMnemonic('N');

        // Nome utilizado por tecnologias assistivas.
        campoNome.getAccessibleContext()
                .setAccessibleName(
                        "Nome do usuário"
                );

        // Explica a finalidade do campo.
        campoNome.getAccessibleContext()
                .setAccessibleDescription(
                        "Digite o nome do usuário que será cadastrado."
                );

        campoNome.setToolTipText(
                "Digite o nome do usuário"
        );


        // ---------------------------------------------------------
        // BOTÃO CADASTRAR
        // ---------------------------------------------------------

        JButton botaoCadastrar =
                new BotaoArredondado(
                        "Cadastrar",
                        corCadastrar
                );

        // Alt + C aciona o botão.
        botaoCadastrar.setMnemonic('C');

        botaoCadastrar
                .getAccessibleContext()
                .setAccessibleName(
                        "Cadastrar usuário"
                );

        botaoCadastrar
                .getAccessibleContext()
                .setAccessibleDescription(
                        "Adiciona o nome digitado à lista de usuários."
                );

        botaoCadastrar.setToolTipText(
                "Cadastrar novo usuário"
        );


        // ---------------------------------------------------------
        // BOTÃO EXCLUIR
        // ---------------------------------------------------------

        JButton botaoExcluir =
                new BotaoArredondado(
                        "Excluir selecionado",
                        corExcluir
                );

        // Alt + E aciona o botão.
        botaoExcluir.setMnemonic('E');

        botaoExcluir
                .getAccessibleContext()
                .setAccessibleName(
                        "Excluir usuário selecionado"
                );

        botaoExcluir
                .getAccessibleContext()
                .setAccessibleDescription(
                        "Remove da lista o usuário atualmente selecionado."
                );

        botaoExcluir.setToolTipText(
                "Excluir o usuário selecionado"
        );


        // ---------------------------------------------------------
        // ADICIONA OS COMPONENTES AO FORMULÁRIO
        // ---------------------------------------------------------

        formulario.add(rotuloNome);

        formulario.add(campoNome);

        formulario.add(botaoCadastrar);

        formulario.add(botaoExcluir);


        // ---------------------------------------------------------
        // MENSAGENS
        // ---------------------------------------------------------

        JLabel mensagem =
                new JLabel(" ");

        mensagem.setFont(
                new Font(
                        "SansSerif",
                        Font.PLAIN,
                        13
                )
        );

        mensagem.setForeground(
                new Color(70, 70, 70)
        );

        mensagem.setBorder(
                new EmptyBorder(
                        3,
                        5,
                        3,
                        5
                )
        );

        // Informa às tecnologias assistivas
        // que esse componente apresenta mensagens.
        mensagem
                .getAccessibleContext()
                .setAccessibleName(
                        "Mensagem de status"
                );

        mensagem
                .getAccessibleContext()
                .setAccessibleDescription(
                        "Apresenta mensagens de erro ou confirmação."
                );


        // ---------------------------------------------------------
        // PAINEL SUPERIOR
        // ---------------------------------------------------------

        JPanel painelSuperior =
                new JPanel(
                        new BorderLayout(
                                8,
                                8
                        )
                );

        painelSuperior.setBackground(
                corFundo
        );

        painelSuperior.add(
                titulo,
                BorderLayout.NORTH
        );

        painelSuperior.add(
                formulario,
                BorderLayout.CENTER
        );

        painelSuperior.add(
                mensagem,
                BorderLayout.SOUTH
        );


        // ---------------------------------------------------------
        // LISTA DE USUÁRIOS
        // ---------------------------------------------------------

        JList<String> lista =
                new JList<>(usuarios);

        lista.setFont(
                new Font(
                        "SansSerif",
                        Font.PLAIN,
                        15
                )
        );

        // Permite selecionar apenas um usuário.
        lista.setSelectionMode(
                ListSelectionModel.SINGLE_SELECTION
        );

        // Define a altura de cada linha.
        lista.setFixedCellHeight(34);

        lista.setBackground(Color.WHITE);

        lista.setForeground(corTexto);

        lista.setSelectionBackground(
                corSelecao
        );

        lista.setSelectionForeground(
                Color.WHITE
        );

        lista.setBorder(
                new EmptyBorder(
                        8,
                        10,
                        8,
                        10
                )
        );


        // ---------------------------------------------------------
        // ACESSIBILIDADE DA LISTA
        // ---------------------------------------------------------

        lista.getAccessibleContext()
                .setAccessibleName(
                        "Usuários cadastrados"
                );

        lista.getAccessibleContext()
                .setAccessibleDescription(
                        "Lista contendo os usuários cadastrados no sistema."
                );

        lista.setToolTipText(
                "Selecione um usuário para excluí-lo"
        );


        // ---------------------------------------------------------
        // BARRA DE ROLAGEM
        // ---------------------------------------------------------

        JScrollPane rolagem =
                new JScrollPane(lista);

        rolagem.setBorder(
                BorderFactory.createCompoundBorder(

                        BorderFactory.createTitledBorder(
                                "Usuários cadastrados"
                        ),

                        new EmptyBorder(
                                4,
                                4,
                                4,
                                4
                        )
                )
        );


        // ---------------------------------------------------------
        // ORGANIZAÇÃO DA INTERFACE
        // ---------------------------------------------------------

        painelPrincipal.add(
                painelSuperior,
                BorderLayout.NORTH
        );

        painelPrincipal.add(
                rolagem,
                BorderLayout.CENTER
        );

        janela.add(
                painelPrincipal
        );


        // ---------------------------------------------------------
        // ACESSIBILIDADE:
        // ENTER EXECUTA CADASTRAR
        // ---------------------------------------------------------

        // Define o botão Cadastrar como botão padrão.
        //
        // Assim, após digitar o nome,
        // basta pressionar Enter.
        janela.getRootPane()
                .setDefaultButton(
                        botaoCadastrar
                );


        // ---------------------------------------------------------
        // EVENTO: CADASTRAR
        // ---------------------------------------------------------

        botaoCadastrar.addActionListener(
                evento -> {

                    // Obtém o nome digitado.
                    String nome =
                            campoNome
                                    .getText()
                                    .strip();


                    // Verifica se o campo está vazio.
                    if (nome.isEmpty()) {

                        definirMensagem(
                                mensagem,
                                "Erro: o campo nome é obrigatório.",
                                corErro
                        );

                        // Retorna o foco ao campo.
                        campoNome.requestFocusInWindow();

                        return;
                    }


                    // Adiciona o usuário à lista.
                    usuarios.addElement(
                            proximoId[0]
                                    + " — "
                                    + nome
                    );


                    // Incrementa o próximo ID.
                    proximoId[0] += 1;


                    // Limpa o campo.
                    campoNome.setText("");


                    // Informa que a operação funcionou.
                    definirMensagem(
                            mensagem,
                            "Sucesso: usuário cadastrado.",
                            corSucesso
                    );


                    // Retorna o foco ao campo.
                    campoNome.requestFocusInWindow();
                }
        );


        // ---------------------------------------------------------
        // EVENTO: EXCLUIR
        // ---------------------------------------------------------

        botaoExcluir.addActionListener(
                evento -> {

                    // Obtém o índice selecionado.
                    int indice =
                            lista.getSelectedIndex();


                    // Nenhum item selecionado retorna -1.
                    if (indice < 0) {

                        definirMensagem(
                                mensagem,
                                "Erro: selecione um usuário na lista.",
                                corErro
                        );

                        // Coloca o foco na lista.
                        lista.requestFocusInWindow();

                        return;
                    }


                    // Remove o usuário.
                    usuarios.remove(indice);


                    // Exibe a confirmação.
                    definirMensagem(
                            mensagem,
                            "Sucesso: usuário excluído.",
                            corSucesso
                    );


                    // Retorna o foco ao campo de nome.
                    campoNome.requestFocusInWindow();
                }
        );


        // ---------------------------------------------------------
        // CONFIGURAÇÕES FINAIS DA JANELA
        // ---------------------------------------------------------

        janela.setSize(
                670,
                430
        );

        janela.setMinimumSize(
                new Dimension(
                        620,
                        380
                )
        );

        // Centraliza a janela na tela.
        janela.setLocationRelativeTo(null);

        // Torna a janela visível.
        janela.setVisible(true);

        // Coloca inicialmente o foco no campo Nome.
        campoNome.requestFocusInWindow();
    }


    // =========================================================
    // MÉTODO PARA EXIBIR MENSAGENS
    // =========================================================

    private static void definirMensagem(
            JLabel mensagem,
            String texto,
            Color cor) {

        // Altera o texto apresentado na tela.
        mensagem.setText(texto);

        // Altera a cor visual.
        mensagem.setForeground(cor);

        // Atualiza também a informação usada
        // pelas tecnologias assistivas.
        mensagem
                .getAccessibleContext()
                .setAccessibleDescription(texto);
    }


    // =========================================================
    // BOTÃO ARREDONDADO
    // =========================================================

    static class BotaoArredondado
            extends JButton {

        private final Color cor;


        public BotaoArredondado(
                String texto,
                Color cor) {

            super(texto);

            this.cor = cor;


            setFont(
                    new Font(
                            "SansSerif",
                            Font.BOLD,
                            13
                    )
            );

            setForeground(Color.WHITE);

            // O botão continua podendo receber
            // foco pelo teclado.
            setFocusable(true);

            // A área padrão do Swing não será desenhada,
            // pois criaremos nossa própria aparência.
            setContentAreaFilled(false);

            setOpaque(false);

            // A borda será desenhada manualmente.
            setBorderPainted(false);

            // O foco padrão não será utilizado.
            // A classe desenhará um foco personalizado
            // e mais visível.
            setFocusPainted(false);

            // Ativa o comportamento de mouse sobre o botão.
            setRolloverEnabled(true);

            // Cria espaço interno no botão.
            setBorder(
                    new EmptyBorder(
                            9,
                            16,
                            9,
                            16
                    )
            );
        }


        @Override
        protected void paintComponent(
                Graphics g) {

            // Cria uma cópia do objeto gráfico.
            Graphics2D g2 =
                    (Graphics2D) g.create();


            // Suaviza as bordas arredondadas.
            g2.setRenderingHint(
                    RenderingHints.KEY_ANTIALIASING,
                    RenderingHints.VALUE_ANTIALIAS_ON
            );


            // Define a cor conforme o estado do botão.
            if (getModel().isPressed()) {

                g2.setColor(
                        cor.darker().darker()
                );

            } else if (
                    getModel().isRollover()) {

                g2.setColor(
                        cor.darker()
                );

            } else {

                g2.setColor(cor);
            }


            // Desenha o fundo arredondado.
            g2.fillRoundRect(
                    0,
                    0,
                    getWidth(),
                    getHeight(),
                    18,
                    18
            );


            // -------------------------------------------------
            // INDICAÇÃO VISUAL DE FOCO
            // -------------------------------------------------

            // Se o botão estiver com foco,
            // desenha uma borda branca pontilhada.
            //
            // Isso é importante para quem navega
            // utilizando apenas o teclado.
            if (hasFocus()) {

                g2.setColor(Color.WHITE);

                g2.setStroke(
                        new BasicStroke(
                                2,
                                BasicStroke.CAP_ROUND,
                                BasicStroke.JOIN_ROUND,
                                0,
                                new float[]{4, 3},
                                0
                        )
                );

                g2.drawRoundRect(
                        4,
                        4,
                        getWidth() - 9,
                        getHeight() - 9,
                        13,
                        13
                );
            }


            g2.dispose();


            // Solicita ao JButton que desenhe
            // o texto normalmente.
            super.paintComponent(g);
        }
    }


    // =========================================================
    // PAINEL COM FUNDO ARREDONDADO
    // =========================================================

    static class PainelArredondado
            extends JPanel {

        private final int raio;

        private final Color corFundo;


        public PainelArredondado(
                int raio,
                Color corFundo) {

            this.raio = raio;

            this.corFundo = corFundo;

            // Impede o JPanel de desenhar
            // seu fundo retangular tradicional.
            setOpaque(false);
        }


        @Override
        protected void paintComponent(
                Graphics g) {

            Graphics2D g2 =
                    (Graphics2D) g.create();


            g2.setRenderingHint(
                    RenderingHints.KEY_ANTIALIASING,
                    RenderingHints.VALUE_ANTIALIAS_ON
            );


            // Desenha o fundo arredondado.
            g2.setColor(corFundo);

            g2.fillRoundRect(
                    0,
                    0,
                    getWidth(),
                    getHeight(),
                    raio,
                    raio
            );


            g2.dispose();


            super.paintComponent(g);
        }
    }


    // =========================================================
    // BORDA ARREDONDADA
    // =========================================================

    static class BordaArredondada
            extends AbstractBorder {

        private final Color cor;

        private final int raio;


        public BordaArredondada(
                Color cor,
                int raio) {

            this.cor = cor;

            this.raio = raio;
        }


        @Override
        public void paintBorder(
                Component componente,
                Graphics g,
                int x,
                int y,
                int largura,
                int altura) {

            Graphics2D g2 =
                    (Graphics2D) g.create();


            g2.setRenderingHint(
                    RenderingHints.KEY_ANTIALIASING,
                    RenderingHints.VALUE_ANTIALIAS_ON
            );


            g2.setColor(cor);


            // Desenha a borda arredondada.
            g2.drawRoundRect(
                    x,
                    y,
                    largura - 1,
                    altura - 1,
                    raio,
                    raio
            );


            g2.dispose();
        }


        @Override
        public Insets getBorderInsets(
                Component componente) {

            return new Insets(
                    6,
                    8,
                    6,
                    8
            );
        }


        @Override
        public Insets getBorderInsets(
                Component componente,
                Insets insets) {

            insets.top = 6;
            insets.left = 8;
            insets.bottom = 6;
            insets.right = 8;

            return insets;
        }
    }
}