from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProveedorBase(BaseModel):
    ruc: str = Field(..., min_length=8, max_length=20, description="Identificacion fiscal unica")
    razon_social: str = Field(..., min_length=3, max_length=150, description="Nombre comercial o legal")
    telefono: Optional[str] = Field(None, max_length=20, description="Telefono de contacto")
    activo: Optional[bool] = Field(True, description="Estado del proveedor")

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorResponse(ProveedorBase):
    id_proveedor: int
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True