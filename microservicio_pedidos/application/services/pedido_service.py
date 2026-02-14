from typing import Optional
from microservicio_pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from microservicio_pedidos.application.ports.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def crear_pedido(self, pedido_in: PedidoCreate) -> Pedido:
        nuevo_id = 1
        # Acceder a la DB en memoria
        if hasattr(self.repository, 'db') and self.repository.db:
            nuevo_id = max(p.id_pedido for p in self.repository.db) + 1
        
        nuevo_pedido = Pedido(id_pedido=nuevo_id, **pedido_in.model_dump())
        return self.repository.save(nuevo_pedido)

    def consultar_pedido(self, id_pedido: int) -> Optional[Pedido]:
        return self.repository.get_by_id(id_pedido)

    def actualizar_pedido(self, id_pedido: int, datos: PedidoUpdate) -> Optional[Pedido]:
        pedido_existente = self.repository.get_by_id(id_pedido)
        if not pedido_existente:
            return None
        
        pedido_actualizado = pedido_existente.model_copy(update=datos.model_dump(exclude_unset=True))
        return self.repository.update(pedido_actualizado)

    def eliminar_pedido(self, id_pedido: int) -> bool:
        return self.repository.delete(id_pedido)