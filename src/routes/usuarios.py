from fastapi import APIRouter, status
from typing import List
from src.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from src.services.usuario_service import UsuarioService

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: UsuarioCreate):
    return UsuarioService.crear_usuario(usuario)

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios():
    return UsuarioService.obtener_usuarios()