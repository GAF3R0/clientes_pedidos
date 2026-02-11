from abc import ABC, abstractmethod
from typing import Optional
from examentaller4.Doctor.domain.doctor import Doctor

class PacienteRepository(ABC):
    @abstractmethod
    def save(self, Doctor: Doctor) -> Doctor:
        pass

    @abstractmethod
    def get_by_id(self, iddoc: str) -> Optional[Doctor]:
        pass

    @abstractmethod
    def update(self, iddoc: str, Doctor: Doctor) -> Optional[Doctor]:
        pass

    @abstractmethod
    def delete(self, iddoc: str) -> bool:
        pass