from pydantic import BaseModel, Field
from datetime import datetime

class UsuarioBase(BaseModel):
    email: str = Field(..., min_length=3, max_length=100, description="Email para loguearse")

class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=6, description="Contraseña de acceso (mínimo 6 caracteres)")

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    created_at: datetime

    class Config:
        from_attributes = True
        
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    usuario: UsuarioResponse