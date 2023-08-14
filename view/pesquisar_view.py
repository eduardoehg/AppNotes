from tkinter import ttk
from uteis import limpar_tela
from controller.pesquisar_controller import PesquisarController, EditarNotaController, VizualizarNotaController, ExcluirNotaController
import tkinter as tk


class PesquisarView:

    def __init__(self, frame):

        self.controller_pesquisar = PesquisarController()
        self.controller_vizualizar = VizualizarNotaController()
        self.controller_editar = EditarNotaController(frame)
        self.controller_excluir = ExcluirNotaController()
        self.frame = frame
        self.categorias = []
        self.nota = []
        self.combobox = None
        self.entry_palavra = None
        self.treeview = None

        self.tela_pesquisar()

    def tela_pesquisar(self):
        limpar_tela(self.frame)
        label = tk.Label(self.frame, text='Selecione uma categoria, informe o título ou digite uma palavra contida '
                                          '\nna descrição da nota para realizar a pesquisa')
        label.config(font=('Nunito', 11, 'bold'), bg='#a1d1d2', fg='#111f32')
        label.grid(row=0, column=0, padx=45, pady=10)
        label.rowconfigure(0, weight=1)
        label.columnconfigure(0, weight=1)

        frame1 = tk.Frame(self.frame, bg='#a1d1d2')
        frame1.grid(row=1, column=0, sticky='W', padx=10)
        label_categoria = tk.Label(frame1, text='Categorias')
        label_categoria.config(font=('Nunito', 11, 'bold'), bg='#a1d1d2', fg='#111f32')
        label_categoria.grid(row=0, column=0, sticky='W')
        self.categorias = self.controller_pesquisar.carregar_categorias()
        self.categorias.insert(0, ['Selecione'])
        self.categorias.insert(1, ['Todas as Notas'])
        self.combobox = ttk.Combobox(frame1, values=[categoria[0] for categoria in self.categorias])
        self.combobox.config(font=('Nunito', 11, 'bold'), foreground='#111f32', width=46)
        self.combobox.set(self.categorias[0])
        self.combobox.grid(row=0, column=1, padx=10)
        label_palavra = tk.Label(frame1, text='Título ou Palavra')
        label_palavra.config(font=('Nunito', 11, 'bold'), bg='#a1d1d2', fg='#111f32')
        label_palavra.grid(row=1, column=0)
        self.entry_palavra = tk.Entry(frame1, borderwidth=0, relief='groove', width=48)
        self.entry_palavra.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', insertbackground='#a1d1d2')
        self.entry_palavra.grid(row=1, column=1, padx=10, pady=(8, 10))
        botao_pesquisar = tk.Button(frame1, text='Pesquisar', width=12, command=self.pesquisar_nota)
        botao_pesquisar.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', borderwidth=0, relief='groove')
        botao_pesquisar.grid(row=2, column=1, padx=(320, 0))

        label_resultados = tk.Label(self.frame, text='Resultados')
        label_resultados.config(font=('Nunito', 11, 'bold'), bg='#a1d1d2', fg='#111f32')
        label_resultados.grid(row=3, column=0, sticky='W', padx=10, pady=(5, 0))

        # INICIO TREEVIEW #
        estilo = ttk.Style()
        estilo.theme_use('default')  # alt - clam - default
        estilo.configure('Treeview', background='#111f32', fieldbackground='#111f32', foreground='#a1d1d2',
                         font=('Nunito', 11, 'bold'), border=0)
        estilo.configure("Treeview.Heading", background='#111f32', foreground='#a1d1d2', font=('Nunito', 11, 'bold'),
                         border=0)
        estilo.map('Treeview', background=[('selected', '#a1d1d2')], foreground=[('selected', '#111f32')])

        canvas = tk.Canvas(self.frame)
        scroll = ttk.Scrollbar(canvas, orient='vertical')
        canvas.grid(row=4, column=0)

        self.treeview = ttk.Treeview(canvas, yscrollcommand=scroll.set, columns=('categoria', 'titulo', 'descricao'))
        self.treeview.config(show='headings', height=14)
        self.treeview.column('categoria', minwidth=0, width=105, anchor='center')
        self.treeview.column('titulo', minwidth=0, width=165, anchor='center')
        self.treeview.column('descricao', minwidth=0, width=286)
        self.treeview.heading('categoria', text='Categoria')
        self.treeview.heading('titulo', text='Título')
        self.treeview.heading('descricao', text='Descrição')
        self.treeview.grid(row=4, column=0)

        scroll.configure(command=self.treeview.yview)
        scroll.grid(row=0, column=3, rowspan=50, sticky=tk.NS)
        # FIM TREEVIEW #

        frame2 = tk.Frame(self.frame, bg='#a1d1d2')
        frame2.grid(row=5, column=0)
        botao_vizualizar = tk.Button(frame2, text='Ler Nota', width=12, command=self.vizualizar_nota)
        botao_vizualizar.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', borderwidth=0, relief='groove')
        botao_vizualizar.grid(row=0, column=0, padx=(210, 0))
        botao_editar = tk.Button(frame2, text='Editar Nota', width=12, command=self.editar_nota)
        botao_editar.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', borderwidth=0, relief='groove')
        botao_editar.grid(row=0, column=1, padx=5, pady=10)
        botao_excluir = tk.Button(frame2, text='Excluir Nota', width=12, command=self.excluir_nota)
        botao_excluir.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', borderwidth=0, relief='groove')
        botao_excluir.grid(row=0, column=2)

    def pesquisar_nota(self):
        self.treeview.delete(*self.treeview.get_children())
        notas = self.controller_pesquisar.pesquisar_nota(self.combobox.get(), self.entry_palavra.get())
        if notas:
            for id_nota, descricao, titulo, categoria in notas:
                self.treeview.insert("", tk.END, values=(categoria, titulo, descricao), tags=(id_nota,))
        self.combobox.set(self.categorias[0])
        self.entry_palavra.delete(0, 'end')

    def vizualizar_nota(self):
        selecionado = self.treeview.selection()
        for valores in selecionado:
            info = self.treeview.item(valores)
            id_nota = info['tags'][0]
            conteudo_nota = info['values']
            self.nota = list([id_nota] + conteudo_nota)
        self.controller_vizualizar.vizualizar_nota(self.frame, self.nota)

    def editar_nota(self):
        selecionado = self.treeview.selection()
        for valores in selecionado:
            info = self.treeview.item(valores)
            id_nota = info['tags'][0]
            conteudo_nota = info['values']
            self.nota = list([id_nota] + conteudo_nota)
        self.controller_editar.editar_nota(self.nota)

    def excluir_nota(self):
        selecionado = self.treeview.selection()
        for valores in selecionado:
            info = self.treeview.item(valores)
            id_nota = info['tags'][0]
            conteudo_nota = info['values']
            self.nota = list([id_nota] + conteudo_nota)
        self.controller_excluir.excluir_nota(self.nota, self.treeview)
