from uteis import msg_erro, msg_sucesso
from view.inserir_view import InserirView
from view.vizualizar_view import VizualizarView
from model.pesquisar_model import PesquisarModel, ExluirModel


class PesquisarController:

    def __init__(self):
        self.model = PesquisarModel()

    def carregar_categorias(self):
        return self.model.carregar_cateogrias()

    def pesquisar_nota(self, categoria, palavra):
        if categoria == 'Todas as Notas':
            notas = self.model.pesquisar_nota()
            return notas
        elif categoria == 'Selecione':
            if palavra:
                notas = self.model.pesquisar_nota(palavra=palavra)
                return notas
            else:
                msg_erro('Para realizar a pesquisa, selecione uma categoria ou informe uma palavra!')
        else:
            if categoria and palavra:
                notas = self.model.pesquisar_nota(categoria=categoria, palavra=palavra)
                return notas
            else:
                notas = self.model.pesquisar_nota(categoria=categoria)
                return notas


class VizualizarNotaController:

    def __init__(self):
        self.model = VizualizarView()

    def vizualizar_nota(self, frame, nota):
        if nota:
            titulo = nota[2]
            corpo = nota[3]
            self.model.tela_vizualizar_nota(frame, titulo, corpo)
        else:
            msg_erro('Selecione uma Nota para ser Visualizada!')


class EditarNotaController:

    def __init__(self, frame):

        self.view = InserirView(frame)

    def editar_nota(self, nota):
        if nota:
            id_nota, categoria, titulo, nota = nota
            self.view.editar_nota(categoria, titulo, nota, id_nota)
        else:
            msg_erro('Selecione uma Nota para ser Editada!')


class ExcluirNotaController:

    def __init__(self):

        self.model = ExluirModel()

    def excluir_nota(self, nota, treeview):
        if nota:
            self.model.excluir_nota(nota)
            msg_sucesso('Nota Excluída com Sucesso!')
            treeview.delete(*treeview.get_children())
        else:
            msg_erro('Selecione uma Nota para ser Excluída!')
