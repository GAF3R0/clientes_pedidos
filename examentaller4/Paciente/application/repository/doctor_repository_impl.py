from typing import Optional
from examentaller4.Doctor.domain.doctor import Doctor
from examentaller4.Doctor.application.ports.doctor_repository import DoctorRepository


class InMemoryDoctorRepository(DoctorRepository):
    def __init__(self):
        self._doctors = {}

    def save(self, Doctor: Doctor) -> Doctor:
        self._doctors[Doctor.iddoc] = Doctor
        return Doctor

    def get_by_id(self, iddoc: str) -> Optional[Doctor]:
        return self._doctors.get(iddoc)

    def update(self, iddoc: str, Doctor: Doctor) -> Optional[Doctor]:
        if iddoc in self._doctors:
            self._doctors[iddoc] = Doctors
            return Doctor
        return None

    def delete(self, iddoc: str) -> bool:
        if iddoc in self._doctors:
            del self._doctors[iddoc]
            return True
        return False