from abc import ABC, abstractmethod

class PedidoRepository(ABC):
    @abstractmethod
    def save(self, pedido: dict): pass

class ClienteExternalService(ABC):
    @abstractmethod
    async def verificar_cliente(self, cliente_id: int) -> bool: pass

class EventPublisher(ABC):
    @abstractmethod
    def publish(self, message: str): pass