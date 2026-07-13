from fastapi import APIRouter, Query, status
from typing import List
from src.schemas.proveedor_schema import ProveedorCreate, ProveedorResponse
from src.services.proveedor_service import ProveedorService

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

@router.post("/", response_model=ProveedorResponse, status_code=status.HTTP_201_CREATED)
def crear_proveedor(proveedor: ProveedorCreate):
    return ProveedorService.crear_proveedor(proveedor)

@router.get("/", response_model=List[ProveedorResponse])
def listar_proveedores(solo_activos: bool = Query(default=True, description="Filtrar solo proveedores activos")):
    if solo_activos:
        return ProveedorService.obtener_proveedores_activos()
    return ProveedorService.obtener_proveedores_general()

@router.delete("/{id_proveedor}")
def desactivar_proveedor(id_proveedor: int):
    return ProveedorService.desactivar_proveedor(id_proveedor)