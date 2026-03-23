from fastapi import FastAPI
from infrastructure.api import router as clientes_router

app = FastAPI(title="MS Clientes - Conexión Workbench")

app.include_router(clientes_router)

if __name__ == "__main__":
    import uvicorn
    # Puerto 8001 para que el MS_Pedidos sepa dónde buscar
    uvicorn.run(app, host="127.0.0.1", port=8001)