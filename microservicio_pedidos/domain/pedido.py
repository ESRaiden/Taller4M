from pydantic import BaseModel
from typing import Optional, List

# Definición del modelo de datos
class Pedido(BaseModel):
    id_pedido: int
    detalle_pedido: str  # Ej: "2 Hamburguesas y 1 Refresco"
    total: float

# Modelo para crear (sin ID, el ID lo genera el sistema)
class PedidoCreate(BaseModel):
    detalle_pedido: str
    total: float

# Modelo para actualizar (todos opcionales)
class PedidoUpdate(BaseModel):
    detalle_pedido: Optional[str] = None
    total: Optional[float] = None