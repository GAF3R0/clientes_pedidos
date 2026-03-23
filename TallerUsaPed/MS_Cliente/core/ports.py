from abc import ABC, abstractmethod
from typing import Optional
from .entities import Cliente

class ClienteRepository(ABC):
    @abstractmethod
    def get_by_id(self, cliente_id: int) -> Optional[Cliente]:
        pass

    @abstractmethod
    def save(self, cliente: Cliente) -> Cliente:
        pass