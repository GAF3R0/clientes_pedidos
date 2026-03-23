import httpx
import pika
import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.ports import PedidoRepository

# 1. CONFIGURACIÓN DE POSTGRESQL (Asegúrate de que la IP sea la de tu Windows)
PG_URL = "postgresql://postgres:contrasena@172.29.112.1:5432/db_pedidos"

engine = create_engine(PG_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- MODELO DE LA TABLA ---
class PedidoTabla(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente_id = Column(Integer, nullable=False)
    producto = Column(String(100), nullable=False) # Tipo String (VARCHAR) para evitar el error de array
    cantidad = Column(Integer, default=1)

# --- ADAPTADOR DE PERSISTENCIA (PostgreSQL) ---
class PostgresPedidoRepository(PedidoRepository):
    def save(self, pedido_data: dict):
        db = SessionLocal()
        try:
            nuevo_db_pedido = PedidoTabla(
                cliente_id=pedido_data['cliente_id'],
                producto=pedido_data['producto'],
                cantidad=pedido_data.get('cantidad', 1)
            )
            db.add(nuevo_db_pedido)
            db.commit() # Vital para que el cambio se guarde en Windows
            db.refresh(nuevo_db_pedido)
            return nuevo_db_pedido
        except Exception as e:
            db.rollback()
            print(f"Error al guardar en Postgres: {e}")
            raise e
        finally:
            db.close()

# --- ADAPTADOR DE COMUNICACIÓN (HTTP a MS_Clientes) ---
class ClienteHttpAdapter:
    async def verificar_cliente(self, cliente_id: int) -> bool:
        async with httpx.AsyncClient() as client:
            try:
                # Localhost/127.0.0.1 porque ambos MS están en el mismo WSL
                url = f"http://127.0.0.1:8001/clientes/{cliente_id}"
                response = await client.get(url, timeout=5.0)
                return response.status_code == 200
            except Exception as e:
                print(f"Error de conexión con MS_Clientes: {e}")
                return False

# --- ADAPTADOR DE MENSAJERÍA (RabbitMQ) ---
class RabbitMQAdapter:
    def __init__(self, host="172.29.112.1"):
        self.host = host

    def publish(self, message: str):
        try:
            # Conexión al RabbitMQ en Windows
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host, heartbeat=600)
            )
            channel = connection.channel()
            
            # Declaramos la cola por si no existe
            channel.queue_declare(queue='ordenes_nuevas', durable=False)
            
            # Publicamos el mensaje
            channel.basic_publish(
                exchange='',
                routing_key='ordenes_nuevas',
                body=message
            )
            connection.close()
            print(f" [x] Enviado a RabbitMQ: {message}")
        except Exception as e:
            print(f"Error al publicar en RabbitMQ: {e}")