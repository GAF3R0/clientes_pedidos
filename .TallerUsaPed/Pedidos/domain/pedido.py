from pydantic import BaseModel

class Pedido(BaseModel):
    idpedido: str
    idusuario: str  # Relación con el usuario (ej. 100018412)
    total: float