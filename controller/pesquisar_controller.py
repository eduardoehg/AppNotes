from uteis import msg_erro
from view.inserir_view import InserirView
from view.vizualizar_view import VizualizarView
from model.pesquisar_model import PesquisarModel, ExluirModel


class PesquisarController:

    def __init__(self):
        self.model = PesquisarModel()

    def carregar_categorias(self):
        return self.model.carregar_cateogrias()

    def pesquisar_nota(self, categoria, palavra):
        if categoria == 'Selecione':
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
        titulo = nota[2]
        corpo = nota[3]
        self.model.tela_vizualizar_nota(frame, titulo, corpo)


class EditarNotaController:

    def __init__(self, frame):

        self.view = InserirView(frame)

    def editar_nota(self, nota):
        id_nota, categoria, titulo, nota = nota
        self.view.editar_nota(categoria, titulo, nota, id_nota)


class ExcluirNotaController:

    def __init__(self):

        self.model = ExluirModel()

    def excluir_nota(self, nota):
        if nota:
            self.model.excluir_nota(nota)
