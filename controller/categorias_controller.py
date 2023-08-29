from uteis import msg_sucesso, msg_erro
from model.categorias_model import InserirCategoriaModel, EditarCategoriaModel, ExcluirCategoriModel
from view.inserir_view import InserirView


class InserirCategoriaController:

    def __init__(self, janela_base):
        self.model = InserirCategoriaModel()
        self.view = InserirView(janela_base)

    def inserir(self, janela, nome):
        if nome:
            self.model.inserir(nome)
            msg_sucesso('Categoria Criada com Sucesso!')
            self.view.atualizar_categorias()
            janela.destroy()
        else:
            janela.grab_set()
            msg_erro('Informe o nome da Categoria para Salvar!')


class EditarCategoriaController:

    def __init__(self, janela_base):
        self.model = EditarCategoriaModel()
        self.view = InserirView(janela_base)

    def carregar_categorias(self):
        return self.model.carregar_categorias()

    def editar(self, janela, categoria, nome):
        if nome and categoria and categoria != 'Selecione':
            self.model.editar(nome, categoria)
            msg_sucesso('Categoria Alterada com Sucesso!')
            self.view.atualizar_categorias()
            janela.destroy()
        else:
            janela.grab_set()
            msg_erro('Selecione e informe o novo nome da Categoria para Salvar!')


class ExcluirCategoriaController:

    def __init__(self, janela_base):
        self.model = ExcluirCategoriModel()
        self.view = InserirView(janela_base)

    def carregar_categorias(self):
        return self.model.carregar_categorias()

    def excluir(self, janela, categoria):
        if categoria != 'Selecione':
            self.model.excluir(categoria)
            msg_sucesso('Categoria Excluida com Sucesso!')
            self.view.atualizar_categorias()
            janela.destroy()
        else:
            janela.grab_set()
            msg_erro('Selecione uma Categoria para Excluir!')
