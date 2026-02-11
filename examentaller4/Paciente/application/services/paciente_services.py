from typing import Optional
from examentaller4.Paciente.domain.paciente import Paciente
from examentaller4.Paciente.application.ports.paciente_repository import PacienteRepository

class PacienteService:
    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    def registrar_paciente(self, idpaciente: str, namepaciente: str, email: str) -> Paciente:
        # Requisito: Mínimo 3 atributos (id, nombre, email)
        nuevo_paciente = Paciente(
            idpaciente=idpaciente, 
            namepaciente=namepaciente, 
            email=email
        )
        return self.repository.save(nuevo_paciente)

    def consultar_paciente(self, idpaciente: str) -> Optional[Paciente]:
        return self.repository.get_by_id(idpaciente)

    def modificar_paciente(self, idpaciente: str, namepaciente: Optional[str] = None, email: Optional[str] = None) -> Optional[Paciente]:
        paciente_existente = self.repository.get_by_id(idpaciente)
        
        if paciente_existente:
            if namepaciente:
                paciente_existente.namepaciente = namepaciente
            if email:
                paciente_existente.email = email
            
            return self.repository.update(idpaciente, paciente_existente)
        return None

    def eliminar_paciente(self, idpaciente: str) -> bool:
        return self.repository.delete(idpaciente)