from uteis import dimensionamento, gerar_pdf, gerar_word
import tkinter as tk


class VizualizarView:

    def __init__(self):

        self.frame = None
        self.titulo = None
        self.nota = None

    def tela_vizualizar_nota(self, frame, titulo, nota):
        self.frame = frame
        self.titulo = titulo
        self.nota = nota
        texto = f'Título: {self.titulo}\n\n{self.nota}'

        janela = tk.Toplevel(self.frame)
        largura, altura, x, y = dimensionamento(janela, 638, 670, 67)
        janela.geometry(f'{largura}x{altura}+{x}+{y}')
        janela.config(bg='#a1d1d2')
        janela.title(f'Vizualizar Nota')
        janela.grid_propagate(False)

        frame_cabecalho = tk.Frame(janela, bg='#a1d1d2', width=600, height=50)
        frame_cabecalho.grid_propagate(False)
        frame_cabecalho.grid(row=0, column=0, pady=10, padx=20)
        frame_corpo = tk.Frame(janela, bg='#a1d1d2', width=600, height=580, borderwidth=1, relief='solid')
        frame_corpo.grid(row=1, column=0)
        frame_corpo.grid_propagate(False)

        botao_pdf = tk.Button(frame_cabecalho, text='  Gerar PDF  ', width=12, command=self.pdf)
        botao_pdf.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 12, 'bold'), relief='groove', borderwidth=0)
        botao_pdf.grid(row=0, column=1, pady=10)
        botao_word = tk.Button(frame_cabecalho, text='  Gerar Word  ', width=12, command=self.word)
        botao_word.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 12, 'bold'), relief='groove', borderwidth=0)
        botao_word.grid(row=0, column=2, padx=(5, 220), pady=10)

        botao_voltar = tk.Button(frame_cabecalho, text='  Voltar  ', width=12, command=janela.destroy)
        botao_voltar.config(bg='#111f32', fg='#a1d1d2', font=('Nunito', 12, 'bold'), relief='groove', borderwidth=0)
        botao_voltar.grid(row=0, column=3, pady=10)

        nota = tk.Text(frame_corpo, wrap='word', width=64, height=27)
        nota.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2')
        nota.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        nota.insert(1.0, texto)
        nota.config(state=tk.DISABLED)

    def pdf(self):
        gerar_pdf(self.titulo, self.nota)

    def word(self):
        gerar_word(self.titulo, self.nota)
