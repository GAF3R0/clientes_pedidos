from typing import Optional
from examentaller4.Paciente.domain.paciente import Paciente
from examentaller4.Paciente.application.ports.paciente_repository import PacienteRepository


class InMemoryPacienteRepository(PacienteRepository):
    def __init__(self):
        self._pacientes = {}

    def save(self, Paciente: Paciente) -> Paciente:
        self._pacientes[Paciente.idpaciente] = Paciente
        return Paciente

    def get_by_id(self, idpaciente: str) -> Optional[Paciente]:
        return self._pacientes.get(idpaciente)

    def update(self, idpaciente: str, Paciente: Paciente) -> Optional[Paciente]:
        if idpaciente in self._pacientes:
            self._pacientes[idpaciente] = Pacientes
            return Pacientes
        return None

    def delete(self, idpaciente: str) -> bool:
        if idpaciente in self._pacientes:
            del self._pacientes[idpaciente]
            return True
        return False