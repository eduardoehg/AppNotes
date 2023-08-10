from .connection import Connection


class PesquisarDao:

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

    def pesquisar_id(self, categoria):
        try:
            self.connection.conectar()
            comando = f'SELECT idCategoria FROM categorias WHERE nome = "{categoria}"'
            id_categoria = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return id_categoria[0][0]
        except Exception as ex:
            print(ex)

    def pesquisar_nome_categoria(self, id_categoria):
        try:
            self.connection.conectar()
            comando = f'SELECT nome FROM categorias WHERE idCategoria = {id_categoria}'
            nome = self.connection.pesquisar_bd(comando)
            self.connection.desconectar()
            return nome[0][0]
        except Exception as ex:
            print(ex)

    def pesquisar_nota(self, categoria, palavra):
        if categoria and palavra:
            try:
                id_categorias = self.pesquisar_id(categoria)
                self.connection.conectar()
                comando1 = f'SELECT * FROM notas WHERE idCategoria = {id_categorias}'
                lista1 = self.connection.pesquisar_bd(comando1)
                comando2 = f'SELECT * FROM notas WHERE titulo LIKE "%{palavra}%" OR descricao LIKE "%{palavra}%"'
                lista2 = self.connection.pesquisar_bd(comando2)
                self.connection.desconectar()
                notas = []
                for item in lista1 + lista2:
                    if item not in notas:
                        item[-1] = self.pesquisar_nome_categoria(item[-1])
                        notas.append(item)
                return notas
            except Exception as ex:
                print(ex)
        else:
            if categoria:
                try:
                    id_categoria = self.pesquisar_id(categoria)
                    self.connection.conectar()
                    comando = f'SELECT * FROM notas WHERE idCategoria = {id_categoria}'
                    resultado = self.connection.pesquisar_bd(comando)
                    self.connection.desconectar()
                    notas = []
                    for item in resultado:
                        if item not in notas:
                            item[-1] = self.pesquisar_nome_categoria(item[-1])
                            notas.append(item)
                    return notas
                except Exception as ex:
                    print(ex)
            else:
                try:
                    self.connection.conectar()
                    comando = f'SELECT * FROM notas WHERE titulo LIKE "%{palavra}%" OR descricao LIKE "%{palavra}%"'
                    resultado = self.connection.pesquisar_bd(comando)
                    self.connection.desconectar()
                    notas = []
                    for item in resultado:
                        if item not in notas:
                            item[-1] = self.pesquisar_nome_categoria(item[-1])
                            notas.append(item)
                    return notas
                except Exception as ex:
                    print(ex)


class ExcluirDao:

    def __init__(self):

        self.connection = Connection()

    def excluir_nota(self, nota):
        id_nota = nota[0]
        try:
            self.connection.conectar()
            comando = f'DELETE FROM notas WHERE idNota = {id_nota}'
            self.connection.alterar_bd(comando)
            self.connection.desconectar()
        except Exception as ex:
            print(ex)
