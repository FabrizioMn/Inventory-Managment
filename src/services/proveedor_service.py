from src.config.database import supabase
from src.schemas.proveedor_schema import ProveedorCreate
from fastapi import HTTPException, status

class ProveedorService:

    @staticmethod
    def crear_proveedor(proveedor: ProveedorCreate):
        ruc_existente = supabase.table("proveedor").select("id_proveedor").eq("ruc", proveedor.ruc).execute()
        if ruc_existente.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El proveedor con RUC '{proveedor.ruc}' ya se encuentra registrado"
            )

        data = proveedor.model_dump()
        response = supabase.table("proveedor").insert(data).execute()

        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo registrar el proveedor")

        return response.data[0]

    @staticmethod
    def obtener_proveedores():
        response = supabase.table("proveedor").select("*").execute()
        return response.data

    @staticmethod
    def obtener_proveedor_por_id(id_proveedor: int):
        response = supabase.table("proveedor").select("*").eq("id_proveedor", id_proveedor).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Proveedor no encontrado")
        return response.data[0]