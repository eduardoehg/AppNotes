from dao.categorias_dao import InserirCategoriaDao, EditarCategoriaDao, ExcluirCategoriaDao


class InserirCategoriaModel:

    def __init__(self):
        self.dao = InserirCategoriaDao()
        self.nome = None

    def inserir(self, nome):
        self.nome = nome
        self.dao.inserir(self.nome)


class EditarCategoriaModel:

    def __init__(self):
        self.dao = EditarCategoriaDao()
        self.nome = None
        self.categoria = None

    def carregar_categorias(self):
        return self.dao.carregar_categorias()

    def editar(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.dao.editar(self.nome, self.categoria)


class ExcluirCategoriModel:

    def __init__(self):
        self.dao = ExcluirCategoriaDao()
        self.categoria = None

    def carregar_categorias(self):
        return self.dao.carregar_categorias()

    def excluir(self, categoria):
        self.categoria = categoria
        self.dao.excluir(categoria)
