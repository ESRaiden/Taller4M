from typing import List, Optional
# Imports absolutos
from microservicio_pedidos.domain.pedido import Pedido
from microservicio_pedidos.application.ports.pedido_repository import PedidoRepository

class InMemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        # Simulación de base de datos en memoria
        self.db: List[Pedido] = []

    def save(self, pedido: Pedido) -> Pedido:
        self.db.append(pedido)
        return pedido

    def get_by_id(self, id_pedido: int) -> Optional[Pedido]:
        # Busca el pedido por ID
        return next((p for p in self.db if p.id_pedido == id_pedido), None)

    def update(self, pedido: Pedido) -> Optional[Pedido]:
        # Busca el índice y actualiza
        idx = next((i for i, p in enumerate(self.db) if p.id_pedido == pedido.id_pedido), -1)
        if idx != -1:
            self.db[idx] = pedido
            return pedido
        return None

    def delete(self, id_pedido: int) -> bool:
        # Busca el índice y elimina
        idx = next((i for i, p in enumerate(self.db) if p.id_pedido == id_pedido), -1)
        if idx != -1:
            self.db.pop(idx)
            return True
        return False