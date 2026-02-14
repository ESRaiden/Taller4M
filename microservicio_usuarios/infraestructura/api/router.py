from fastapi import APIRouter, HTTPException
from microservicio_usuarios.domain.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from microservicio_usuarios.infraestructura.adapters.in_memory_repository import InMemoryUsuarioRepository
from microservicio_usuarios.application.services.usuario_service import UsuarioService

router = APIRouter()

# Inyección de dependencias
repo = InMemoryUsuarioRepository()
service = UsuarioService(repo)

@router.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario_in: UsuarioCreate):
    return service.crear_usuario(usuario_in)

@router.get("/usuarios/{idusuario}", response_model=Usuario)
def obtener_usuario(idusuario: int):
    usuario = service.obtener_usuario(idusuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/usuarios/{idusuario}", response_model=Usuario)
def actualizar_usuario(idusuario: int, datos: UsuarioUpdate):
    usuario = service.actualizar_usuario(idusuario, datos)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/usuarios/{idusuario}")
def eliminar_usuario(idusuario: int):
    if not service.eliminar_usuario(idusuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}