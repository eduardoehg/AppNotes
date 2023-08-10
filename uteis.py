from tkinter import messagebox


def dimensionamento(janela, largura, altura, teto=0):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela - largura) // 2
    y = (altura_tela - (altura + teto)) // 2
    return largura, altura, x, y


def limpar_tela(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def msg_sucesso(msg):
    messagebox.showinfo(title='SUCESSO!', message=f'{msg}')


def msg_erro(msg):
    messagebox.showinfo(title='ERRO!', message=f'{msg}')
