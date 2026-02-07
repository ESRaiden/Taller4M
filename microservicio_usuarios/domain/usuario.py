from pydantic import BaseModel, EmailStr
from typing import Optional

class Usuario(BaseModel):
    idusuario: int
    nombre: str
    email: EmailStr

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None