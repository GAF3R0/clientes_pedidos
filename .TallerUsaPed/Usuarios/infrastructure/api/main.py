from fastapi import APIRouter, HTTPException
from TallerUsaPed.Usuarios.application.services.user_services import UserService

# Definimos el router
router = APIRouter()

def init_routes(service: UserService):
    
    @router.post("/usuarios/", status_code=201)
    def registrar_usuario(idusuario: str, username: str, email: str):
        # Requisito: Registrar usuario con mínimo 3 atributos
        return service.registrar_usuario(idusuario, username, email)

    @router.get("/usuarios/{idusuario}")
    def consultar_usuario(idusuario: str):
        # Requisito: Consultar información del usuario
        user = service.consultar_usuario(idusuario)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    @router.put("/usuarios/{idusuario}")
    def modificar_usuario(idusuario: str, username: str = None, email: str = None):
        # Requisito: Modificar nombre o email existente
        user = service.modificar_usuario(idusuario, username, email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no se pudo actualizar")
        return user

    @router.delete("/usuarios/{idusuario}")
    def eliminar_usuario(idusuario: str):
        # Requisito: Eliminar usuario
        if not service.eliminar_usuario(idusuario):
            raise HTTPException(status_code=404, detail="Error al eliminar")
        return {"message": f"Usuario {idusuario} eliminado"}

    return router