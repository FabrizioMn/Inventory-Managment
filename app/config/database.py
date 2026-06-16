from supabase import create_client,Client
from dotenv import load_dotenv
import os
load_dotenv()

url:str = os.getenv("SUPABASE_URL")
key:str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Error: No se encontraron las credenciales")

supabase: Client = create_client(url,key)
print("Configuracion de Supabase cargada exitosamente")
