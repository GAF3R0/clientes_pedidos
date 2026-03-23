from typing import Optional
# RUTAS ABSOLUTAS: Obligatorio para evitar el ModuleNotFoundError
from TallerUsaPed.Usuarios.domain.user import User
from TallerUsaPed.Usuarios.application.ports.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def registrar_usuario(self, idusuario: str, username: str, email: str) -> User:
        # Requisito: Mínimo 3 atributos (id, nombre, email)
        nuevo_usuario = User(
            idusuario=idusuario, 
            username=username, 
            email=email
        )
        return self.repository.save(nuevo_usuario)

    def consultar_usuario(self, idusuario: str) -> Optional[User]:
        return self.repository.get_by_id(idusuario)

    def modificar_usuario(self, idusuario: str, username: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
        usuario_existente = self.repository.get_by_id(idusuario)
        
        if usuario_existente:
            if username:
                usuario_existente.username = username
            if email:
                usuario_existente.email = email
            
            return self.repository.update(idusuario, usuario_existente)
        return None

    def eliminar_usuario(self, idusuario: str) -> bool:
        return self.repository.delete(idusuario)