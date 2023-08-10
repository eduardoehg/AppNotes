from .connection import Connection


class InserirDao:

    def __init__(self):
        self.connection = Connection()

    def listar_categorias(self):
        try:
            self.connection.conectar()
            comando = 'SELECT nome FROM categorias'
            nomes = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return nomes
        except Exception as ex:
            print(ex)

    def pesquisar_id(self, categoria):
        try:
            self.connection.conectar()
            comando = f'SELECT idCategoria FROM categorias WHERE nome = "{categoria}"'
            id_categoria = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return id_categoria[0][0]
        except Exception as ex:
            print(ex)

    def inserir_nota(self, titulo, descricao, id_categoria):
        try:
            self.connection.conectar()
            comando = f'''
            INSERT INTO notas (titulo, descricao, idCategoria)
            VALUES ("{titulo}", "{descricao}", {id_categoria})
            '''
            self.connection.alterar_bd(comando)
            self.connection.desconectar()
        except Exception as ex:
            print(ex)

    def editar_nota(self, titulo, descricao, id_categoria, id_nota):
        try:
            self.connection.conectar()
            comando = f'''
            UPDATE notas
            SET descricao = "{descricao}", titulo = "{titulo}", idCategoria = {id_categoria}
            WHERE idNota = {id_nota};
            '''
            self.connection.alterar_bd(comando)
            self.connection.desconectar()
        except Exception as ex:
            print(ex)
