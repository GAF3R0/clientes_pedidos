from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI
import uvicorn
from TallerUsaPed.Pedidos.application.services.pedido_service import PedidoService
from TallerUsaPed.Pedidos.infrastructure.repository.pedido_repository_impl import InMemoryPedidoRepository

app = FastAPI(title="Microservicio Pedidos - Erick Gamaliel Fuentes Rodriguez")

# Inyección de dependencias
repo = InMemoryPedidoRepository()
service = PedidoService(repo)

@app.post("/pedidos/", status_code=201)
def registrar_pedido(idpedido: str, idusuario: str, total: float):
    return service.crear_pedido(idpedido, idusuario, total)

@app.get("/pedidos/")
def obtener_pedidos():
    return service.listar_pedidos()

if __name__ == "__main__":
    # REQUISITO: Puerto 8002
    uvicorn.run(app, host="0.0.0.0", port=8002)