import sqlite3


class Connection:

    def __init__(self):
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect('database.db')
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.cursor.close()
        self.conexao.close()

    def alterar_bd(self, comando):
        self.cursor.execute(comando)
        self.conexao.commit()

    def pesquisar_bd(self, comando):
        resultados = []
        self.cursor.execute(comando)
        for linha in self.cursor.fetchall():
            resultado = list(linha)
            resultados.append(resultado)
        return resultados
