from typing import List, Optional
from microservicio_pacientes.domain.paciente import Paciente
from microservicio_pacientes.application.ports.paciente_repository import PacienteRepository

class InMemoryPacienteRepository(PacienteRepository):
    def __init__(self):
        self.db: List[Paciente] = []

    def save(self, paciente: Paciente) -> Paciente:
        self.db.append(paciente)
        return paciente

    def get_by_id(self, id_paciente: int) -> Optional[Paciente]:
        return next((p for p in self.db if p.id_paciente == id_paciente), None)

    def update(self, paciente: Paciente) -> Optional[Paciente]:
        idx = next((i for i, p in enumerate(self.db) if p.id_paciente == paciente.id_paciente), -1)
        if idx != -1:
            self.db[idx] = paciente
            return paciente
        return None

    def delete(self, id_paciente: int) -> bool:
        idx = next((i for i, p in enumerate(self.db) if p.id_paciente == id_paciente), -1)
        if idx != -1:
            self.db.pop(idx)
            return True
        return False