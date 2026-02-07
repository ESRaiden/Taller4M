from abc import ABC, abstractmethod
from typing import Optional, List
# Import absoluto para evitar errores
from microservicio_pedidos.domain.pedido import Pedido

class PedidoRepository(ABC):
    @abstractmethod
    def save(self, pedido: Pedido) -> Pedido: pass

    @abstractmethod
    def get_by_id(self, id_pedido: int) -> Optional[Pedido]: pass

    @abstractmethod
    def update(self, pedido: Pedido) -> Optional[Pedido]: pass

    @abstractmethod
    def delete(self, id_pedido: int) -> bool: pass