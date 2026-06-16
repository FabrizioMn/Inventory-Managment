from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

#------- Detalle de Venta -------
class DetalleVentaBase(BaseModel):
    producto_id: int = Field(..., description="ID del producto")
    cantidad: int = Field(..., gt=0, description="Cantidad vendida")
    precio_unitario: float = Field(..., gt=0, description="Precio de venta")

class DetalleVentaCreate(DetalleVentaBase):
    pass  

class DetalleVentaResponse(DetalleVentaBase):
    id_detalle_venta: int
    venta_id: int

    class Config:
        from_attributes = True

#------- Venta -------
class VentaBase(BaseModel):
    usuario_id: int = Field(..., description="ID del usuario que realiza la venta")

class VentaCreate(VentaBase):
    productos: List[DetalleVentaCreate] = Field(..., min_items=1, description="Lista de productos")

class VentaResponse(VentaBase):
    id_venta: int
    total: float
    created_at: datetime
    productos: List[DetalleVentaResponse] = []

    class Config:
        from_attributes = True