from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre de la categoria")
    descripcion: Optional[str] = Field(None, description="Descripcion")
    activo: Optional[bool] = Field(True, description="Estado de la categoria")

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id_categoria: int
    activo: bool
    created_at: datetime

    class Config:
        from_attributes = True