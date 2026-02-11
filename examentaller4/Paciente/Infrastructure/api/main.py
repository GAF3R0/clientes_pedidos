from fastapi import APIRouter, HTTPException
from examentaller4.Paciente.application.services.paciente_services import PacienteService

router = APIRouter()

def init_routes(service: PacienteService):
    
    @router.post("/paciente/", status_code=201)
    def registrar_paciente(idpaciente: str, namepaciente: str, email: str):
        return service.registrar_paciente(idpaciente, namepaciente, email)

    @router.get("/paciente/{idpaciente}")
    def consultar_paciente(idpaciente: str):
        paciente = service.consultar_paciente(idpaciente)
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        return paciente

    @router.put("/paciente/{idpaciente}")
    def modificar_paciente(idpaciente: str, namepaciente: str = None, email: str = None):
        user = service.modificar_paciente(idpaciente, namepaciente, email)
        if not user:
            raise HTTPException(status_code=404, detail="Paciente no se pudo actualizar")
        return user

    @router.delete("/paciente/{idpaciente}")
    def eliminar_paciente(idpaciente: str):
        if not service.eliminar_paciente(idpaciente):
            raise HTTPException(status_code=404, detail="Error al eliminar")
        return {"message": f"Paciente {idpaciente} eliminado"}

    return router