import os
import sys

# Asegurar que Python encuentre la carpeta 'src'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.config.database import supabase
from src.config.security import obtener_password_hash

def crear_usuario_consola():
    print("=== SCRIPT DE CREACIÓN DE USUARIOS ADMINISTRADORES ===")
    email = input("Introduce el email del usuario: ").strip()
    password = input("Introduce la contraseña (mínimo 6 caracteres): ").strip()

    if len(password) < 6:
        print("❌ Error: La contraseña debe tener al menos 6 caracteres.")
        return

    # Verificar si el email ya existe en Supabase
    try:
        user_existente = supabase.table("usuario").select("id_usuario").eq("email", email).execute()
        if user_existente.data:
            print(f"❌ Error: El email '{email}' ya está registrado.")
            return
        
        # Hashear la contraseña usando la misma lógica del sistema
        password_hasheada = obtener_password_hash(password)

        # Insertar en la base de datos
        data = {
            "email": email,
            "password": password_hasheada
        }
        
        response = supabase.table("usuario").insert(data).execute()

        if response.data:
            print(f"\n✅ ¡Usuario creado con éxito!")
            print(f"ID: {response.data[0]['id_usuario']}")
            print(f"Email: {response.data[0]['email']}")
        else:
            print("❌ Error inesperado: No se pudo insertar el usuario.")

    except Exception as e:
        print(f"❌ Ocurrió un error al conectar con Supabase: {e}")

if __name__ == "__main__":
    crear_usuario_consola()