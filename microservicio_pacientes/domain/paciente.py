from pydantic import BaseModel, EmailStr
from typing import Optional

class Paciente(BaseModel):
    id_paciente: int
    nombre: str
    email: EmailStr

class PacienteCreate(BaseModel):
    nombre: str
    email: EmailStr

class PacienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None