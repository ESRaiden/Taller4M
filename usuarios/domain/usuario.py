from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

# 1. Definimos los estados posibles del usuario
class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

# 2. El modelo principal de Usuario con lógica de negocio
class User(BaseModel):
    """Entidad de dominio: User"""
    id: int  # En la foto dice str, pero int es más fácil para pruebas rápidas. Úsalo según tu BD.
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
    created_at: datetime

    # Comportamientos de dominio (Métodos)
    def activate(self):
        """Comportamiento de dominio"""
        self.status = UserStatus.ACTIVE

    def deactivate(self):
        """Comportamiento de dominio"""
        self.status = UserStatus.INACTIVE

    def is_active(self) -> bool:
        """Comportamiento de dominio"""
        return self.status == UserStatus.ACTIVE

# 3. Los DTOs (Data Transfer Objects)
class UserCreate(BaseModel):
    """DTO para crear usuario"""
    username: str
    email: str

class UserUpdate(BaseModel):
    """DTO para actualizar usuario"""
    username: Optional[str] = None
    email: Optional[str] = None
    status: Optional[UserStatus] = None 