from fastapi import APIRouter, HTTPException
from microservicio_pacientes.domain.paciente import Paciente, PacienteCreate, PacienteUpdate
from microservicio_pacientes.infrastructure.adapters.memory_paciente_repo import InMemoryPacienteRepository

router = APIRouter()
repo = InMemoryPacienteRepository()

@router.post("/pacientes/", response_model=Paciente)
def crear_paciente(paciente_in: PacienteCreate):
    nuevo_id = 1
    if repo.db:
        nuevo_id = max(p.id_paciente for p in repo.db) + 1
        
    nuevo_paciente = Paciente(id_paciente=nuevo_id, **paciente_in.model_dump())
    return repo.save(nuevo_paciente)

@router.get("/pacientes/{id_paciente}", response_model=Paciente)
def obtener_paciente(id_paciente: int):
    paciente = repo.get_by_id(id_paciente)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/pacientes/{id_paciente}", response_model=Paciente)
def actualizar_paciente(id_paciente: int, datos: PacienteUpdate):
    paciente_existente = repo.get_by_id(id_paciente)
    if not paciente_existente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    datos_actualizados = paciente_existente.model_copy(update=datos.model_dump(exclude_unset=True))
    return repo.update(datos_actualizados)

@router.delete("/pacientes/{id_paciente}")
def eliminar_paciente(id_paciente: int):
    if not repo.delete(id_paciente):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"mensaje": "Paciente eliminado correctamente"}