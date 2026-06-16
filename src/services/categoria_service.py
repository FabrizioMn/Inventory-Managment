from src.config.database import supabase
from src.schemas.categoria_schema import CategoriaCreate
from fastapi import HTTPException

class CategoriaService:

    @staticmethod
    def crear_categoria(categoria: CategoriaCreate):
        data = categoria.model_dump()
        
        response = supabase.table("categoria").insert(data).execute()
        
        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo crear la categoría")
            
        return response.data[0]

    @staticmethod
    def obtener_categorias():
        response = supabase.table("categoria").select("*").execute()
        return response.data

    @staticmethod
    def obtener_categoria_por_id(id_categoria: int):
        response = supabase.table("categoria").select("*").eq("id_categoria", id_categoria).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Categoría con ID {id_categoria} no encontrada")
            
        return response.data[0]