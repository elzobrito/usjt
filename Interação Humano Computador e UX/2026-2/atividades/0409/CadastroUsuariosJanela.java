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
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.border.AbstractBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;

public class CadastroUsuariosJanela {

    public static void main(String[] args) {

        // Executa a criação da tela na thread de interface do Swing.
        SwingUtilities.invokeLater(CadastroUsuariosJanela::criarTela);
    }

    private static void criarTela() {

        // ---------------------------------------------------------
        // APARÊNCIA
        // ---------------------------------------------------------

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

        Color corFundo =
                new Color(245, 247, 250);

        Color corTexto =
                new Color(40, 40, 40);

        Color corBorda =
                new Color(205, 210, 218);

        Color corCadastrar =
                new Color(46, 125, 50);

        Color corExcluir =
                new Color(183, 28, 28);

        Color corSelecao =
                new Color(40, 90, 150);

        Color corSucesso =
                new Color(35, 110, 60);

        Color corErro =
                new Color(180, 40, 40);

        // ---------------------------------------------------------
        // MODELO DA TABELA
        // ---------------------------------------------------------

        /*
         * DefaultTableModel armazena os dados
         * que serão exibidos na JTable.
         *
         * As duas colunas serão:
         *
         * ID
         * Nome
         */
        DefaultTableModel modeloTabela =
                new DefaultTableModel(
                        new Object[]{"ID", "Nome"},
                        0
                ) {

                    /*
                     * Sobrescrevemos este método
                     * para impedir que o usuário
                     * edite diretamente as células.
                     */
                    @Override
                    public boolean isCellEditable(
                            int linha,
                            int coluna) {

                        return false;
                    }
                };

        // Adiciona os usuários iniciais.
        modeloTabela.addRow(
                new Object[]{1, "Ana"}
        );

        modeloTabela.addRow(
                new Object[]{2, "Carlos"}
        );

        // Próximo código de usuário.
        int[] proximoId = {3};

        // ---------------------------------------------------------
        // JANELA
        // ---------------------------------------------------------

        JFrame janela =
                new JFrame(
                        "Cadastro de usuários"
                );

        janela.setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE
        );

        janela.setLayout(
                new BorderLayout()
        );

        janela.getContentPane()
                .setBackground(corFundo);

        // ---------------------------------------------------------
        // PAINEL PRINCIPAL
        // ---------------------------------------------------------

        JPanel painelPrincipal =
                new JPanel(
                        new BorderLayout(
                                15,
                                15
                        )
                );

        painelPrincipal.setBackground(
                corFundo
        );

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

        titulo.setForeground(
                corTexto
        );

        titulo.setBorder(
                new EmptyBorder(
                        0,
                        0,
                        10,
                        0
                )
        );

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
        // RÓTULO
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

        rotuloNome.setLabelFor(
                campoNome
        );

        // Alt + N leva o foco para o campo.
        rotuloNome.setDisplayedMnemonic(
                'N'
        );

        campoNome.getAccessibleContext()
                .setAccessibleName(
                        "Nome do usuário"
                );

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

        // Alt + C
        botaoCadastrar.setMnemonic(
                'C'
        );

        botaoCadastrar
                .getAccessibleContext()
                .setAccessibleName(
                        "Cadastrar usuário"
                );

        botaoCadastrar
                .getAccessibleContext()
                .setAccessibleDescription(
                        "Adiciona o usuário à tabela."
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

        // Alt + E
        botaoExcluir.setMnemonic(
                'E'
        );

        botaoExcluir
                .getAccessibleContext()
                .setAccessibleName(
                        "Excluir usuário selecionado"
                );

        botaoExcluir
                .getAccessibleContext()
                .setAccessibleDescription(
                        "Remove da tabela o usuário selecionado."
                );

        botaoExcluir.setToolTipText(
                "Excluir o usuário selecionado"
        );

        // ---------------------------------------------------------
        // ADICIONA COMPONENTES AO FORMULÁRIO
        // ---------------------------------------------------------

        formulario.add(
                rotuloNome
        );

        formulario.add(
                campoNome
        );

        formulario.add(
                botaoCadastrar
        );

        formulario.add(
                botaoExcluir
        );

        // ---------------------------------------------------------
        // MENSAGEM
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

        mensagem.getAccessibleContext()
                .setAccessibleName(
                        "Mensagem de status"
                );

        mensagem.getAccessibleContext()
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
        // TABELA
        // ---------------------------------------------------------

        /*
         * Cria a tabela usando o modelo definido anteriormente.
         */
        JTable tabela =
                new JTable(
                        modeloTabela
                );

        tabela.setFont(
                new Font(
                        "SansSerif",
                        Font.PLAIN,
                        14
                )
        );

        /*
         * Define a altura das linhas.
         */
        tabela.setRowHeight(
                32
        );

        /*
         * Permite selecionar apenas
         * uma linha por vez.
         */
        tabela.setSelectionMode(
                ListSelectionModel.SINGLE_SELECTION
        );

        /*
         * Faz a seleção considerar
         * a linha inteira.
         */
        tabela.setRowSelectionAllowed(
                true
        );

        /*
         * Não permite selecionar
         * apenas uma célula individual.
         */
        tabela.setCellSelectionEnabled(
                false
        );

        /*
         * Define as cores utilizadas
         * na linha selecionada.
         */
        tabela.setSelectionBackground(
                corSelecao
        );

        tabela.setSelectionForeground(
                Color.WHITE
        );

        /*
         * Faz a tabela ocupar
         * toda a área disponível.
         */
        tabela.setFillsViewportHeight(
                true
        );

        /*
         * Impede que o usuário
         * reorganize as colunas.
         */
        tabela.getTableHeader()
                .setReorderingAllowed(
                        false
                );

        /*
         * Altera a fonte do cabeçalho.
         */
        tabela.getTableHeader()
                .setFont(
                        new Font(
                                "SansSerif",
                                Font.BOLD,
                                14
                        )
                );

        /*
         * Define uma largura menor
         * para a coluna ID.
         */
        tabela.getColumnModel()
                .getColumn(0)
                .setPreferredWidth(60);

        tabela.getColumnModel()
                .getColumn(0)
                .setMaxWidth(100);

        /*
         * Define uma largura maior
         * para a coluna Nome.
         */
        tabela.getColumnModel()
                .getColumn(1)
                .setPreferredWidth(400);

        // ---------------------------------------------------------
        // ACESSIBILIDADE DA TABELA
        // ---------------------------------------------------------

        tabela.getAccessibleContext()
                .setAccessibleName(
                        "Tabela de usuários cadastrados"
                );

        tabela.getAccessibleContext()
                .setAccessibleDescription(
                        "Tabela contendo o código e o nome dos usuários cadastrados."
                );

        tabela.setToolTipText(
                "Selecione uma linha para excluir um usuário"
        );

        // ---------------------------------------------------------
        // SCROLL DA TABELA
        // ---------------------------------------------------------

        JScrollPane rolagem =
                new JScrollPane(
                        tabela
                );

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
        // ORGANIZAÇÃO DA JANELA
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
        // ENTER CADASTRA
        // ---------------------------------------------------------

        /*
         * Permite cadastrar pressionando Enter.
         */
        janela.getRootPane()
                .setDefaultButton(
                        botaoCadastrar
                );

        // ---------------------------------------------------------
        // EVENTO CADASTRAR
        // ---------------------------------------------------------

        botaoCadastrar.addActionListener(
                evento -> {

                    /*
                     * Obtém o texto digitado
                     * e remove espaços extras.
                     */
                    String nome =
                            campoNome
                                    .getText()
                                    .strip();

                    /*
                     * Verifica se o campo está vazio.
                     */
                    if (nome.isEmpty()) {

                        definirMensagem(
                                mensagem,
                                "Erro: o campo nome é obrigatório.",
                                corErro
                        );

                        campoNome.requestFocusInWindow();

                        return;
                    }

                    /*
                     * Adiciona uma nova linha à tabela.
                     *
                     * Primeira coluna: ID
                     * Segunda coluna: nome
                     */
                    modeloTabela.addRow(
                            new Object[]{
                                    proximoId[0],
                                    nome
                            }
                    );

                    /*
                     * Incrementa o próximo ID.
                     */
                    proximoId[0] += 1;

                    /*
                     * Limpa o campo.
                     */
                    campoNome.setText("");

                    /*
                     * Exibe mensagem de sucesso.
                     */
                    definirMensagem(
                            mensagem,
                            "Sucesso: usuário cadastrado.",
                            corSucesso
                    );

                    /*
                     * Retorna o foco
                     * para o campo Nome.
                     */
                    campoNome.requestFocusInWindow();
                }
        );

        // ---------------------------------------------------------
        // EVENTO EXCLUIR
        // ---------------------------------------------------------

        botaoExcluir.addActionListener(
                evento -> {

                    /*
                     * Obtém o número da linha
                     * selecionada na tabela.
                     */
                    int linha =
                            tabela.getSelectedRow();

                    /*
                     * Caso nenhuma linha esteja selecionada,
                     * getSelectedRow() retorna -1.
                     */
                    if (linha < 0) {

                        definirMensagem(
                                mensagem,
                                "Erro: selecione um usuário na tabela.",
                                corErro
                        );

                        tabela.requestFocusInWindow();

                        return;
                    }

                    /*
                     * Remove a linha selecionada
                     * do modelo da tabela.
                     */
                    modeloTabela.removeRow(
                            linha
                    );

                    /*
                     * Exibe mensagem de sucesso.
                     */
                    definirMensagem(
                            mensagem,
                            "Sucesso: usuário excluído.",
                            corSucesso
                    );

                    /*
                     * Retorna o foco
                     * para o campo Nome.
                     */
                    campoNome.requestFocusInWindow();
                }
        );

        // ---------------------------------------------------------
        // CONFIGURAÇÕES FINAIS
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

        /*
         * Centraliza a janela.
         */
        janela.setLocationRelativeTo(
                null
        );

        /*
         * Exibe a janela.
         */
        janela.setVisible(
                true
        );

        /*
         * Coloca o foco inicial
         * no campo Nome.
         */
        campoNome.requestFocusInWindow();
    }

    // =========================================================
    // MÉTODO PARA MENSAGENS
    // =========================================================

    private static void definirMensagem(
            JLabel mensagem,
            String texto,
            Color cor) {

        mensagem.setText(
                texto
        );

        mensagem.setForeground(
                cor
        );

        /*
         * Atualiza também a descrição
         * utilizada pelas tecnologias assistivas.
         */
        mensagem.getAccessibleContext()
                .setAccessibleDescription(
                        texto
                );
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

            setForeground(
                    Color.WHITE
            );

            /*
             * O componente continua sendo um JButton,
             * portanto mantém comportamento de teclado
             * e recursos de acessibilidade.
             */
            setFocusable(
                    true
            );

            /*
             * Não utiliza o fundo padrão
             * do botão Swing.
             */
            setContentAreaFilled(
                    false
            );

            setOpaque(
                    false
            );

            /*
             * A borda será desenhada
             * pelo nosso próprio código.
             */
            setBorderPainted(
                    false
            );

            /*
             * O indicador de foco também
             * será desenhado manualmente.
             */
            setFocusPainted(
                    false
            );

            /*
             * Permite detectar quando
             * o mouse está sobre o botão.
             */
            setRolloverEnabled(
                    true
            );

            /*
             * Espaçamento interno.
             */
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

            Graphics2D g2 =
                    (Graphics2D) g.create();

            /*
             * Suaviza o desenho
             * das bordas arredondadas.
             */
            g2.setRenderingHint(
                    RenderingHints.KEY_ANTIALIASING,
                    RenderingHints.VALUE_ANTIALIAS_ON
            );

            /*
             * Altera a cor dependendo
             * do estado do botão.
             */
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

                g2.setColor(
                        cor
                );
            }

            /*
             * Desenha o fundo arredondado.
             */
            g2.fillRoundRect(
                    0,
                    0,
                    getWidth(),
                    getHeight(),
                    18,
                    18
            );

            // -------------------------------------------------
            // FOCO VISÍVEL
            // -------------------------------------------------

            if (hasFocus()) {

                g2.setColor(
                        Color.WHITE
                );

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

                /*
                 * Desenha uma linha pontilhada
                 * quando o botão possui foco.
                 */
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

            /*
             * Permite que o JButton
             * desenhe seu texto normalmente.
             */
            super.paintComponent(
                    g
            );
        }
    }

    // =========================================================
    // PAINEL ARREDONDADO
    // =========================================================

    static class PainelArredondado
            extends JPanel {

        private final int raio;

        private final Color corFundo;

        public PainelArredondado(
                int raio,
                Color corFundo) {

            this.raio =
                    raio;

            this.corFundo =
                    corFundo;

            setOpaque(
                    false
            );
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

            /*
             * Desenha o fundo arredondado
             * do painel.
             */
            g2.setColor(
                    corFundo
            );

            g2.fillRoundRect(
                    0,
                    0,
                    getWidth(),
                    getHeight(),
                    raio,
                    raio
            );

            g2.dispose();

            super.paintComponent(
                    g
            );
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

            this.cor =
                    cor;

            this.raio =
                    raio;
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

            g2.setColor(
                    cor
            );

            /*
             * Desenha a borda arredondada.
             */
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