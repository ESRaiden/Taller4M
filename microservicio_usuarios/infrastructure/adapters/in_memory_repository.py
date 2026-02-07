from typing import List, Optional
from microservicio_usuarios.domain.usuario import Usuario
from microservicio_usuarios.application.ports.usuario_repository import UsuarioRepository

class InMemoryUsuarioRepository(UsuarioRepository):
    def __init__(self):
        self.db: List[Usuario] = []

    def save(self, usuario: Usuario) -> Usuario:
        self.db.append(usuario)
        return usuario

    def get_by_id(self, idusuario: int) -> Optional[Usuario]:
        return next((u for u in self.db if u.idusuario == idusuario), None)

    def update(self, usuario: Usuario) -> Optional[Usuario]:
        idx = next((i for i, u in enumerate(self.db) if u.idusuario == usuario.idusuario), -1)
        if idx != -1:
            self.db[idx] = usuario
            return usuario
        return None

    def delete(self, idusuario: int) -> bool:
        idx = next((i for i, u in enumerate(self.db) if u.idusuario == idusuario), -1)
        if idx != -1:
            self.db.pop(idx)
            return True
        return False