from .connection import Connection


class InserirCategoriaDao:

    def __init__(self):
        self.connection = Connection()

    def inserir(self, nome):
        try:
            self.connection.conectar()
            comando = f'''
            INSERT INTO categorias (nome)
            VALUES("{nome}")
            '''
            self.connection.alterar_bd(comando)
            self.connection.desconectar()
        except Exception as ex:
            print(ex)


class EditarCategoriaDao:

    def __init__(self):
        self.connection = Connection()

    def carregar_categorias(self):
        try:
            self.connection.conectar()
            comando = f'SELECT nome FROM categorias'
            categorias = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return categorias
        except Exception as ex:
            print(ex)

    def pesquisar(self, categoria):
        try:
            self.connection.conectar()
            comando = f'SELECT idCategoria FROM categorias WHERE nome = "{categoria}"'
            id_categoria = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return id_categoria[0][0]
        except Exception as ex:
            print(ex)

    def editar(self, nome, categoria):
        id_categoria = self.pesquisar(categoria)
        try:
            self.connection.conectar()
            comando = f'''
            UPDATE categorias
            SET nome = "{nome}"
            WHERE idCategoria = {id_categoria};
            '''
            self.connection.alterar_bd(comando)
            self.connection.desconectar()
        except Exception as ex:
            print(ex)


class ExcluirCategoriaDao:

    def __init__(self):
        self.connection = Connection()

    def carregar_categorias(self):
        try:
            self.connection.conectar()
            comando = f'SELECT nome FROM categorias'
            categorias = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return categorias
        except Exception as ex:
            print(ex)

    def pesquisar(self, categoria):
        try:
            self.connection.conectar()
            comando = f'SELECT idCategoria FROM categorias WHERE nome = "{categoria}"'
            id_categoria = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return id_categoria[0][0]
        except Exception as ex:
            print(ex)

    def excluir(self, categoria):
        id_categoria = self.pesquisar(categoria)
        try:
            self.connection.conectar()
            comando1 = f'DELETE FROM notas WHERE idCategoria = {id_categoria}'
            self.connection.alterar_bd(comando1)
            comando2 = f'DELETE FROM categorias WHERE idCategoria = {id_categoria}'
            self.connection.alterar_bd(comando2)
            self.connection.desconectar()
        except Exception as ex:
            print(ex)
