from src.config.database import supabase
from src.schemas.producto_schema import ProductoCreate
from fastapi import HTTPException, status

class ProductoService:

    @staticmethod
    def crear_producto(producto: ProductoCreate):
        sku_existente = supabase.table("producto").select("id_producto").eq("sku", producto.sku).execute()
        if sku_existente.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"El SKU '{producto.sku}' ya esta registrado en el sistema"
            )
        
        if producto.id_categoria:
            cat_existente = supabase.table("categoria").select("id_categoria").eq("id_categoria", producto.id_categoria).execute()
            if not cat_existente.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"La categoría con ID {producto.id_categoria} no existe"
                )

        data = producto.model_dump()
        response = supabase.table("producto").insert(data).execute()
        
        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo registrar el producto")
            
        return response.data[0]

    @staticmethod
    def obtener_productos():
        response = supabase.table("producto").select("*").execute()
        return response.data

    @staticmethod
    def obtener_producto_por_id(id_producto: int):
        response = supabase.table("producto").select("*").eq("id_producto", id_producto).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return response.data[0]

    @staticmethod
    def obtener_producto_por_sku(sku: str):
        response = supabase.table("producto").select("*").eq("sku", sku).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"No se encontro ningun producto con el SKU {sku}")
        return response.data[0]