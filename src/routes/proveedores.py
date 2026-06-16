from fastapi import APIRouter, status
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
def listar_proveedores():
    return ProveedorService.obtener_proveedores()

@router.get("/{id_proveedor}", response_model=ProveedorResponse)
def obtener_proveedor(id_proveedor: int):
    return ProveedorService.obtener_proveedor_por_id(id_proveedor)