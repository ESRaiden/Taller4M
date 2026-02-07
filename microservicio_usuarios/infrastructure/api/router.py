from fastapi import APIRouter, HTTPException
from microservicio_usuarios.domain.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from microservicio_usuarios.infrastructure.adapters.in_memory_repository import InMemoryUsuarioRepository

router = APIRouter()
repo = InMemoryUsuarioRepository() # Instancia de la BD en memoria

@router.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario_in: UsuarioCreate):
    # Lógica simple para generar ID automático
    nuevo_id = 1
    if repo.db:
        nuevo_id = max(u.idusuario for u in repo.db) + 1
        
    nuevo_usuario = Usuario(idusuario=nuevo_id, **usuario_in.model_dump())
    return repo.save(nuevo_usuario)

@router.get("/usuarios/{idusuario}", response_model=Usuario)
def obtener_usuario(idusuario: int):
    usuario = repo.get_by_id(idusuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/usuarios/{idusuario}", response_model=Usuario)
def actualizar_usuario(idusuario: int, datos: UsuarioUpdate):
    usuario_existente = repo.get_by_id(idusuario)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Actualizamos solo los campos enviados
    datos_actualizados = usuario_existente.model_copy(update=datos.model_dump(exclude_unset=True))
    return repo.update(datos_actualizados)

@router.delete("/usuarios/{idusuario}")
def eliminar_usuario(idusuario: int):
    if not repo.delete(idusuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}