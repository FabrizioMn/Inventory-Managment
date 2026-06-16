from src.config.database import supabase
from src.schemas.usuario_schema import UsuarioCreate
from fastapi import HTTPException, status

class UsuarioService:

    @staticmethod
    def crear_usuario(usuario: UsuarioCreate):
        user_existente = supabase.table("usuario").select("id_usuario").eq("email", usuario.email).execute()
        if user_existente.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El email '{usuario.email}' ya existe"
            )

        data = usuario.model_dump()
        response = supabase.table("usuario").insert(data).execute()

        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo registrar el usuario")

        return response.data[0]

    @staticmethod
    def obtener_usuarios():
        response = supabase.table("usuario").select("id_usuario", "email", "created_at").execute()
        return response.data