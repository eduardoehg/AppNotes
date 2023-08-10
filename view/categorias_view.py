from uteis import dimensionamento
from controller.categorias_controller import InserirCategoriaController, EditarCategoriaController, ExcluirCategoriaController
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


class CategoriaView:

    def __init__(self, titulo, descricao):
        self.janela = tk.Toplevel()
        self.titulo = titulo
        self.descricao = descricao
        self.frame = None

        self.tela_categoria_base()

    def tela_categoria_base(self):
        largura, altura, x, y = dimensionamento(self.janela, 620, 160, 450)
        self.janela.geometry(f'{largura}x{altura}+{x}+{y}')
        self.janela.config(bg='#a1d1d2')
        self.janela.title(f'{self.titulo}')
        self.janela.grid_propagate(False)

        label = tk.Label(self.janela, text=f'{self.descricao}')
        label.config(bg='#a1d1d2', fg='#111f32', font=('Nunito', 11, 'bold'))
        label.grid(row=0, column=0, pady=10, padx=10)

        self.frame = tk.Frame(self.janela, borderwidth=1, relief='solid', width=580, height=95, background='#a1d1d2')
        self.frame.grid(row=1, column=0, padx=20)
        self.frame.grid_propagate(False)


class InserirCategoriaView(CategoriaView):

    def __init__(self, titulo, descricao):
        super().__init__(titulo, descricao)
        self.controller = InserirCategoriaController()
        self.entry = None

        self.tela_inserir()

    def tela_inserir(self):
        label_nome = tk.Label(self.frame, text='Nome')
        label_nome.config(bg='#a1d1d2', fg='#111f32', font=('Nunito', 11, 'bold'))
        label_nome.grid(row=0, column=0, pady=10, padx=10)
        self.entry = tk.Entry(self.frame, borderwidth=0, width=55)
        self.entry.config(bg='#111f32', fg='#a1d1d2', insertbackground='#a1d1d2', font=('Nunito', 11, 'bold'))
        self.entry.grid(row=0, column=1)
        botao = tk.Button(self.frame, text='Salvar', width=12, command=self.inserir_categoria)
        botao.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 11, 'bold'), relief='groove', borderwidth=0)
        botao.grid(row=1, column=1, padx=(383, 0))

    def inserir_categoria(self):
        janela = self.janela
        nome = self.entry.get()
        self.controller.inserir(janela, nome)


class EditarCategoriaView(CategoriaView):

    def __init__(self, titulo, descricao):
        super().__init__(titulo, descricao)
        self.controller = EditarCategoriaController()
        self.combobox = None
        self.entry = None

        self.tela_editar()

    def tela_editar(self):
        categorias = self.controller.carregar_categorias()
        self.combobox = ttk.Combobox(self.frame, values=[categoria[0] for categoria in categorias])
        self.combobox.config(font=('Nunito', 11, 'bold'), foreground='#111f32', width=15)
        self.combobox.set(categorias[0])
        self.combobox.grid(row=0, column=0, padx=10, pady=10)
        label = tk.Label(self.frame, text='Novo Nome')
        label.config(font=('Nunito', 11, 'bold'), fg='#111f32', bg='#a1d1d2')
        label.grid(row=0, column=1)
        self.entry = tk.Entry(self.frame, borderwidth=0, relief='groove', width=32)
        self.entry.config(font=('Nunito', 11, 'bold'), fg='#a1d1d2', bg='#111f32', insertbackground='#a1d1d2')
        self.entry.grid(row=0, column=2, padx=10)
        botao = tk.Button(self.frame, text='Salvar', width=12, command=self.editar_categoria)
        botao.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 11, 'bold'), relief='groove', borderwidth=0)
        botao.grid(row=1, column=2, padx=(175, 0))

    def editar_categoria(self):
        self.controller.editar(self.janela, self.combobox.get(), self.entry.get())


class ExcluirCategoriaView(CategoriaView):

    def __init__(self, titulo, descricao):
        super().__init__(titulo, descricao)
        self.controller = ExcluirCategoriaController()
        self.combobox = None

        self.tela_excluir()

    def tela_excluir(self):
        label = tk.Label(self.frame, text='Categoria')
        label.config(font=('Nunito', 11, 'bold'), bg='#a1d1d2', fg='#111f32')
        label.grid(row=0, column=0, pady=10, padx=10)
        lista = self.controller.carregar_categorias()
        self.combobox = ttk.Combobox(self.frame, values=[item[0] for item in lista])
        self.combobox.config(font=('Nunito', 11, 'bold'), width=50)
        self.combobox.set(lista[0])
        self.combobox.grid(row=0, column=1)
        botao = tk.Button(self.frame, text='Excluir', width=12, command=self.excluir_categoria)
        botao.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', borderwidth=0, relief='groove')
        botao.grid(row=1, column=1, padx=(358, 0))

    def excluir_categoria(self):
        resposta = messagebox.askokcancel('Exluir Categoria!', 'Ao remover todas as notas pertencentes a categoria '
                                                               'serão removidas!\n\nDeseja realmente exluir?')
        if resposta:
            self.controller.excluir(self.janela, self.combobox.get())
