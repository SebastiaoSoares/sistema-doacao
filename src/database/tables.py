from sqlalchemy import Table, String, Column, MetaData, Integer, Date, ForeignKey, Boolean
from src.database.database import Database
database = Database()

class Tabela():
    '''
    A classe que organiza e cria as tabelas do banco de dados
    '''

    def __init__(self):
        self.metadata = MetaData() # Função para criar as tabelas

# <--------------------------------------------------Tabelas-------------------------------------------------->
             
            # Doações
        self.doacao = Table(
            'doacao', self.metadata,
            Column('id_doacao', Integer, primary_key=True, autoincrement=True),
            Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), nullable=False),
            Column('data_doacao', Date, nullable=False),
            Column('motivo_recusa', String(255)),
            Column('status_atual', String(40), nullable=False)
        )

        self.doacaoItem = Table(
            'doacaoItem', self.metadata,
            Column('id_doacao', Integer, ForeignKey('doacao.id_doacao'), primary_key=True),
            Column('id_item', Integer, ForeignKey('itens.id_item'), primary_key=True),
            Column('quantidade', Integer, nullable=False)
        )

            # Usuários
        self.usuarios = Table('usuarios', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('nome', String(70)),
            Column('email', String(70)),
            Column('senha', String(70)),
            Column('endereco', String(70)),
            Column('status', String(40)),
            Column('identificador', String(40)), # CPF ou CNPJ
            Column('tipo_perfil', String(40))
        )

        self.pessoaJuridica = Table('pessoaJuridica', self.metadata,
            Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), primary_key=True),
            Column('user_cnpj', String(14), unique=True, nullable=False),
            Column('razao_social', String(100), nullable=False)
        )

        self.pessoaFisica = Table('pessoaFisica', self.metadata,
            Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), primary_key=True),
            Column('user_cpf', String(11), unique=True, nullable=False),
            Column('data_nascimento', Date)
        )

            # Categoria
        self.itemCategoria = Table('itemCategoria', self.metadata,
            Column('id_categoria', Integer, primary_key=True, autoincrement=True),
            Column('nome_categoria', String(50), unique=True, nullable=False)
        )

            # Itens
        self.itens = Table('itens', self.metadata,
            Column('id_item', Integer, primary_key=True, autoincrement=True),
            Column('id_categoria', Integer, ForeignKey('itemCategoria.id_categoria')),
            Column('descricao', String(255)),
            Column('unidade_medida', String(50))
        )

            # Distribuição
        self.distribuicao = Table('distribuicao', self.metadata,
            Column('id_distribuicao', Integer, primary_key=True, autoincrement=True),
            Column('id_pedido', Integer, ForeignKey('pedidoAuxilio.id_pedido')),
            Column('id_doacao', Integer, ForeignKey('doacao.id_doacao')),
            Column('user_cnpj', String(14), ForeignKey('pessoaJuridica.user_cnpj')),
            Column('data_entrega', Date, nullable=False),
            Column('validacao_recebimento', Boolean, default=False)
        )
        
        self.distribuicaoItem = Table('distribuicaoItem', self.metadata,
            Column('id_distribuicao', Integer, ForeignKey('distribuicao.id_distribuicao'), primary_key=True),
            Column('id_item', Integer, ForeignKey('itens.id_item'), primary_key=True),
            Column('user_cnpj', String(14), ForeignKey('pessoaJuridica.user_cnpj'))
        )

        # TODO: self.rastreio = Table('rastreio', self.metadata,) 
           
            # Pedido de auxílio
        self.pedidoAuxilio = Table('pedidoAuxilio', self.metadata,
            Column('id_pedido', Integer, primary_key=True, autoincrement=True),
            Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), nullable=False),
            Column('flag_fraude', Boolean, default=False),
            Column('status', String(40), nullable=False),
            Column('justificativa', String(500), nullable=False),
            Column('data_pedido', Date, nullable=False)
        )

            # Voluntariado
        self.vagaVoluntario = Table('vagaVoluntario', self.metadata,
            Column('id_vaga', Integer, primary_key=True, autoincrement=True),
            Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), nullable=False),
            Column('data_evento', Date, nullable=False),
            Column('carga_horaria', String(50)),
            Column('titulo', String(100), nullable=False),
            Column('descricao', String(500), nullable=False)
        )
        
        self.inscricao = Table('inscricao', self.metadata,
            Column('id_inscricao', Integer, primary_key=True, autoincrement=True),
            Column('id_vaga', Integer, ForeignKey('vagaVoluntario.id_vaga'), nullable=False),
            Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), nullable=False),
            Column('data_inscricao', Date, nullable=False),
            Column('status', String(40), nullable=False),
            Column('checkin_presenca', Boolean, default=False)
        )

        
    def criar_tabelas(self, database):
        '''
        Cria as tabelas no banco de dados.
        '''

        self.metadata.create_all(database.session)