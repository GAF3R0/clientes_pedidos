from abc import ABC, abstractmethod
from typing import Optional
from examentaller4.Paciente.domain.paciente import Paciente

class PacienteRepository(ABC):
    @abstractmethod
    def save(self, Paciente: Paciente) -> Paciente:
        pass

    @abstractmethod
    def get_by_id(self, idpaciente: str) -> Optional[Paciente]:
        pass

    @abstractmethod
    def update(self, idpaciente: str, Paciente: Paciente) -> Optional[Paciente]:
        pass

    @abstractmethod
    def delete(self, idpaciente: str) -> bool:
        pass