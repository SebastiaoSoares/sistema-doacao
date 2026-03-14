class Usuario():
    '''
    Classe que representa o usuário no sistema.
    '''
    def __init__(self, nome, email, senha, endereco, status, identificador, tipo_perfil, id=None):
            self.id = id
            self.nome = nome
            self.email = email
            self.senha = senha
            self.endereco = endereco
            self.status = status
            self.identificador = identificador
            self.tipo_perfil = tipo_perfil