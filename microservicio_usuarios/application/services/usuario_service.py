from typing import Optional
from microservicio_usuarios.domain.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from microservicio_usuarios.application.ports.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def crear_usuario(self, usuario_in: UsuarioCreate) -> Usuario:
        # Lógica para calcular el nuevo ID
        nuevo_id = 1
        # Accedemos a la DB simulada del repositorio si existe
        if hasattr(self.repository, 'db') and self.repository.db:
            nuevo_id = max(u.idusuario for u in self.repository.db) + 1
            
        nuevo_usuario = Usuario(idusuario=nuevo_id, **usuario_in.model_dump())
        return self.repository.save(nuevo_usuario)

    def obtener_usuario(self, idusuario: int) -> Optional[Usuario]:
        return self.repository.get_by_id(idusuario)

    def actualizar_usuario(self, idusuario: int, datos: UsuarioUpdate) -> Optional[Usuario]:
        usuario_existente = self.repository.get_by_id(idusuario)
        if not usuario_existente:
            return None
        
        datos_actualizados = usuario_existente.model_copy(update=datos.model_dump(exclude_unset=True))
        return self.repository.update(datos_actualizados)

    def eliminar_usuario(self, idusuario: int) -> bool:
        return self.repository.delete(idusuario)