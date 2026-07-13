from src.config.database import supabase
from src.schemas.categoria_schema import CategoriaCreate
from fastapi import HTTPException

class CategoriaService:

    @staticmethod
    def crear_categoria(categoria: CategoriaCreate):
        data = categoria.model_dump()
        data["activo"] = True
        response = supabase.table("categoria").insert(data).execute()
        
        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo crear la categoría")
            
        return response.data[0]

    @staticmethod
    def obtener_categorias_activos():
        response = supabase.table("categoria").select("*").eq("activo", True).order("id_categoria").execute()
        return response.data

    @staticmethod
    def obtener_categorias_general():
        response = supabase.table("categoria").select("*").order("id_categoria").execute()
        return response.data

    @staticmethod
    def desactivar_categoria(id_categoria: int):
        response = supabase.table("categoria").update({"activo": False}).eq("id_categoria", id_categoria).execute()
        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo desactivar la categoría")
        return {"message": f"Categoría con ID {id_categoria} desactivada exitosamente"}