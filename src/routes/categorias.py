from fastapi import APIRouter, Query, status,Depends
from typing import List
from src.schemas.categoria_schema import CategoriaCreate, CategoriaResponse
from src.services.categoria_service import CategoriaService
from src.routes.usuarios import obtener_usuario_actual

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"],
    dependencies=[Depends(obtener_usuario_actual)]
)

@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: CategoriaCreate):
    return CategoriaService.crear_categoria(categoria)

@router.get("/", response_model=List[CategoriaResponse])
def listar_categorias(solo_activos: bool = Query(default=True, description="Filtrar solo categorías activas")):
    if solo_activos:
        return CategoriaService.obtener_categorias_activos()
    return CategoriaService.obtener_categorias_general()

@router.delete("/{id_categoria}")
def desactivar_categoria(id_categoria: int):
    return CategoriaService.desactivar_categoria(id_categoria)