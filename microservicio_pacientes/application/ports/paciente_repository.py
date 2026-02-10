from abc import ABC, abstractmethod
from typing import Optional
from microservicio_pacientes.domain.paciente import Paciente

class PacienteRepository(ABC):
    @abstractmethod
    def save(self, paciente: Paciente) -> Paciente: pass
    
    @abstractmethod
    def get_by_id(self, id_paciente: int) -> Optional[Paciente]: pass
    
    @abstractmethod
    def update(self, paciente: Paciente) -> Optional[Paciente]: pass
    
    @abstractmethod
    def delete(self, id_paciente: int) -> bool: pass