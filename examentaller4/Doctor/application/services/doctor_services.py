from typing import Optional
from examentaller4.Doctor.domain.doctor import Doctor
from examentaller4.Doctor.application.ports.doctor_repository import DoctorRepository

class DoctorService:
    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def registrar_doctor(self, iddoc: str, namedoc: str, especialidad: str) -> Doctor:
        nuevo_doctor = Doctor(
            iddoc=iddoc, 
            namedoc=namedoc, 
            especialidad=especialidad
        )
        return self.repository.save(nuevo_doctor)

    def consultar_doctor(self, iddoc: str) -> Optional[Doctor]:
        return self.repository.get_by_id(iddoc)

    def modificar_doctor(self, iddoc: str, namedoc: Optional[str] = None, especialidad: Optional[str] = None) -> Optional[Doctor]:
        doctor_existente = self.repository.get_by_id(iddoc)
        
        if doctor_existente:
            if namedoc:
                doctor_existente.namedoc = namedoc
            if email:
                doctor_existente.especialidad = especialidad
            
            return self.repository.update(iddoc, doctor_existente)
        return None

    def eliminar_doctor(self, iddoc: str) -> bool:
        return self.repository.delete(iddoc)