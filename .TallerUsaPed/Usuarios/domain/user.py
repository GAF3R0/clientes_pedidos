from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class User(BaseModel):
    # Entidad de dominio: User
    # Usamos idusuario para coincidir con tu esquema inicial
    idusuario: str 
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
    created_at: datetime = Field(default_factory=datetime.now)

    # Comportamientos del dominio (ahora dentro de la clase)
    def active(self):
        self.status = UserStatus.ACTIVE

    def deactive(self):
        self.status = UserStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == UserStatus.ACTIVE