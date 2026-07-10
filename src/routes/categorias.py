from fastapi import APIRouter, status
from typing import List
from src.schemas.categoria_schema import CategoriaCreate, CategoriaResponse
from src.services.categoria_service import CategoriaService

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)

@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: CategoriaCreate):
    return CategoriaService.crear_categoria(categoria)

@router.get("/", response_model=List[CategoriaResponse])
def listar_categorias():
    return CategoriaService.obtener_categorias()
