import tkinter as tk
from tkinter import ttk

import customtkinter as ctk


class CadastroUsuariosJanela:

    def __init__(self):

        # ---------------------------------------------------------
        # CONFIGURAÇÃO GERAL
        # ---------------------------------------------------------

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ---------------------------------------------------------
        # CORES
        # ---------------------------------------------------------

        self.cor_fundo = "#F5F7FA"

        self.cor_card = "#FFFFFF"

        self.cor_texto = "#282828"

        self.cor_texto_secundario = "#666666"

        self.cor_borda = "#D5D9E0"

        self.cor_cadastrar = "#2E7D32"

        self.cor_cadastrar_hover = "#1B5E20"

        self.cor_excluir = "#B71C1C"

        self.cor_excluir_hover = "#8E0000"

        self.cor_selecao = "#285A96"

        self.cor_sucesso = "#236E3C"

        self.cor_erro = "#B42828"

        # ---------------------------------------------------------
        # JANELA
        # ---------------------------------------------------------

        self.janela = ctk.CTk()

        self.janela.title(
            "Cadastro de usuários"
        )

        self.janela.geometry(
            "700x460"
        )

        self.janela.minsize(
            650,
            400
        )

        self.janela.configure(
            fg_color=self.cor_fundo
        )

        # ---------------------------------------------------------
        # PRÓXIMO ID
        # ---------------------------------------------------------

        self.proximo_id = 3

        # ---------------------------------------------------------
        # CONFIGURAÇÃO DA TABELA
        # ---------------------------------------------------------

        self.configurar_estilo_tabela()

        # ---------------------------------------------------------
        # PAINEL PRINCIPAL
        # ---------------------------------------------------------

        self.painel_principal = ctk.CTkFrame(
            self.janela,
            fg_color=self.cor_fundo,
            corner_radius=0
        )

        self.painel_principal.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        # ---------------------------------------------------------
        # TÍTULO
        # ---------------------------------------------------------

        self.titulo = ctk.CTkLabel(
            self.painel_principal,
            text="Cadastro de usuários",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            ),
            text_color=self.cor_texto
        )

        self.titulo.pack(
            pady=(0, 18)
        )

        # ---------------------------------------------------------
        # CARD DO FORMULÁRIO
        # ---------------------------------------------------------

        self.card_formulario = ctk.CTkFrame(
            self.painel_principal,
            fg_color=self.cor_card,
            corner_radius=16,
            border_width=1,
            border_color=self.cor_borda
        )

        self.card_formulario.pack(
            fill="x",
            pady=(0, 10)
        )

        # ---------------------------------------------------------
        # CONTEÚDO DO FORMULÁRIO
        # ---------------------------------------------------------

        self.formulario = ctk.CTkFrame(
            self.card_formulario,
            fg_color="transparent"
        )

        self.formulario.pack(
            fill="x",
            padx=18,
            pady=16
        )

        # ---------------------------------------------------------
        # RÓTULO
        # ---------------------------------------------------------

        self.rotulo_nome = ctk.CTkLabel(
            self.formulario,
            text="Nome:",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            text_color=self.cor_texto
        )

        self.rotulo_nome.pack(
            side="left",
            padx=(0, 8)
        )

        # ---------------------------------------------------------
        # CAMPO NOME
        # ---------------------------------------------------------

        self.campo_nome = ctk.CTkEntry(
            self.formulario,
            width=230,
            height=38,
            placeholder_text="Digite o nome",
            font=ctk.CTkFont(
                size=14
            ),
            corner_radius=10,
            border_width=1,
            border_color=self.cor_borda
        )

        self.campo_nome.pack(
            side="left",
            padx=(0, 10)
        )

        # ---------------------------------------------------------
        # BOTÃO CADASTRAR
        # ---------------------------------------------------------

        self.botao_cadastrar = ctk.CTkButton(
            self.formulario,
            text="Cadastrar",
            command=self.cadastrar_usuario,

            width=110,
            height=38,

            corner_radius=10,

            fg_color=self.cor_cadastrar,

            hover_color=self.cor_cadastrar_hover,

            text_color="white",

            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),

            cursor="hand2"
        )

        self.botao_cadastrar.pack(
            side="left",
            padx=5
        )

        # ---------------------------------------------------------
        # BOTÃO EXCLUIR
        # ---------------------------------------------------------

        self.botao_excluir = ctk.CTkButton(
            self.formulario,
            text="Excluir selecionado",
            command=self.excluir_usuario,

            width=155,
            height=38,

            corner_radius=10,

            fg_color=self.cor_excluir,

            hover_color=self.cor_excluir_hover,

            text_color="white",

            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),

            cursor="hand2"
        )

        self.botao_excluir.pack(
            side="left",
            padx=5
        )

        # ---------------------------------------------------------
        # MENSAGEM DE STATUS
        # ---------------------------------------------------------

        self.mensagem = ctk.CTkLabel(
            self.painel_principal,
            text=" ",
            anchor="w",
            font=ctk.CTkFont(
                size=13
            ),
            text_color=self.cor_texto_secundario
        )

        self.mensagem.pack(
            fill="x",
            padx=5,
            pady=(0, 8)
        )

        # ---------------------------------------------------------
        # CARD DA TABELA
        # ---------------------------------------------------------

        self.card_tabela = ctk.CTkFrame(
            self.painel_principal,
            fg_color=self.cor_card,
            corner_radius=16,
            border_width=1,
            border_color=self.cor_borda
        )

        self.card_tabela.pack(
            fill="both",
            expand=True
        )

        # ---------------------------------------------------------
        # TÍTULO DA TABELA
        # ---------------------------------------------------------

        self.titulo_tabela = ctk.CTkLabel(
            self.card_tabela,
            text="Usuários cadastrados",
            anchor="w",
            font=ctk.CTkFont(
                size=15,
                weight="bold"
            ),
            text_color=self.cor_texto
        )

        self.titulo_tabela.pack(
            fill="x",
            padx=18,
            pady=(15, 8)
        )

        # ---------------------------------------------------------
        # ÁREA DA TABELA
        # ---------------------------------------------------------

        self.area_tabela = ctk.CTkFrame(
            self.card_tabela,
            fg_color="transparent"
        )

        self.area_tabela.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # ---------------------------------------------------------
        # TABELA
        # ---------------------------------------------------------

        self.tabela = ttk.Treeview(
            self.area_tabela,

            columns=(
                "id",
                "nome"
            ),

            show="headings",

            selectmode="browse"
        )

        # Cabeçalho ID.
        self.tabela.heading(
            "id",
            text="ID"
        )

        # Cabeçalho Nome.
        self.tabela.heading(
            "nome",
            text="Nome"
        )

        # Coluna ID.
        self.tabela.column(
            "id",
            width=80,
            minwidth=60,
            stretch=False,
            anchor="center"
        )

        # Coluna Nome.
        self.tabela.column(
            "nome",
            width=450,
            minwidth=200,
            anchor="w"
        )

        # ---------------------------------------------------------
        # SCROLLBAR
        # ---------------------------------------------------------

        self.rolagem = ttk.Scrollbar(
            self.area_tabela,

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
        # DADOS INICIAIS
        # ---------------------------------------------------------

        self.tabela.insert(
            "",
            "end",
            values=(
                1,
                "Ana"
            )
        )

        self.tabela.insert(
            "",
            "end",
            values=(
                2,
                "Carlos"
            )
        )

        # ---------------------------------------------------------
        # ACESSIBILIDADE E TECLADO
        # ---------------------------------------------------------

        # Enter cadastra.
        self.janela.bind(
            "<Return>",
            lambda evento:
                self.cadastrar_usuario()
        )

        # Alt + N coloca o foco no campo Nome.
        self.janela.bind(
            "<Alt-n>",
            lambda evento:
                self.campo_nome.focus_set()
        )

        # Alt + C cadastra.
        self.janela.bind(
            "<Alt-c>",
            lambda evento:
                self.cadastrar_usuario()
        )

        # Alt + E exclui.
        self.janela.bind(
            "<Alt-e>",
            lambda evento:
                self.excluir_usuario()
        )

        # Delete exclui o usuário selecionado.
        self.tabela.bind(
            "<Delete>",
            lambda evento:
                self.excluir_usuario()
        )

        # Foco inicial.
        self.campo_nome.focus_set()

    # =============================================================
    # ESTILO DA TABELA
    # =============================================================

    def configurar_estilo_tabela(self):

        estilo = ttk.Style()

        try:

            estilo.theme_use(
                "clam"
            )

        except tk.TclError:

            pass

        # ---------------------------------------------------------
        # CORPO DA TABELA
        # ---------------------------------------------------------

        estilo.configure(
            "Treeview",

            background="#FFFFFF",

            fieldbackground="#FFFFFF",

            foreground="#282828",

            rowheight=34,

            font=(
                "Arial",
                11
            ),

            borderwidth=0
        )

        # ---------------------------------------------------------
        # SELEÇÃO
        # ---------------------------------------------------------

        estilo.map(
            "Treeview",

            background=[
                (
                    "selected",
                    self.cor_selecao
                )
            ],

            foreground=[
                (
                    "selected",
                    "white"
                )
            ]
        )

        # ---------------------------------------------------------
        # CABEÇALHO
        # ---------------------------------------------------------

        estilo.configure(
            "Treeview.Heading",

            background="#EEF1F5",

            foreground="#282828",

            font=(
                "Arial",
                11,
                "bold"
            ),

            padding=9,

            relief="flat"
        )

        estilo.map(
            "Treeview.Heading",

            background=[
                (
                    "active",
                    "#E2E6EB"
                )
            ]
        )

    # =============================================================
    # CADASTRAR
    # =============================================================

    def cadastrar_usuario(self):

        # Obtém o nome informado.
        nome = (
            self.campo_nome
            .get()
            .strip()
        )

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
        # INSERE NA TABELA
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
            "end"
        )

        # Exibe mensagem.
        self.definir_mensagem(
            "Sucesso: usuário cadastrado.",
            self.cor_sucesso
        )

        # Retorna o foco.
        self.campo_nome.focus_set()

    # =============================================================
    # EXCLUIR
    # =============================================================

    def excluir_usuario(self):

        selecionado = (
            self.tabela
            .selection()
        )

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
        # REMOVE DA TABELA
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

        self.mensagem.configure(
            text=texto,
            text_color=cor
        )

    # =============================================================
    # EXECUTAR
    # =============================================================

    def executar(self):

        self.janela.mainloop()


# =============================================================
# PROGRAMA PRINCIPAL
# =============================================================

if __name__ == "__main__":

    programa = CadastroUsuariosJanela()

    programa.executar()