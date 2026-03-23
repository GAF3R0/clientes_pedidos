from typing import Optional
from TallerUsaPed.Usuarios.domain.user import User
from TallerUsaPed.Usuarios.application.ports.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        # Base de datos simulada en memoria
        self._users = {}

    def save(self, user: User) -> User:
        self._users[user.idusuario] = user
        return user

    def get_by_id(self, idusuario: str) -> Optional[User]:
        return self._users.get(idusuario)

    def update(self, idusuario: str, user: User) -> Optional[User]:
        if idusuario in self._users:
            self._users[idusuario] = user
            return user
        return None

    def delete(self, idusuario: str) -> bool:
        if idusuario in self._users:
            del self._users[idusuario]
            return True
        return False