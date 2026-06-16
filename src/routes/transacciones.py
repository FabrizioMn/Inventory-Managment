from fastapi import APIRouter, status
from typing import List
from src.schemas.abastecimiento_schema import AbastecimientoCreate, AbastecimientoResponse
from src.schemas.venta_schema import VentaCreate,VentaResponse
from src.services.inventario_service import InventarioService

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones Inventario"]
)

@router.post("/abastecer", response_model=AbastecimientoResponse, status_code=status.HTTP_201_CREATED)
def registrar_abastecimiento(abastecimiento: AbastecimientoCreate):
    return InventarioService.registrar_abastecimiento(abastecimiento)

@router.get("/historial-abastecimientos", response_model=List[AbastecimientoResponse])
def ver_historial_abastecimientos():
    return InventarioService.obtener_historial_abastecimientos()

@router.post("/venta",response_model=VentaResponse , status_code=status.HTTP_201_CREATED)
def registrar_venta(venta:VentaCreate):
    return InventarioService.registrar_venta(venta)

@router.get("/historial-ventas",response_model=List[VentaResponse])
def ver_historial_ventas():
    return InventarioService.obtener_historial_ventas()