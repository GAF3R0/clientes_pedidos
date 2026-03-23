from fastapi import APIRouter, HTTPException
from .adapters import ClienteHttpAdapter, RabbitMQAdapter, PostgresPedidoRepository
from core.use_case import CrearPedidoUseCase

router = APIRouter()

@router.post("/pedidos/")
async def post_pedido(cliente_id: int, producto: str, cantidad: int):
    try:
        cliente_service = ClienteHttpAdapter()
        publisher = RabbitMQAdapter()
        repo = PostgresPedidoRepository() 

        use_case = CrearPedidoUseCase(
            repo=repo, 
            cliente_service=cliente_service, 
            publisher=publisher
        )

        resultado = await use_case.ejecutar(cliente_id, producto, cantidad)
        
   
        if "error" in resultado:
            raise HTTPException(status_code=400, detail=resultado["error"])
            
        return resultado

    except ConnectionError as ce:
        raise HTTPException(
            status_code=503, 
            detail="Error de conexión con la Base de Datos o RabbitMQ"
        )
    except Exception as e:
        # Esto imprimirá el error en tu terminal de WSL para que lo veas
        print(f"DEBUG ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))