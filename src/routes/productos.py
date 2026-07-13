from fastapi import APIRouter, status, Query
from typing import List
from src.schemas.producto_schema import ProductoCreate, ProductoResponse,ProductoUpdate
from src.services.producto_service import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: ProductoCreate):
    return ProductoService.crear_producto(producto)

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(solo_activos: bool = Query(default=True, description="Filtrar solo registros activos")):
    if solo_activos:
        return ProductoService.obtener_productos_activos()
    return ProductoService.obtener_productos_general()

@router.put("/{id_producto}", status_code=status.HTTP_200_OK)
def actualizar_producto(id_producto: int, producto: ProductoUpdate):
    return ProductoService.actualizar_producto(id_producto, producto)

@router.delete("/{id_producto}")
def desactivar_producto(id_producto: int):
    return ProductoService.desactivar_producto(id_producto)