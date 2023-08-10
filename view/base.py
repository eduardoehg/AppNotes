from .inserir_view import InserirView
from .pesquisar_view import PesquisarView
from .categorias_view import InserirCategoriaView, EditarCategoriaView, ExcluirCategoriaView
from uteis import dimensionamento
from functools import partial
import tkinter as tk


class Base:

    def __init__(self, janela):
        self.janela = janela
        self.frame_cabecalho = None
        self.frame_corpo = None
        self.nome_tela = ''

        self.tela_base()
        
    def tela_base(self):
        largura, altura, x, y = dimensionamento(self.janela, 638, 650, 85)
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")
        self.janela.title('AppNotes')
        self.janela.config(background='#a1d1d2')

        self.frame_cabecalho = tk.Frame(self.janela, bg='#a1d1d2', width=600, height=50)
        self.frame_cabecalho.grid_propagate(False)
        self.frame_cabecalho.grid(row=0, column=0, pady=10, padx=20)
        self.frame_corpo = tk.Frame(self.janela, bg='#a1d1d2', width=600, height=560, borderwidth=1, relief='solid')
        self.frame_corpo.grid(row=1, column=0)
        self.frame_corpo.grid_propagate(False)

        barra = tk.Menu(self.janela)
        self.janela.config(menu=barra)
        barra.add_command(label='Inserir', command=self.inserirview)
        barra.add_command(label='Pesquisar', command=self.pesquisarview)
        categorias = tk.Menu(barra, tearoff=0)
        barra.add_cascade(label='Categorias', menu=categorias)
        titulo_inserir = 'Inserir Nova Categoria'
        descricao_inserir = 'Digite o nome da nova categoria e clique em salvar'
        categorias.add_command(label='Inserir Categoria', command=partial(InserirCategoriaView, titulo_inserir,
                                                                          descricao_inserir))
        titulo_editar = 'Editar Categoria'
        descricao_editar = 'Selecione a categoria desejada e digite o seu novo nome'
        categorias.add_command(label='Editar Categoria', command=partial(EditarCategoriaView, titulo_editar,
                                                                         descricao_editar))
        titulo_excluir = 'Excluir Categoria'
        descricao_excluir = 'Selecione a categoria desejada e clique em excluir'
        categorias.add_command(label='Excluir Categoria', command=partial(ExcluirCategoriaView, titulo_excluir,
                                                                          descricao_excluir))
        barra.add_command(label='Sair', command=self.janela.quit)

        frame_cabecalho_esquerda = tk.Frame(self.frame_cabecalho, background='#a1d1d2', width=365, height=50)
        frame_cabecalho_esquerda.grid_propagate(False)
        frame_cabecalho_esquerda.grid(row=0, column=0)
        frame_cabecalho_direita = tk.Frame(self.frame_cabecalho, background='#a1d1d2', width=365, height=50)
        frame_cabecalho_direita.grid_propagate(False)
        frame_cabecalho_direita.grid(row=0, column=1)
        titulo = tk.Label(frame_cabecalho_esquerda, text='AppNotes', fg='#111f32')
        titulo.config(font=('Nunito', 24, 'bold'), bg='#a1d1d2')
        titulo.grid(row=0, column=0)
        imagem_inserir = tk.PhotoImage(file='img/add.png')
        botao_inserir = tk.Button(frame_cabecalho_direita, text='  Inserir ', image=imagem_inserir, compound='left',
                                  width=110, command=self.inserirview)
        botao_inserir.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 12, 'bold'), relief='groove', borderwidth=0)
        botao_inserir.grid(row=0, column=1, padx=(0, 5), pady=10)
        imagem_pesquisar = tk.PhotoImage(file='img/search.png')
        botao_pesquisar = tk.Button(frame_cabecalho_direita, text='  Pesquisar ', image=imagem_pesquisar,
                                    compound='left', width=110, command=self.pesquisarview)
        botao_pesquisar.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 12, 'bold'), relief='groove', borderwidth=0)
        botao_pesquisar.grid(row=0, column=2, pady=10)

        InserirView(self.frame_corpo)
        self.nome_tela = 'inserir'

        self.janela.mainloop()

    def pesquisarview(self):
        if self.nome_tela == 'inserir':
            PesquisarView(self.frame_corpo)
            self.nome_tela = 'pesquisar'

    def inserirview(self):
        if self.nome_tela == 'pesquisar':
            InserirView(self.frame_corpo)
            self.nome_tela = 'inserir'
