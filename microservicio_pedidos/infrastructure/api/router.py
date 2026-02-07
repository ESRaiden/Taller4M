from fastapi import APIRouter, HTTPException
from microservicio_pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from microservicio_pedidos.infrastructure.adapters.memory_pedido_repo import InMemoryPedidoRepository

router = APIRouter()
repo = InMemoryPedidoRepository()

@router.post("/pedidos/", response_model=Pedido)
def crear_pedido(pedido_in: PedidoCreate):
    nuevo_id = 1
    if repo.db:
        nuevo_id = max(p.id_pedido for p in repo.db) + 1
    
    nuevo_pedido = Pedido(id_pedido=nuevo_id, **pedido_in.model_dump())
    return repo.save(nuevo_pedido)

@router.get("/pedidos/{id_pedido}", response_model=Pedido)
def consultar_pedido(id_pedido: int):
    pedido = repo.get_by_id(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.put("/pedidos/{id_pedido}", response_model=Pedido)
def actualizar_pedido(id_pedido: int, datos: PedidoUpdate):
    pedido_existente = repo.get_by_id(id_pedido)
    if not pedido_existente:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    pedido_actualizado = pedido_existente.model_copy(update=datos.model_dump(exclude_unset=True))
    return repo.update(pedido_actualizado)

@router.delete("/pedidos/{id_pedido}")
def eliminar_pedido(id_pedido: int):
    if not repo.delete(id_pedido):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"mensaje": "Pedido eliminado correctamente"}