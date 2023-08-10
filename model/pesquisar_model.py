from dao.pesquisar_dao import PesquisarDao, ExcluirDao


class PesquisarModel:

    def __init__(self):
        self.dao = PesquisarDao()
        self.categoria = None
        self.palavra = None

    def carregar_cateogrias(self):
        return self.dao.carregar_categorias()

    def pesquisar_nota(self, categoria=None, palavra=None):
        self.categoria = categoria
        self.palavra = palavra
        notas = self.dao.pesquisar_nota(self.categoria, self.palavra)
        return notas


class ExluirModel:

    def __init__(self):

        self.dao = ExcluirDao()

    def excluir_nota(self, nota):
        self.dao.excluir_nota(nota)
