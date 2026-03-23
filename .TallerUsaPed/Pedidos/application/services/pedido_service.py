from TallerUsaPed.Pedidos.domain.pedido import Pedido
from TallerUsaPed.Pedidos.application.ports.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository
    
    def crear_pedido(self, idpedido: str, idusuario: str, total: float) -> Pedido:
        # Creación con los 3 atributos requeridos
        nuevo_pedido = Pedido(idpedido=idpedido, idusuario=idusuario, total=total)
        return self.repository.save(nuevo_pedido)

    def listar_pedidos(self):
        return self.repository.get_all()