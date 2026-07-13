from src.config.database import supabase
from src.schemas.usuario_schema import UsuarioCreate
from fastapi import HTTPException, status
from src.config.security import (
    crear_token_acceso,
    obtener_password_hash,
    verificar_password
)

class UsuarioService:

    @staticmethod
    def crear_usuario(usuario: UsuarioCreate):
        user_existente = supabase.table("usuario").select("id_usuario").eq("email", usuario.email).execute()
        if user_existente.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El email '{usuario.email}' ya existe"
            )

        password_hasheada= obtener_password_hash(usuario.password)
        
        data = {"email":usuario.email,"password":password_hasheada}
        response = supabase.table("usuario").insert(data).execute()

        if not response.data:
            raise HTTPException(status_code=400, detail="No se pudo registrar el usuario")

        return response.data[0]

    @staticmethod
    def obtener_usuarios():
        response = supabase.table("usuario").select("id_usuario", "email", "created_at").execute()
        return response.data
    
    @staticmethod
    def autenticar_usuario(usuario_login: UsuarioCreate):
        user_bd = (
            supabase.table("usuario")
            .select("*")
            .eq("email", usuario_login.email)
            .execute()
        )

        if not user_bd.data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas",
            )

        usuario = user_bd.data[0]

        if not verificar_password(usuario_login.password, usuario["password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas",
            )

        token_data = {"sub": str(usuario["id_usuario"]), "email": usuario["email"]}
        token = crear_token_acceso(token_data)

        return {
            "access_token": token,
            "token_type": "bearer",
            "usuario": {
                "id_usuario": usuario["id_usuario"],
                "email": usuario["email"],
                "created_at": usuario["created_at"],
            },
        }