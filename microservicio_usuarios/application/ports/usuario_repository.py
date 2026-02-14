from abc import ABC, abstractmethod
from typing import Optional
from microservicio_usuarios.domain.usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def save(self, usuario: Usuario) -> Usuario: pass
    
    @abstractmethod
    def get_by_id(self, idusuario: int) -> Optional[Usuario]: pass
    
    @abstractmethod
    def update(self, usuario: Usuario) -> Optional[Usuario]: pass
    
    @abstractmethod
    def delete(self, idusuario: int) -> bool: pass