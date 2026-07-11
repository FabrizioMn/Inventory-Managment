from fastapi import APIRouter, status
from typing import List
from src.schemas.producto_schema import ProductoCreate, ProductoResponse
from src.services.producto_service import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: ProductoCreate):
    return ProductoService.crear_producto(producto)

@router.get("/", response_model=List[ProductoResponse])
def listar_productos():
    return ProductoService.obtener_productos()


@router.put("/{id_producto}", status_code=status.HTTP_200_OK)
def actualizar_producto(id_producto: int, producto: ProductoCreate):
    return ProductoService.actualizar_producto(id_producto, producto)

@router.delete("/{id_producto}", status_code=status.HTTP_200_OK)
def eliminar_producto(id_producto: int):
    return ProductoService.eliminar_producto(id_producto)