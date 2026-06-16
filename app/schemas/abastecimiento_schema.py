from pydantic import BaseModel, Field
from datetime import datetime

class AbastecimientoBase(BaseModel):
    cantidad: int = Field(..., gt=0, description="Cantidad de productos que ingresan")
    precio_compra: float = Field(..., gt=0, description="Precio al que se compro el producto al proveedor")
    id_proveedor: int = Field(..., description="ID del proveedor")
    id_usuario: int = Field(..., description="ID del usuario")
    id_producto: int = Field(..., description="ID del producto")

class AbastecimientoCreate(AbastecimientoBase):
    pass

class AbastecimientoResponse(AbastecimientoBase):
    id_abastecimiento: int
    created_at: datetime

    class Config:
        from_attributes = True