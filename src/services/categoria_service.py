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
