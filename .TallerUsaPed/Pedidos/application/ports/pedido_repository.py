from abc import ABC, abstractmethod
from TallerUsaPed.Pedidos.domain.pedido import Pedido

class PedidoRepository(ABC):
    @abstractmethod
    def save(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def get_all(self):
        pass