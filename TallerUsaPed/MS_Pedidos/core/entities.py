from dataclasses import dataclass

@dataclass
class Pedido:
    id: int
    cliente_id: int
    producto: str
    cantidad: int