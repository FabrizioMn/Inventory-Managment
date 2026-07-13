from fastapi import APIRouter, status , Depends , HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from src.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, TokenResponse
from src.services.usuario_service import UsuarioService
from src.config.security import verificar_token

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

security_bearer= HTTPBearer()

def obtener_usuario_actual(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)):
    token = credentials.credentials
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )
    return payload

@router.post("/login", response_model=TokenResponse)
def login(usuario: UsuarioCreate):
    return UsuarioService.autenticar_usuario(usuario)

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(usuario_actual:dict = Depends(obtener_usuario_actual)):
    return UsuarioService.obtener_usuarios()