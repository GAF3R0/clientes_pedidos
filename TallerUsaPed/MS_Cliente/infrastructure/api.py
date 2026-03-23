from fastapi import APIRouter, HTTPException
from .database import MySQLRepository
from core.entities import Cliente

router = APIRouter()
repo = MySQLRepository()

@router.get("/clientes/{cliente_id}")
async def get_cliente(cliente_id: int):
    cliente = repo.get_by_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/clientes/")
async def create_cliente(cliente: Cliente):
    # Verificamos si ya existe para evitar error de PK en Workbench
    existente = repo.get_by_id(cliente.id)
    if existente:
        raise HTTPException(status_code=400, detail="El ID del cliente ya existe")
    
    return repo.save(cliente)