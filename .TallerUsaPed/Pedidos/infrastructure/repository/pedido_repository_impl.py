from TallerUsaPed.Pedidos.application.ports.pedido_repository import PedidoRepository
from TallerUsaPed.Pedidos.domain.pedido import Pedido

class InMemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        self._pedidos = []

    def save(self, pedido: Pedido) -> Pedido:
        self._pedidos.append(pedido)
        return pedido

    def get_all(self):
        return self._pedidos