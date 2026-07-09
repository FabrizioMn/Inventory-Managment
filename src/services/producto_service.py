from src.config.database import supabase
from src.schemas.producto_schema import ProductoCreate
from fastapi import HTTPException, status

class ProductoService:

    @staticmethod
    def crear_producto(producto: ProductoCreate):
        sku_existente = supabase.table("producto").select("id_producto").eq("sku", producto.sku.strip()).execute()
        if sku_existente.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"El SKU '{producto.sku}' ya esta registrado en el sistema"
            )

        nombre_existente = supabase.table("producto").select("id_producto").ilike("nombre", producto.nombre.strip()).execute()
        if nombre_existente.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=f"Ya existe un producto registrado con el nombre '{producto.nombre}'"
            )
        
        if producto.id_categoria:
            cat_existente = supabase.table("categoria").select("id_categoria").eq("id_categoria", producto.id_categoria).execute()
            if not cat_existente.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"La categoría con ID {producto.id_categoria} no existe"
                )

        data = producto.model_dump()
        data["sku"] = data["sku"].strip()
        data["nombre"] = data["nombre"].strip()
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
    
    @staticmethod
    def eliminar_producto(id_producto: int):
        producto_existente = supabase.table("producto").select("id_producto").eq("id_producto", id_producto).execute()
        if not producto_existente.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El producto con ID {id_producto} no existe"
            )
        
        response = supabase.table("producto").delete().eq("id_producto", id_producto).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="No se pudo eliminar el producto"
            )
            
        return {"message": f"Producto con ID {id_producto} eliminado exitosamente"}