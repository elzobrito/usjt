// Organiza componentes em cinco regiões: NORTH, SOUTH, EAST, WEST e CENTER.
import java.awt.BorderLayout;

// Permite alternar entre painéis, exibindo um deles por vez.
import java.awt.CardLayout;

// Representa uma dimensão formada por largura e altura.
import java.awt.Dimension;

// Define as regras de posicionamento de um componente no GridBagLayout.
import java.awt.GridBagConstraints;

// Organiza componentes em uma grade flexível de linhas e colunas.
import java.awt.GridBagLayout;

// Representa os espaçamentos superior, esquerdo, inferior e direito.
import java.awt.Insets;

// Implementa um mapa que preserva a ordem de inserção das chaves.
import java.util.LinkedHashMap;

// Representa uma estrutura de pares de chave e valor.
import java.util.Map;

// Disponibiliza métodos para criar bordas nos componentes Swing.
import javax.swing.BorderFactory;

// Agrupa botões de opção para permitir apenas uma seleção por vez.
import javax.swing.ButtonGroup;

// Representa um botão que pode executar uma ação.
import javax.swing.JButton;

// Representa uma caixa de seleção com uma lista de opções.
import javax.swing.JComboBox;

// Representa a janela principal da aplicação.
import javax.swing.JFrame;

// Exibe um texto ou uma imagem na interface.
import javax.swing.JLabel;

// Representa um contêiner que agrupa outros componentes.
import javax.swing.JPanel;

// Representa um botão de opção.
import javax.swing.JRadioButton;

// Representa um campo de entrada de texto de uma linha.
import javax.swing.JTextField;

// Disponibiliza utilitários, como executar tarefas na thread de eventos do Swing.
import javax.swing.SwingUtilities;

/**
 * Aplicação didática para explorar ergonomia cognitiva em Java/Swing.
 *
 * A interface apresenta duas condições de preenchimento:
 *
 * A — códigos:
 * O usuário digita códigos e uma descrição em campos de texto.
 *
 * B — reconhecimento:
 * O usuário seleciona informações em listas de opções.
 *
 * O programa também permite:
 * - Simular uma interrupção durante o preenchimento.
 * - Verificar se os dados correspondem ao registro solicitado.
 * - Direcionar o foco ao primeiro campo que precisa de revisão.
 * - Limpar os dois formulários.
 * - Executar testes básicos sem abrir a interface.
 *
 * Os dados permanecem apenas na memória durante a execução.
 * Não há gravação em arquivo ou banco de dados.
 *
 * Observação: Map.of(), usado nos testes, requer Java 9 ou superior.
 */
public class ErgonomiaJava {

    // Cria a janela principal e define o texto de sua barra de título.
    // private: o atributo só pode ser acessado diretamente dentro desta classe.
    // final: a referência não pode ser substituída após a inicialização.
    // O objeto JFrame continua podendo ser modificado normalmente.
    private final JFrame frame =
        new JFrame("Ergonomia da interação — Java/Swing");

    // Gerenciador que controla qual formulário fica visível.
    private final CardLayout cards = new CardLayout();

    // Painel que armazena os formulários A e B usando o CardLayout.
    private final JPanel formCards = new JPanel(cards);

    // Rótulo inicialmente vazio; receberá as instruções da condição selecionada.
    private final JLabel instruction = new JLabel();

    // Rótulo que apresenta mensagens de orientação e resultados da validação.
    // O texto inicial será substituído por showMode("A") durante a montagem.
    private final JLabel status =
        new JLabel("Nenhuma tentativa registrada.");

    // Associa o identificador de cada campo A ao respectivo JTextField.
    // Exemplo: "predio" -> campo de texto do prédio.
    // LinkedHashMap mantém a ordem em que os campos foram adicionados.
    private final Map<String, JTextField> fieldsA = new LinkedHashMap<>();

    // Associa o identificador de cada campo B ao respectivo JComboBox.
    // JComboBox<String> indica que as opções da lista são textos.
    private final Map<String, JComboBox<String>> fieldsB =
        new LinkedHashMap<>();

    // Armazena a condição atual da interface.
    // Diferentemente dos atributos final, este atributo recebe novas referências.
    private String mode = "A";

    /**
     * Construtor da aplicação.
     *
     * É privado porque a criação da instância ocorre dentro da própria classe,
     * a partir do método main.
     */
    private ErgonomiaJava() {

        // Monta os componentes, configura os eventos e exibe a janela.
        buildUi();
    }

    /**
     * Constrói a interface gráfica e associa ações aos botões.
     */
    private void buildUi() {

        // Encerra a aplicação quando o usuário fecha a janela.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Define o layout da janela.
        // Os valores 10 e 10 indicam os espaços horizontal e vertical
        // entre os componentes das regiões do BorderLayout.
        frame.setLayout(new BorderLayout(10, 10));

        // Cria o painel superior.
        // JPanel usa FlowLayout por padrão, organizando os componentes
        // em sequência e podendo quebrar a linha quando falta espaço.
        JPanel toolbar = new JPanel();

        // Cria a opção A e a deixa selecionada inicialmente.
        JRadioButton modeA = new JRadioButton("A — códigos", true);

        // Cria a opção B, inicialmente desmarcada.
        JRadioButton modeB = new JRadioButton("B — reconhecimento");

        // Cria um grupo lógico para tornar as opções mutuamente exclusivas.
        // ButtonGroup controla a seleção, mas não é um painel visual.
        ButtonGroup modes = new ButtonGroup();

        // Inclui a opção A no grupo.
        modes.add(modeA);

        // Inclui a opção B no mesmo grupo.
        modes.add(modeB);

        // Cria o botão usado para simular uma interrupção.
        JButton interrupt = new JButton("Simular interrupção");

        // Adiciona o texto explicativo ao painel superior.
        toolbar.add(new JLabel("Condição:"));

        // Adiciona os controles ao painel, na ordem em que devem aparecer.
        toolbar.add(modeA);
        toolbar.add(modeB);
        toolbar.add(interrupt);

        // Posiciona o painel de controles no topo da janela.
        frame.add(toolbar, BorderLayout.NORTH);

        // Cria o painel central com espaçamento de 8 pixels entre suas regiões.
        JPanel center = new JPanel(new BorderLayout(8, 8));

        // Cria uma borda invisível para afastar o conteúdo das extremidades.
        // Ordem dos valores: superior, esquerda, inferior e direita.
        center.setBorder(
            BorderFactory.createEmptyBorder(8, 18, 8, 18)
        );

        // Posiciona as instruções acima dos formulários.
        center.add(instruction, BorderLayout.NORTH);

        // Constrói o formulário A e o identifica com o nome "A".
        formCards.add(buildFormA(), "A");

        // Constrói o formulário B e o identifica com o nome "B".
        formCards.add(buildFormB(), "B");

        // Adiciona o painel de formulários ao centro.
        // O CardLayout exibirá apenas um formulário por vez.
        center.add(formCards, BorderLayout.CENTER);

        // Cria o painel que agrupa os botões de ação.
        JPanel actions = new JPanel();

        // Cria o botão que verifica o preenchimento do formulário atual.
        JButton confirm = new JButton("Confirmar registro");

        // Cria o botão que limpa os dois formulários.
        JButton clear = new JButton("Limpar");

        // Adiciona os botões ao painel de ações.
        actions.add(confirm);
        actions.add(clear);

        // Posiciona as ações abaixo dos formulários.
        center.add(actions, BorderLayout.SOUTH);

        // Adiciona o conjunto central à janela principal.
        frame.add(center, BorderLayout.CENTER);

        // Define um espaçamento ao redor da mensagem de status.
        status.setBorder(
            BorderFactory.createEmptyBorder(8, 18, 14, 18)
        );

        // Posiciona a mensagem de status na parte inferior da janela.
        frame.add(status, BorderLayout.SOUTH);

        // Registra a ação executada quando o usuário seleciona a condição A.
        // A expressão lambda "e -> ..." representa o tratamento do evento.
        // O parâmetro e contém o evento recebido, mas não é usado neste caso.
        modeA.addActionListener(e -> showMode("A"));

        // Registra a ação executada quando o usuário seleciona a condição B.
        modeB.addActionListener(e -> showMode("B"));

        // Registra a ação do botão de interrupção.
        // As chaves permitem executar mais de uma instrução na lambda.
        interrupt.addActionListener(e -> {

            // Apresenta uma orientação para uma pausa simulada.
            // O programa não usa temporizador nem bloqueia a interface.
            status.setText(
                "Interrupção: o telefone tocou. Conte até cinco e retome a tarefa."
            );

            // Solicita o foco do teclado para o botão de interrupção.
            // Os valores dos campos permanecem preservados nos dois modos.
            interrupt.requestFocusInWindow();
        });

        // Ao clicar em confirmar, chama o método confirm().
        confirm.addActionListener(e -> confirm());

        // Ao clicar em limpar, chama o método clear().
        clear.addActionListener(e -> clear());

        // Seleciona o formulário A e atualiza as instruções e o status.
        showMode("A");

        // Define a dimensão mínima da janela em pixels: largura e altura.
        frame.setMinimumSize(new Dimension(760, 520));

        // Calcula o tamanho da janela com base nas dimensões preferidas
        // dos componentes e respeitando o tamanho mínimo configurado.
        frame.pack();

        // Centraliza a janela na tela.
        frame.setLocationRelativeTo(null);

        // Torna a janela visível para o usuário.
        frame.setVisible(true);
    }

    /**
     * Constrói o formulário A com campos de digitação.
     *
     * @return painel com os quatro campos da condição A.
     */
    private JPanel buildFormA() {

        // Cria um painel com a estrutura visual comum aos formulários.
        JPanel panel = formPanel();

        // Adiciona o campo do prédio na primeira linha, cujo índice é zero.
        addTextField(panel, fieldsA, 0, "predio", "1. Prédio/código");

        // Adiciona o campo da categoria na segunda linha.
        addTextField(panel, fieldsA, 1, "categoria", "2. Categoria/código");

        // Adiciona o campo do local na terceira linha.
        addTextField(panel, fieldsA, 2, "local", "3. Local/código");

        // Adiciona o campo da descrição na quarta linha.
        addTextField(panel, fieldsA, 3, "descricao", "4. Descrição");

        // Retorna o painel montado para inclusão no CardLayout.
        return panel;
    }

    /**
     * Constrói o formulário B com listas de opções.
     *
     * @return painel com os quatro campos da condição B.
     */
    private JPanel buildFormB() {

        // Cria o painel com o mesmo layout e título usados no formulário A.
        JPanel panel = formPanel();

        // Adiciona a lista de prédios.
        // A primeira opção é vazia para representar um campo não preenchido.
        addCombo(
            panel,
            0,
            "predio",
            "1. Prédio",
            new String[]{"", "Prédio A", "Prédio B", "Prédio C"}
        );

        // Adiciona a lista de categorias.
        addCombo(
            panel,
            1,
            "categoria",
            "2. Categoria",
            new String[]{"", "Acessório", "Documento", "Eletrônico"}
        );

        // Adiciona a lista de locais.
        addCombo(
            panel,
            2,
            "local",
            "3. Local",
            new String[]{"", "Armário 1", "Armário 2", "Armário 3"}
        );

        // Cria a lista de descrições diretamente neste método.
        // Por padrão, JComboBox não permite digitar novas opções.
        JComboBox<String> description = new JComboBox<>(
            new String[]{
                "",
                "guarda-chuva azul",
                "mochila preta",
                "caderno vermelho"
            }
        );

        // Guarda a referência da lista para leitura, limpeza e foco.
        fieldsB.put("descricao", description);

        // Adiciona o rótulo e a lista de descrições à quarta linha.
        addRow(panel, 3, "4. Descrição", description);

        // Retorna o formulário B montado.
        return panel;
    }

    /**
     * Cria a estrutura visual compartilhada pelos dois formulários.
     *
     * @return painel vazio com GridBagLayout e borda com título.
     */
    private JPanel formPanel() {

        // Usa uma grade flexível para alinhar rótulos e campos.
        JPanel panel = new JPanel(new GridBagLayout());

        // Adiciona uma borda visível com o título informado.
        panel.setBorder(
            BorderFactory.createTitledBorder("Registro interno")
        );

        // Entrega o painel para que o método chamador acrescente os campos.
        return panel;
    }

    /**
     * Cria um campo de texto, registra sua referência e o adiciona ao painel.
     *
     * @param panel painel que receberá o campo.
     * @param map mapa que armazenará a referência do campo.
     * @param row índice da linha no formulário.
     * @param key identificador interno, como "predio".
     * @param label texto exibido ao lado do campo.
     */
    private void addTextField(
        JPanel panel,
        Map<String, JTextField> map,
        int row,
        String key,
        String label
    ) {

        // Cria um campo com largura preferida baseada em 24 colunas.
        // Esse número não limita a quantidade de caracteres digitados.
        JTextField field = new JTextField(24);

        // Associa a chave ao componente para permitir acessá-lo posteriormente.
        map.put(key, field);

        // Posiciona o rótulo e o campo na linha informada.
        addRow(panel, row, label, field);
    }

    /**
     * Cria uma lista de opções e a registra entre os campos do formulário B.
     *
     * @param panel painel que receberá a lista.
     * @param row índice da linha no formulário.
     * @param key identificador interno do campo.
     * @param label texto exibido ao lado da lista.
     * @param values opções disponíveis para seleção.
     */
    private void addCombo(
        JPanel panel,
        int row,
        String key,
        String label,
        String[] values
    ) {

        // Cria a caixa de seleção usando o vetor de textos recebido.
        JComboBox<String> combo = new JComboBox<>(values);

        // Armazena a referência da lista no mapa do formulário B.
        fieldsB.put(key, combo);

        // Posiciona o rótulo e a lista na linha indicada.
        addRow(panel, row, label, combo);
    }

    /**
     * Adiciona uma linha composta por um rótulo e um componente de entrada.
     *
     * O rótulo ocupa a coluna zero e o componente ocupa a coluna um.
     *
     * @param panel painel que usa GridBagLayout.
     * @param row índice da linha.
     * @param label texto do rótulo.
     * @param component componente que será colocado ao lado do rótulo.
     */
    private void addRow(
        JPanel panel,
        int row,
        String label,
        java.awt.Component component
    ) {

        // Component é uma classe-base dos componentes usados neste exemplo.
        // Por isso, o parâmetro aceita tanto JTextField quanto JComboBox.

        // Cria as regras de posicionamento para os componentes desta linha.
        GridBagConstraints c = new GridBagConstraints();

        // Define uma margem externa de 8 pixels em todos os lados.
        c.insets = new Insets(8, 8, 8, 8);

        // Define em qual linha os componentes serão posicionados.
        c.gridy = row;

        // Define a primeira coluna para o rótulo.
        c.gridx = 0;

        // Alinha o componente ao início da linha.
        // Em uma interface orientada da esquerda para a direita, é a esquerda.
        c.anchor = GridBagConstraints.LINE_START;

        // Cria e adiciona o rótulo com as restrições atuais.
        panel.add(new JLabel(label), c);

        // Passa a usar a segunda coluna para o componente de entrada.
        // O layout preserva as restrições já associadas ao rótulo.
        c.gridx = 1;

        // Dá à coluna do campo participação na distribuição do espaço
        // horizontal extra disponível no painel.
        c.weightx = 1;

        // Permite que o componente preencha horizontalmente sua área.
        c.fill = GridBagConstraints.HORIZONTAL;

        // Adiciona o componente de entrada ao lado do rótulo.
        panel.add(component, c);
    }

    /**
     * Alterna o formulário visível e atualiza as mensagens da interface.
     *
     * Os campos não são apagados ao alternar entre as condições.
     *
     * @param nextMode condição a exibir: "A" ou "B".
     */
    private void showMode(String nextMode) {

        // Atualiza o atributo que identifica o modo ativo.
        mode = nextMode;

        // Exibe o painel registrado com o nome correspondente ao modo.
        cards.show(formCards, mode);

        // Usa o operador ternário para escolher a instrução.
        // Formato: condição ? valorSeVerdadeiro : valorSeFalso.
        // Na condição A, os códigos permanecem visíveis para consulta.
        instruction.setText(
            mode.equals("A")
                ? "Memorize: prédio B = 74; acessório = K; armário 3 = 19. Registre um guarda-chuva azul."
                : "Use opções reconhecíveis e preserve o estado após a interrupção."
        );

        // Atualiza a mensagem para indicar o início de uma observação.
        // Essa mensagem não significa que os campos foram limpos.
        status.setText("Condição alterada. Comece uma nova observação.");

        // Solicita o foco para o primeiro campo do formulário selecionado.
        // A solicitação depende de o componente estar apto a receber foco.
        // Na chamada inicial, a janela ainda não foi exibida, então o pedido
        // pode não ser atendido.
        if (mode.equals("A")) {
            fieldsA.get("predio").requestFocusInWindow();
        } else {
            fieldsB.get("predio").requestFocusInWindow();
        }
    }

    /**
     * Lê os valores do formulário atualmente selecionado.
     *
     * Converte os diferentes componentes da interface em uma estrutura comum:
     * um mapa com identificadores e textos.
     *
     * @return valores do formulário ativo.
     */
    private Map<String, String> values() {

        // Cria um mapa para armazenar os textos lidos dos componentes.
        Map<String, String> result = new LinkedHashMap<>();

        // Verifica se o formulário ativo é o de campos de texto.
        if (mode.equals("A")) {

            // Percorre cada entrada do mapa.
            // k representa a chave, como "predio".
            // v representa o JTextField associado à chave.
            // getText() retorna o conteúdo digitado.
            fieldsA.forEach((k, v) -> result.put(k, v.getText()));

        } else {

            // Percorre as listas do formulário B.
            // getSelectedItem() retorna a opção selecionada.
            // String.valueOf() converte o objeto retornado em texto.
            fieldsB.forEach(
                (k, v) -> result.put(k, String.valueOf(v.getSelectedItem()))
            );
        }

        // Retorna os dados que serão usados na validação.
        return result;
    }

    /**
     * Verifica se os dados correspondem ao registro esperado.
     *
     * É static porque não depende de uma instância nem de componentes Swing.
     * Isso permite executar a validação nos testes sem construir a janela.
     *
     * A ausência de public/private/protected indica acesso de pacote.
     *
     * Retornos possíveis:
     * - "OK": todos os campos estão corretos.
     * - "INCOMPLETE:campo": o campo está vazio ou ausente.
     * - "REVIEW:campo": o campo contém um valor diferente do esperado.
     *
     * A verificação para na primeira ocorrência encontrada, seguindo a ordem:
     * prédio, categoria, local e descrição.
     *
     * @param values mapa com os valores a verificar.
     * @param mode condição usada na validação; a interface fornece "A" ou "B".
     * @return resultado da validação.
     */
    static String validateRecord(Map<String, String> values, String mode) {

        // Define uma matriz de pares: identificador do campo e valor esperado.
        // Cada linha tem duas posições:
        // [0] = identificador; [1] = valor esperado.
        // Neste código, qualquer modo diferente de "A" usa os valores de B.
        String[][] expected = mode.equals("A")
            ? new String[][]{
                {"predio", "74"},
                {"categoria", "K"},
                {"local", "19"},
                {"descricao", "guarda-chuva azul"}
            }
            : new String[][]{
                {"predio", "Prédio B"},
                {"categoria", "Acessório"},
                {"local", "Armário 3"},
                {"descricao", "guarda-chuva azul"}
            };

        // Percorre os pares na ordem definida na matriz.
        for (String[] item : expected) {

            // Busca o texto do campo identificado por item[0].
            // Se a chave não existir, usa uma string vazia.
            // trim() remove espaços comuns no início e no fim do texto.
            // O método pressupõe que valores presentes no mapa não sejam null.
            String actual = values.getOrDefault(item[0], "").trim();

            // Se o campo estiver vazio, informa o problema e encerra o método.
            if (actual.isEmpty()) {
                return "INCOMPLETE:" + item[0];
            }

            // Compara o valor recebido com o esperado, ignorando diferenças
            // entre letras maiúsculas e minúsculas.
            // A comparação não ignora diferenças de acentuação ou pontuação.
            if (!actual.equalsIgnoreCase(item[1])) {
                return "REVIEW:" + item[0];
            }
        }

        // Se o laço terminou, todos os campos corresponderam ao esperado.
        return "OK";
    }

    /**
     * Executa quatro testes básicos da validação.
     *
     * Um smoke test verifica rapidamente alguns comportamentos essenciais.
     * Estes testes não verificam a aparência nem a interação com a janela.
     *
     * Se houver falha, lança AssertionError e interrompe a execução.
     */
    private static void smokeTest() {

        // Cria um mapa não modificável com um registro válido na condição A.
        // Map.of() recebe pares alternados de chave e valor.
        Map<String, String> validA = Map.of(
            "predio", "74",
            "categoria", "K",
            "local", "19",
            "descricao", "guarda-chuva azul"
        );

        // Cria um mapa não modificável com um registro válido na condição B.
        Map<String, String> validB = Map.of(
            "predio", "Prédio B",
            "categoria", "Acessório",
            "local", "Armário 3",
            "descricao", "guarda-chuva azul"
        );

        // Teste 1: um registro correto na condição A deve retornar "OK".
        // O operador ! nega o resultado da comparação.
        if (!validateRecord(validA, "A").equals("OK")) {
            throw new AssertionError("valid A");
        }

        // Teste 2: um registro correto na condição B deve retornar "OK".
        if (!validateRecord(validB, "B").equals("OK")) {
            throw new AssertionError("valid B");
        }

        // Teste 3: o prédio vazio deve ser identificado como incompleto.
        // Como prédio é o primeiro campo verificado, a validação retorna
        // antes de analisar as demais chaves ausentes.
        if (!validateRecord(Map.of("predio", ""), "A")
                .equals("INCOMPLETE:predio")) {

            throw new AssertionError("missing field");
        }

        // Cria uma cópia modificável dos dados válidos da condição B.
        // Isso permite alterar o prédio sem modificar validB.
        Map<String, String> wrong = new LinkedHashMap<>(validB);

        // Substitui o prédio correto por um prédio diferente do esperado.
        wrong.put("predio", "Prédio A");

        // Teste 4: o prédio incorreto deve gerar uma solicitação de revisão.
        if (!validateRecord(wrong, "B").equals("REVIEW:predio")) {
            throw new AssertionError("wrong building");
        }

        // Esta mensagem só é alcançada se os quatro testes passarem.
        // O lançamento explícito de AssertionError não depende da opção -ea.
        System.out.println("JAVA_SMOKE_PASS");
    }

    /**
     * Valida o formulário ativo e apresenta o resultado ao usuário.
     *
     * Não salva os dados e não limpa os campos após a confirmação.
     */
    private void confirm() {

        // Lê os valores atuais e os valida de acordo com o modo selecionado.
        String result = validateRecord(values(), mode);

        // Verifica se todos os campos correspondem ao registro esperado.
        if (result.equals("OK")) {

            // Informa o sucesso da simulação e esclarece que nada foi salvo.
            status.setText(
                "Registro fictício concluído. Confira prédio e armário; nada foi salvo."
            );

        } else {

            // Extrai o nome do campo presente após os dois-pontos.
            // Exemplo: "REVIEW:predio" -> "predio".
            // indexOf(':') localiza o separador.
            // substring(...) retorna o trecho que começa após ele.
            String field = result.substring(result.indexOf(':') + 1);

            // Usa a mesma mensagem para campos incompletos e incorretos.
            // Os dados digitados ou selecionados são mantidos.
            status.setText(
                "Revise " + field + "; os demais dados foram preservados."
            );

            // Solicita o foco para o campo que precisa de revisão.
            if (mode.equals("A")) {
                fieldsA.get(field).requestFocusInWindow();
            } else {
                fieldsB.get(field).requestFocusInWindow();
            }
        }
    }

    /**
     * Limpa todos os campos das duas condições.
     *
     * Também apaga os dados do formulário que estiver oculto.
     */
    private void clear() {

        // values() do mapa retorna a coleção dos componentes armazenados.
        // Para cada JTextField, define o conteúdo como uma string vazia.
        fieldsA.values().forEach(field -> field.setText(""));

        // Para cada JComboBox, seleciona a primeira opção.
        // Todas as listas deste programa têm uma opção vazia no índice zero.
        fieldsB.values().forEach(combo -> combo.setSelectedIndex(0));

        // Informa que a limpeza foi realizada.
        status.setText("Campos limpos; nenhuma informação foi persistida.");
    }

    /**
     * Ponto de entrada da aplicação.
     *
     * Exemplos de execução, após a compilação:
     *
     * java ErgonomiaJava
     * Abre a interface gráfica.
     *
     * java ErgonomiaJava --smoke-test
     * Executa os testes básicos sem abrir a interface.
     *
     * @param args argumentos recebidos pela linha de comando.
     */
    public static void main(String[] args) {

        // Verifica se existe ao menos um argumento e se o primeiro é o
        // comando de teste.
        // O operador && usa avaliação de curto-circuito: args[0] só é
        // acessado quando args.length > 0, evitando acesso a posição inexistente.
        if (args.length > 0 && args[0].equals("--smoke-test")) {

            // Executa os testes sem criar uma instância de ErgonomiaJava.
            // Por isso, os atributos de instância, incluindo JFrame,
            // não são construídos neste caminho de execução.
            smokeTest();

        } else {

            // Agenda a criação da interface na Event Dispatch Thread (EDT),
            // a thread responsável por eventos e atualizações do Swing.
            //
            // ErgonomiaJava::new é uma referência ao construtor.
            // Neste contexto, equivale a:
            // SwingUtilities.invokeLater(() -> new ErgonomiaJava());
            SwingUtilities.invokeLater(ErgonomiaJava::new);
        }
    }
}