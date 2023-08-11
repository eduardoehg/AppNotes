from tkinter import ttk
from uteis import limpar_tela
from controller.inserir_controller import InserirController
import tkinter as tk


class InserirView:

    def __init__(self, frame):
        self.controller = InserirController()
        self.frame = frame
        self.frame1 = None
        self.cb_categoria = None
        self.entry_titulo = None
        self.entry_descricao = None
        self.id_nota = None

        self.tela_inserir()

    def tela_inserir(self):
        limpar_tela(self.frame)
        self.frame1 = tk.Frame(self.frame, width=598, height=50, background='#a1d1d2')
        self.frame1.grid_propagate(False)
        self.frame1.grid(row=0, column=0, pady=(10, 0))
        label_categoria = tk.Label(self.frame1, text='Escolha uma Categoria')
        label_categoria.config(bg='#a1d1d2', fg='#111f32', font=('Nunito', 11, 'bold'))
        label_categoria.grid(row=0, column=0, padx=10)

        self.atualizar_categorias()

        frame2 = tk.Frame(self.frame, width=598, height=50, background='#a1d1d2')
        frame2.grid_propagate(False)
        frame2.grid(row=1, column=0)
        label_titulo = tk.Label(frame2, text='Título da Nota')
        label_titulo.config(bg='#a1d1d2', fg='#111f32', font=('Nunito', 11, 'bold'))
        label_titulo.grid(row=0, column=0, padx=10)
        self.entry_titulo = tk.Entry(frame2, width=50, borderwidth=0)
        self.entry_titulo.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 11, 'bold'), insertbackground='#a1d1d2')
        self.entry_titulo.grid(row=0, column=1)

        label_descricao = tk.Label(self.frame, text='Descrição')
        label_descricao.config(bg='#a1d1d2', fg='#111f32', font=('Nunito', 11, 'bold'))
        label_descricao.grid(row=2, column=0, padx=10, sticky='W')
        self.entry_descricao = tk.Text(self.frame, wrap='word', width=63, height=18, borderwidth=0)
        self.entry_descricao.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 11, 'bold'), insertbackground='#a1d1d2')
        self.entry_descricao.grid(row=3, column=0, pady=(0, 10))

        frame3 = tk.Frame(self.frame, width=598, height=40, background='#a1d1d2')
        frame3.grid_propagate(False)
        frame3.grid(row=4, column=0)
        botao_limpar = tk.Button(frame3, text='Limpar', width=12, command=self.limpar)
        botao_limpar.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 11, 'bold'), relief='groove', borderwidth=0)
        botao_limpar.grid(row=0, column=0, padx=(350, 5))
        botao_salvar = tk.Button(frame3, text='Salvar Nota', width=12, command=self.inserir_nota)
        botao_salvar.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 11, 'bold'), relief='groove', borderwidth=0)
        botao_salvar.grid(row=0, column=1)

    def atualizar_categorias(self):
        categorias = self.controller.listar_categorias()
        categorias.insert(0, ['Selecione'])
        self.cb_categoria = ttk.Combobox(self.frame1, values=[item[0] for item in categorias], width=41)
        self.cb_categoria.config(font=('Nunito', 11, 'bold'), foreground='#111f32')
        self.cb_categoria.set(categorias[0])
        self.cb_categoria.grid(row=0, column=1)

    def inserir_nota(self):
        if self.id_nota is None:
            self.controller.inserir_nota(self.cb_categoria.get(), self.entry_titulo.get(),
                                         self.entry_descricao.get('1.0', 'end-1c'), self.limpar)
        else:
            self.controller.editar_nota(self.cb_categoria.get(), self.entry_titulo.get(),
                                        self.entry_descricao.get('1.0', 'end-1c'), self.id_nota, self.limpar)

    def editar_nota(self, categoria, titulo, nota, id_nota):
        self.tela_inserir()
        self.cb_categoria.set(categoria)
        self.entry_titulo.insert(0, titulo)
        self.entry_descricao.insert('end', nota)
        self.id_nota = id_nota

    def limpar(self):
        self.entry_titulo.delete(0, 'end')
        self.entry_descricao.delete('1.0', 'end')
