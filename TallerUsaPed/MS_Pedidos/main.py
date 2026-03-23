# --- MS_Pedidos/main.py ---
import sys
import os
from fastapi import FastAPI

# 1. Configurar rutas primero
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Importar infraestructura DESPUÉS de configurar rutas
from infrastructure.adapters import Base, engine 
from infrastructure.api import router as pedidos_router

# 3. Forzar la creación de tablas
print("Iniciando conexión con PostgreSQL en Windows...")
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas verificadas/creadas con éxito en db_pedidos.")
except Exception as e:
    print(f"❌ Error al conectar con Postgres: {e}")

app = FastAPI(title="MS Pedidos - Hexagonal")
app.include_router(pedidos_router)

@app.get("/")
async def root():
    return {"message": "Microservicio de Pedidos Operativo (8002)"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)