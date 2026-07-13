from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductoBase(BaseModel):
    sku: str = Field(..., min_length=3, max_length=50, description="Código unico de inventario")
    nombre: str = Field(..., min_length=2, max_length=150, description="Nombre del producto")
    descripcion: Optional[str] = Field(None, description="Detalles del producto")
    precio: float = Field(..., gt=0, description="Precio de venta al público")
    id_categoria: Optional[int] = Field(None, description="ID de la categoría a la que pertenece")
    activo: Optional[bool] = Field(True, description="Estado del producto para Soft Delete")

class ProductoCreate(ProductoBase):
    stock: Optional[int] = Field(0, ge=0)

class ProductoUpdate(BaseModel):
    sku: Optional[str] = Field(None, min_length=3, max_length=50)
    nombre: Optional[str] = Field(None, min_length=2, max_length=150)
    descripcion: Optional[str] = None
    precio: Optional[float] = Field(None, gt=0)
    id_categoria: Optional[int] = None
    activo: Optional[bool] = None

class ProductoResponse(ProductoBase):
    id_producto: int
    stock: int
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True