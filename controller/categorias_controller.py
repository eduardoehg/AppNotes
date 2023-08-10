from uteis import msg_sucesso, msg_erro
from model.categorias_model import InserirCategoriaModel, EditarCategoriaModel, ExcluirCategoriModel


class InserirCategoriaController:

    def __init__(self):
        self.model = InserirCategoriaModel()

    def inserir(self, janela, nome):
        if nome:
            msg_sucesso('Categoria Criada com Sucesso!')
            janela.destroy()
        else:
            msg_erro('Informe o nome da Categoria para Salvar!')
        self.model.inserir(nome)


class EditarCategoriaController:

    def __init__(self):
        self.model = EditarCategoriaModel()

    def carregar_categorias(self):
        return self.model.carregar_categorias()

    def editar(self, janela, categoria, nome):
        if nome and categoria:
            msg_sucesso('Categoria Alterada com Sucesso!')
            janela.destroy()
        else:
            msg_erro('Selecione e informe o novo nome da Categoria para Salvar!')
        self.model.editar(nome, categoria)


class ExcluirCategoriaController:

    def __init__(self):
        self.model = ExcluirCategoriModel()

    def carregar_categorias(self):
        return self.model.carregar_categorias()

    def excluir(self, janela, categoria):
        if categoria:
            msg_sucesso('Categoria Excluida com Sucesso!')
            janela.destroy()
        else:
            msg_erro('Selecione uma Categoria para Excluir!')
        self.model.excluir(categoria)
