from pydantic import BaseModel
from typing import Optional

class Doctor(BaseModel):
    id_doctor: int
    nombre: str
    especialidad: str

class DoctorCreate(BaseModel):
    nombre: str
    especialidad: str

class DoctorUpdate(BaseModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None