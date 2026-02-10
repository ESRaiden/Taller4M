from abc import ABC, abstractmethod
from typing import Optional
from microservicio_doctores.domain.doctor import Doctor

class DoctorRepository(ABC):
    @abstractmethod
    def save(self, doctor: Doctor) -> Doctor: pass
    
    @abstractmethod
    def get_by_id(self, id_doctor: int) -> Optional[Doctor]: pass
    
    @abstractmethod
    def update(self, doctor: Doctor) -> Optional[Doctor]: pass
    
    @abstractmethod
    def delete(self, id_doctor: int) -> bool: pass