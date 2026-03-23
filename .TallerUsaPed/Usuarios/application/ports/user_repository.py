from abc import ABC, abstractmethod
from typing import Optional
# Importamos la entidad de dominio usando la ruta absoluta
from TallerUsaPed.Usuarios.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, idusuario: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, idusuario: str, user: User) -> Optional[User]:
        pass

    @abstractmethod
    def delete(self, idusuario: str) -> bool:
        pass