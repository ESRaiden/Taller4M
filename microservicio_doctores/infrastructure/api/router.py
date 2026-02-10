from fastapi import APIRouter, HTTPException
from microservicio_doctores.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from microservicio_doctores.infrastructure.adapters.memory_doctor_repo import InMemoryDoctorRepository

router = APIRouter()
repo = InMemoryDoctorRepository()

@router.post("/doctores/", response_model=Doctor)
def crear_doctor(doctor_in: DoctorCreate):
    nuevo_id = 1
    if repo.db:
        nuevo_id = max(d.id_doctor for d in repo.db) + 1
        
    nuevo_doctor = Doctor(id_doctor=nuevo_id, **doctor_in.model_dump())
    return repo.save(nuevo_doctor)

@router.get("/doctores/{id_doctor}", response_model=Doctor)
def obtener_doctor(id_doctor: int):
    doctor = repo.get_by_id(id_doctor)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor

@router.put("/doctores/{id_doctor}", response_model=Doctor)
def actualizar_doctor(id_doctor: int, datos: DoctorUpdate):
    doctor_existente = repo.get_by_id(id_doctor)
    if not doctor_existente:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    
    datos_actualizados = doctor_existente.model_copy(update=datos.model_dump(exclude_unset=True))
    return repo.update(datos_actualizados)

@router.delete("/doctores/{id_doctor}")
def eliminar_doctor(id_doctor: int):
    if not repo.delete(id_doctor):
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return {"mensaje": "Doctor eliminado correctamente"}