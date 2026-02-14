from fastapi import APIRouter, HTTPException
from microservicio_pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
# OJO: infraestructura
from microservicio_pedidos.infraestructura.adapters.memory_pedido_repo import InMemoryPedidoRepository
from microservicio_pedidos.application.services.pedido_service import PedidoService

router = APIRouter()

# Inyección de dependencias
repo = InMemoryPedidoRepository()
service = PedidoService(repo)

@router.post("/pedidos/", response_model=Pedido)
def crear_pedido(pedido_in: PedidoCreate):
    return service.crear_pedido(pedido_in)

@router.get("/pedidos/{id_pedido}", response_model=Pedido)
def consultar_pedido(id_pedido: int):
    pedido = service.consultar_pedido(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.put("/pedidos/{id_pedido}", response_model=Pedido)
def actualizar_pedido(id_pedido: int, datos: PedidoUpdate):
    pedido_actualizado = service.actualizar_pedido(id_pedido, datos)
    if not pedido_actualizado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido_actualizado

@router.delete("/pedidos/{id_pedido}")
def eliminar_pedido(id_pedido: int):
    if not service.eliminar_pedido(id_pedido):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {"mensaje": "Pedido eliminado correctamente"}