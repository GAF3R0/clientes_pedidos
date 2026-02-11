from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Doctor(BaseModel):
    iddoc: str 
    namedoc: str
    especialidad: str
    status: UserStatus = UserStatus.ACTIVE
    created_at: datetime = Field(default_factory=datetime.now)

    def active(self):
        self.status = UserStatus.ACTIVE

    def deactive(self):
        self.status = UserStatus.INACTIVE

    def is_active(self) -> bool:
        return self.status == UserStatus.ACTIVE