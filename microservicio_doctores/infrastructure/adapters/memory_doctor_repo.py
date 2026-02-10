from typing import List, Optional
from microservicio_doctores.domain.doctor import Doctor
from microservicio_doctores.application.ports.doctor_repository import DoctorRepository

class InMemoryDoctorRepository(DoctorRepository):
    def __init__(self):
        self.db: List[Doctor] = []

    def save(self, doctor: Doctor) -> Doctor:
        self.db.append(doctor)
        return doctor

    def get_by_id(self, id_doctor: int) -> Optional[Doctor]:
        return next((d for d in self.db if d.id_doctor == id_doctor), None)

    def update(self, doctor: Doctor) -> Optional[Doctor]:
        idx = next((i for i, d in enumerate(self.db) if d.id_doctor == doctor.id_doctor), -1)
        if idx != -1:
            self.db[idx] = doctor
            return doctor
        return None

    def delete(self, id_doctor: int) -> bool:
        idx = next((i for i, d in enumerate(self.db) if d.id_doctor == id_doctor), -1)
        if idx != -1:
            self.db.pop(idx)
            return True
        return False