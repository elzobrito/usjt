import java.awt.Color;
import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.table.DefaultTableModel;

public class CadastroUsuariosComProblemas {

    public static void main(String[] args) {

        SwingUtilities.invokeLater(
                CadastroUsuariosComProblemas::criarTela
        );
    }


    private static void criarTela() {

        // ---------------------------------------------------------
        // JANELA
        // ---------------------------------------------------------

        JFrame janela = new JFrame("Sistema");

        janela.setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE
        );

        // Layout absoluto.
        janela.setLayout(null);


        // ---------------------------------------------------------
        // TÍTULO
        // ---------------------------------------------------------

        JLabel titulo = new JLabel(
                "CADASTRO"
        );

        titulo.setBounds(
                10,
                5,
                100,
                20
        );

        titulo.setFont(
                new Font(
                        "Arial",
                        Font.PLAIN,
                        11
                )
        );


        // ---------------------------------------------------------
        // RÓTULO
        // ---------------------------------------------------------

        JLabel rotuloNome = new JLabel(
                "N:"
        );

        rotuloNome.setBounds(
                10,
                40,
                20,
                20
        );


        // ---------------------------------------------------------
        // CAMPO NOME
        // ---------------------------------------------------------

        JTextField campoNome =
                new JTextField();

        campoNome.setBounds(
                30,
                40,
                110,
                22
        );


        // ---------------------------------------------------------
        // BOTÃO CADASTRAR
        // ---------------------------------------------------------

        JButton botaoCadastrar =
                new JButton("OK");

        botaoCadastrar.setBounds(
                150,
                40,
                60,
                22
        );

        // Cor vermelha para cadastrar.
        botaoCadastrar.setBackground(
                Color.RED
        );

        botaoCadastrar.setForeground(
                Color.BLACK
        );

        // Impede que o botão receba foco pelo teclado.
        botaoCadastrar.setFocusable(false);


        // ---------------------------------------------------------
        // BOTÃO EXCLUIR
        // ---------------------------------------------------------

        JButton botaoExcluir =
                new JButton("X");

        botaoExcluir.setBounds(
                215,
                40,
                45,
                22
        );

        // Cor verde para excluir.
        botaoExcluir.setBackground(
                Color.GREEN
        );

        botaoExcluir.setForeground(
                Color.WHITE
        );

        botaoExcluir.setFocusable(false);


        // ---------------------------------------------------------
        // MENSAGEM
        // ---------------------------------------------------------

        JLabel mensagem =
                new JLabel("");

        mensagem.setBounds(
                270,
                40,
                120,
                20
        );

        mensagem.setFont(
                new Font(
                        "Arial",
                        Font.PLAIN,
                        9
                )
        );


        // ---------------------------------------------------------
        // TABELA
        // ---------------------------------------------------------

        DefaultTableModel modeloTabela =
                new DefaultTableModel(
                        new Object[]{
                                "Código",
                                "Dados"
                        },
                        0
                );

        modeloTabela.addRow(
                new Object[]{
                        1,
                        "Ana"
                }
        );

        modeloTabela.addRow(
                new Object[]{
                        2,
                        "Carlos"
                }
        );


        JTable tabela =
                new JTable(
                        modeloTabela
                );

        tabela.setFont(
                new Font(
                        "Arial",
                        Font.PLAIN,
                        10
                )
        );

        tabela.setRowHeight(18);


        JScrollPane rolagem =
                new JScrollPane(
                        tabela
                );

        rolagem.setBounds(
                10,
                80,
                380,
                120
        );


        // ---------------------------------------------------------
        // PRÓXIMO ID
        // ---------------------------------------------------------

        int[] proximoId = {3};


        // ---------------------------------------------------------
        // EVENTO CADASTRAR
        // ---------------------------------------------------------

        botaoCadastrar.addActionListener(
                evento -> {

                    String nome =
                            campoNome.getText();

                    modeloTabela.addRow(
                            new Object[]{
                                    proximoId[0],
                                    nome
                            }
                    );

                    proximoId[0]++;

                    mensagem.setForeground(
                            Color.GREEN
                    );

                    mensagem.setText(
                            "OK"
                    );
                }
        );


        // ---------------------------------------------------------
        // EVENTO EXCLUIR
        // ---------------------------------------------------------

        botaoExcluir.addActionListener(
                evento -> {

                    int linha =
                            tabela.getSelectedRow();

                    modeloTabela.removeRow(
                            linha
                    );

                    mensagem.setForeground(
                            Color.RED
                    );

                    mensagem.setText(
                            "X"
                    );
                }
        );


        // ---------------------------------------------------------
        // ADICIONA OS COMPONENTES
        // ---------------------------------------------------------

        janela.add(titulo);

        janela.add(rotuloNome);

        janela.add(campoNome);

        janela.add(botaoCadastrar);

        janela.add(botaoExcluir);

        janela.add(mensagem);

        janela.add(rolagem);


        // ---------------------------------------------------------
        // CONFIGURAÇÃO FINAL
        // ---------------------------------------------------------

        janela.setSize(
                420,
                250
        );

        janela.setResizable(false);

        janela.setVisible(true);
    }
}