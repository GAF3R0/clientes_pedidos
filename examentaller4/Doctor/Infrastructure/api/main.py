from fastapi import APIRouter, HTTPException
from examentaller4.Doctor.application.services.doctor_services import DoctorService

router = APIRouter()

def init_routes(service: DoctorService):
    
    @router.post("/doctores/", status_code=201)
    def registrar_doctor(iddoc: str, namedoc: str, especialidad: str):
        return service.registrar_doctor(iddoc, namedoc, especialidad)

    @router.get("/doctores/{iddoc}")
    def consultar_doctor(iddoc: str):
        doctor = service.consultar_doctor(iddoc)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")
        return doctor

    @router.put("/doctores/{iddoc}")
    def modificar_doctor(iddoc: str, namedoc: str = None, especialidad: str = None):
        doctor = service.modificar_doctor(iddoc, namedoc, especialidad)
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor no se pudo actualizar")
        return doctor

    @router.delete("/doctor/{iddoc}")
    def eliminar_doctor(iddoc: str):
        if not service.eliminar_doctor(iddoc):
            raise HTTPException(status_code=404, detail="Error al eliminar")
        return {"message": f"Doctor {iddoc} eliminado"}

    return router