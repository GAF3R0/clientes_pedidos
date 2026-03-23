from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.ports import ClienteRepository
from core.entities import Cliente as ClienteEntity


DATABASE_URL = "mysql+pymysql://root:28112005@172.29.112.1:3306/db_clientes"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ClienteTabla(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100))


class MySQLRepository(ClienteRepository):
    def get_by_id(self, cliente_id: int):
        db = SessionLocal()
        try:
            db_cliente = db.query(ClienteTabla).filter(ClienteTabla.id == cliente_id).first()
            if db_cliente:
                return ClienteEntity(id=db_cliente.id, nombre=db_cliente.nombre, email=db_cliente.email)
            return None
        finally:
            db.close()

    def save(self, cliente: ClienteEntity):
        db = SessionLocal()
        try:
            nuevo_db_cliente = ClienteTabla(
                id=cliente.id, 
                nombre=cliente.nombre, 
                email=cliente.email
            )
            db.add(nuevo_db_cliente)
            db.commit()
            db.refresh(nuevo_db_cliente)
            return cliente
        finally:
            db.close()