class PedidoAuxilio:
    '''
    Classe que representa um pedido de auxílio, ou seja, uma doação.
    '''
def __init__(self, id_usuario, flag_fraude, status, justificativa, data_pedido, id=None):
    self.id_usuario = id_usuario
    self.flag_fraude = flag_fraude
    self.status = status
    self.justificativa = justificativa
    self.data_pedido = data_pedido
    self.id = id