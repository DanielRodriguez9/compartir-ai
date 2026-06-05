import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print(f" Conectando a: {url}")
print(f" Key: {key[:20]}...")

try:
    supabase = create_client(url, key)
    
    # Probar conexión con una tabla que ya existe
    result = supabase.table("personalities").select("*").execute()
    
    print(f"\n CONEXIÓN EXITOSA!")
    print(f" Personalidades encontradas: {len(result.data)}")
    
except Exception as e:
    print(f"\nError: {e}")
    
