from src.domain.usuarios import Usuario
from src.repositories.repository import Repo
from src.database.database import Database
from src.database.tables import Tabela
from sqlalchemy import text

db = Database()
tb = Tabela()

class Repo_usuario(Repo):
    '''
    Classe que interaje com o Banco de Dados dos usuários
    '''
    def __init__(self, database, table):
        super().__init__(database, table)

    def create(self, usuario):
        '''
        Recebe um objeto de usuário e cadastra ele no banco de dados
        '''
        conexao = self.database.connect()
        if conexao:
            try:
                query = text ("""INSERT INTO usuarios (nome, email, senha, endereco, status, identificador, tipo_perfil)
                            VALUES (:nome, :email, :senha, :endereco, :status, :identificador, :tipo_perfil)
                            ON CONFLICT (id) DO NOTHING""")
                
                conexao.execute(query, {"nome" : usuario.nome, "email" : usuario.email, "senha" : usuario.senha, "endereco" : usuario.endereco, "status" : usuario.status, "identificador" : usuario.identificador, "tipo_perfil" : usuario.tipo_perfil})

                conexao.commit()
                conexao.close()
            except Exception as erro:
                print(f"Não foi possível realizar o cadastro.\nErro: {erro}")
            return "Usuário cadastrado"
        else:
            return "Não foi possível conectar"
        
    def read(self, doacao_id):
        pass

    def update(self, doacao_id):
        pass

    def inactivate(self):
        pass