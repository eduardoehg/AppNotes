from uteis import dimensionamento
import tkinter as tk


class VizualizarView:

    def __init__(self):

        self.frame = None
        self.nota = None

    def tela_vizualizar_nota(self, frame, titulo, corpo):
        self.frame = frame
        texto = f'Título: {titulo}\n\nNota:\n{corpo}'

        janela = tk.Toplevel(self.frame)
        largura, altura, x, y = dimensionamento(janela, 638, 650, 85)
        janela.geometry(f'{largura}x{altura}+{x}+{y}')
        janela.config(bg='#a1d1d2')
        janela.title(f'Vizualizar Nota')
        janela.grid_propagate(False)

        barra = tk.Menu(janela)
        janela.config(menu=barra)
        barra.add_command(label='Gerar PDF')
        barra.add_command(label='Voltar', command=janela.destroy)

        frame = tk.Frame(janela)
        frame.config(bg='#a1d1d2', width=600, height=610, borderwidth=1, relief='solid')
        frame.grid(row=0, column=0, pady=20, padx=20)
        frame.grid_propagate(False)

        self.nota = tk.Label(frame, text=texto, width=64, height=29)
        self.nota.config(font=('Nunito', 11, 'bold'), bg='#111f32', fg='#a1d1d2', anchor='nw')
        self.nota.grid(row=0, column=0, padx=10, pady=10)