from dao.inserir_dao import InserirDao


class InserirModel:

    def __init__(self):
        self.categoria = None
        self.titulo = None
        self.descricao = None
        self.id_categoria = None
        self.dao = InserirDao()

    def listar_categorias(self):
        categorias = self.dao.listar_categorias()
        return categorias

    def pesquisar_id_categoria(self, cat):
        self.id_categoria = self.dao.pesquisar_id(cat)

    def inserir_nota(self, categoria, titulo, descricao):
        self.categoria = categoria
        self.titulo = titulo
        self.descricao = descricao
        self.pesquisar_id_categoria(self.categoria)
        self.dao.inserir_nota(self.titulo, self.descricao, self.id_categoria)

    def editar_nota(self, categoria, titulo, descricao, id_nota):
        self.categoria = categoria
        self.titulo = titulo
        self.descricao = descricao
        self.pesquisar_id_categoria(self.categoria)
        self.dao.editar_nota(self.titulo, self.descricao, self.id_categoria, id_nota)
