from uteis import msg_sucesso, msg_erro
from model.inserir_model import InserirModel


class InserirController:

    def __init__(self):
        self.model = InserirModel()

    def listar_categorias(self):
        return self.model.listar_categorias()

    def inserir_nota(self, categoria, titulo, descricao, limpar):
        if categoria == 'Selecione':
            msg_erro('Selecione uma Categoria para Salvar a Nota!\n\nVocê pode criar uma nova categoria '
                     'em:\nCategorias -> Inserir Categoria')
        else:
            if categoria and titulo and descricao:
                self.model.inserir_nota(categoria, titulo, descricao)
                msg_sucesso('Nota Salva com Sucesso!')
                limpar()
            else:
                msg_erro('Informe um Título e uma Descrição para Salvar a Nota!')

    def editar_nota(self, categoria, titulo, descricao, id_nota, limpar):
        if categoria == 'Selecione':
            msg_erro('Selecione uma Categoria para Salvar a Nota!')
        else:
            if categoria and titulo and descricao and id_nota:
                self.model.editar_nota(categoria, titulo, descricao, id_nota)
                msg_sucesso('Nota Editada com Sucesso!')
                limpar()
            else:
                msg_erro('Informe um Título e uma Descrição para Salvar a Nota!')
