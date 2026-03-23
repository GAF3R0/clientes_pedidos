import sys
import os
from fastapi import FastAPI
# Importamos Base y engine de tus adaptadores para crear las tablas
from infrastructure.adapters import Base, engine 
from infrastructure.api import router as pedidos_router

# --- CONFIGURACIÓN DE RUTAS ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# ------------------------------

# --- CREACIÓN AUTOMÁTICA DE TABLAS ---
# Esto revisa tu Postgres en Windows y crea la tabla 'pedidos' si no existe
Base.metadata.create_all(bind=engine)
# -------------------------------------

app = FastAPI(title="MS Pedidos - Hexagonal")
app.include_router(pedidos_router)

@app.get("/")
async def root():
    return {"message": "Microservicio de Pedidos Operativo (8002)"}

if __name__ == "__main__":
    import uvicorn
    # Escuchamos en 0.0.0.0 para que sea visible desde fuera de WSL si es necesario
    uvicorn.run(app, host="0.0.0.0", port=8002)