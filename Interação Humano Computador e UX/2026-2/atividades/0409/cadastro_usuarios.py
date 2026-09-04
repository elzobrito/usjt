import tkinter as tk
from tkinter import ttk


class CadastroUsuariosJanela:

    def __init__(self):

        # ---------------------------------------------------------
        # JANELA PRINCIPAL
        # ---------------------------------------------------------

        self.janela = tk.Tk()

        self.janela.title("Cadastro de usuários")

        self.janela.geometry("670x430")

        self.janela.minsize(620, 380)

        # Cor de fundo da aplicação.
        self.cor_fundo = "#F5F7FA"

        # Verde do botão Cadastrar.
        self.cor_cadastrar = "#2E7D32"

        # Vermelho do botão Excluir.
        self.cor_excluir = "#B71C1C"

        # Azul utilizado na seleção da tabela.
        self.cor_selecao = "#285A96"

        # Verde das mensagens de sucesso.
        self.cor_sucesso = "#236E3C"

        # Vermelho das mensagens de erro.
        self.cor_erro = "#B42828"

        self.janela.configure(
            bg=self.cor_fundo
        )

        # ---------------------------------------------------------
        # DADOS
        # ---------------------------------------------------------

        self.proximo_id = 3

        # ---------------------------------------------------------
        # ESTILOS
        # ---------------------------------------------------------

        self.configurar_estilos()

        # ---------------------------------------------------------
        # PAINEL PRINCIPAL
        # ---------------------------------------------------------

        self.painel_principal = tk.Frame(
            self.janela,
            bg=self.cor_fundo
        )

        self.painel_principal.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ---------------------------------------------------------
        # TÍTULO
        # ---------------------------------------------------------

        self.titulo = tk.Label(
            self.painel_principal,
            text="Cadastro de usuários",
            font=("Arial", 22, "bold"),
            bg=self.cor_fundo,
            fg="#282828"
        )

        self.titulo.pack(
            pady=(0, 15)
        )

        # ---------------------------------------------------------
        # FORMULÁRIO
        # ---------------------------------------------------------

        self.formulario = tk.Frame(
            self.painel_principal,
            bg="white",
            highlightbackground="#CDD2DA",
            highlightthickness=1
        )

        self.formulario.pack(
            fill="x",
            pady=(0, 8),
            ipady=8
        )

        # ---------------------------------------------------------
        # RÓTULO NOME
        # ---------------------------------------------------------

        self.rotulo_nome = tk.Label(
            self.formulario,
            text="Nome:",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#282828"
        )

        self.rotulo_nome.pack(
            side="left",
            padx=(15, 8)
        )

        # ---------------------------------------------------------
        # CAMPO NOME
        # ---------------------------------------------------------

        self.campo_nome = ttk.Entry(
            self.formulario,
            width=25,
            font=("Arial", 11)
        )

        self.campo_nome.pack(
            side="left",
            ipady=5,
            padx=(0, 10)
        )

        # ---------------------------------------------------------
        # BOTÃO CADASTRAR
        # ---------------------------------------------------------

        self.botao_cadastrar = tk.Button(
            self.formulario,
            text="Cadastrar",
            command=self.cadastrar_usuario,
            font=("Arial", 10, "bold"),
            bg=self.cor_cadastrar,
            fg="white",
            activebackground="#1B5E20",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            padx=14,
            pady=7
        )

        self.botao_cadastrar.pack(
            side="left",
            padx=5
        )

        # ---------------------------------------------------------
        # BOTÃO EXCLUIR
        # ---------------------------------------------------------

        self.botao_excluir = tk.Button(
            self.formulario,
            text="Excluir selecionado",
            command=self.excluir_usuario,
            font=("Arial", 10, "bold"),
            bg=self.cor_excluir,
            fg="white",
            activebackground="#8E0000",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            padx=14,
            pady=7
        )

        self.botao_excluir.pack(
            side="left",
            padx=5
        )

        # ---------------------------------------------------------
        # MENSAGEM
        # ---------------------------------------------------------

        self.mensagem = tk.Label(
            self.painel_principal,
            text=" ",
            font=("Arial", 10),
            bg=self.cor_fundo,
            fg="#464646",
            anchor="w"
        )

        self.mensagem.pack(
            fill="x",
            pady=(0, 5)
        )

        # ---------------------------------------------------------
        # ÁREA DA TABELA
        # ---------------------------------------------------------

        self.frame_tabela = ttk.LabelFrame(
            self.painel_principal,
            text="Usuários cadastrados"
        )

        self.frame_tabela.pack(
            fill="both",
            expand=True
        )

        # ---------------------------------------------------------
        # TABELA
        # ---------------------------------------------------------

        self.tabela = ttk.Treeview(
            self.frame_tabela,
            columns=("id", "nome"),
            show="headings",
            selectmode="browse"
        )

        # Define o título das colunas.
        self.tabela.heading(
            "id",
            text="ID"
        )

        self.tabela.heading(
            "nome",
            text="Nome"
        )

        # Define o tamanho das colunas.
        self.tabela.column(
            "id",
            width=80,
            minwidth=60,
            anchor="center",
            stretch=False
        )

        self.tabela.column(
            "nome",
            width=450,
            minwidth=200,
            anchor="w"
        )

        # ---------------------------------------------------------
        # BARRA DE ROLAGEM
        # ---------------------------------------------------------

        self.rolagem = ttk.Scrollbar(
            self.frame_tabela,
            orient="vertical",
            command=self.tabela.yview
        )

        self.tabela.configure(
            yscrollcommand=self.rolagem.set
        )

        self.rolagem.pack(
            side="right",
            fill="y"
        )

        self.tabela.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ---------------------------------------------------------
        # USUÁRIOS INICIAIS
        # ---------------------------------------------------------

        self.tabela.insert(
            "",
            "end",
            values=(1, "Ana")
        )

        self.tabela.insert(
            "",
            "end",
            values=(2, "Carlos")
        )

        # ---------------------------------------------------------
        # ACESSIBILIDADE / TECLADO
        # ---------------------------------------------------------

        # Enter cadastra o usuário.
        self.janela.bind(
            "<Return>",
            lambda evento: self.cadastrar_usuario()
        )

        # Alt + N leva o foco ao campo Nome.
        self.janela.bind(
            "<Alt-n>",
            lambda evento: self.campo_nome.focus_set()
        )

        # Alt + C cadastra.
        self.janela.bind(
            "<Alt-c>",
            lambda evento: self.cadastrar_usuario()
        )

        # Alt + E exclui o usuário selecionado.
        self.janela.bind(
            "<Alt-e>",
            lambda evento: self.excluir_usuario()
        )

        # Delete também pode excluir a linha selecionada.
        self.tabela.bind(
            "<Delete>",
            lambda evento: self.excluir_usuario()
        )

        # Coloca inicialmente o cursor no campo Nome.
        self.campo_nome.focus_set()

    # =============================================================
    # CONFIGURAÇÃO VISUAL DA TABELA
    # =============================================================

    def configurar_estilos(self):

        estilo = ttk.Style()

        # O tema clam permite maior controle visual.
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        # Estilo geral da tabela.
        estilo.configure(
            "Treeview",
            font=("Arial", 11),
            rowheight=32,
            background="white",
            fieldbackground="white",
            foreground="#282828"
        )

        # Aparência da linha selecionada.
        estilo.map(
            "Treeview",
            background=[
                ("selected", self.cor_selecao)
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        # Aparência do cabeçalho.
        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 11, "bold"),
            padding=8
        )

    # =============================================================
    # CADASTRAR USUÁRIO
    # =============================================================

    def cadastrar_usuario(self):

        # Obtém o texto digitado.
        nome = self.campo_nome.get().strip()

        # ---------------------------------------------------------
        # VALIDAÇÃO
        # ---------------------------------------------------------

        if not nome:

            self.definir_mensagem(
                "Erro: o campo nome é obrigatório.",
                self.cor_erro
            )

            self.campo_nome.focus_set()

            return

        # ---------------------------------------------------------
        # ADICIONA NA TABELA
        # ---------------------------------------------------------

        self.tabela.insert(
            "",
            "end",
            values=(
                self.proximo_id,
                nome
            )
        )

        # Incrementa o próximo ID.
        self.proximo_id += 1

        # Limpa o campo.
        self.campo_nome.delete(
            0,
            tk.END
        )

        # Mensagem de sucesso.
        self.definir_mensagem(
            "Sucesso: usuário cadastrado.",
            self.cor_sucesso
        )

        # Retorna o foco.
        self.campo_nome.focus_set()

    # =============================================================
    # EXCLUIR USUÁRIO
    # =============================================================

    def excluir_usuario(self):

        # Obtém a linha selecionada.
        selecionado = self.tabela.selection()

        # ---------------------------------------------------------
        # VALIDAÇÃO
        # ---------------------------------------------------------

        if not selecionado:

            self.definir_mensagem(
                "Erro: selecione um usuário na tabela.",
                self.cor_erro
            )

            self.tabela.focus_set()

            return

        # ---------------------------------------------------------
        # EXCLUSÃO
        # ---------------------------------------------------------

        self.tabela.delete(
            selecionado[0]
        )

        self.definir_mensagem(
            "Sucesso: usuário excluído.",
            self.cor_sucesso
        )

        self.campo_nome.focus_set()

    # =============================================================
    # MENSAGENS
    # =============================================================

    def definir_mensagem(
        self,
        texto,
        cor
    ):

        self.mensagem.config(
            text=texto,
            fg=cor
        )

    # =============================================================
    # EXECUÇÃO
    # =============================================================

    def executar(self):

        self.janela.mainloop()


# -------------------------------------------------------------
# INÍCIO DO PROGRAMA
# -------------------------------------------------------------

if __name__ == "__main__":

    programa = CadastroUsuariosJanela()

    programa.executar()