from pydantic import BaseModel
from typing import Optional, List

class Pedido(BaseModel):
    id_pedido: int
    detalle_pedido: str  # Ej: "2 Hamburguesas y 1 Refresco"
    total: float

class PedidoCreate(BaseModel):
    detalle_pedido: str
    total: float

class PedidoUpdate(BaseModel):
    detalle_pedido: Optional[str] = None
    total: Optional[float] = None