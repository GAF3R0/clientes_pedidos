import json

class CrearPedidoUseCase:
    def __init__(self, repo, cliente_service, publisher):
        """
        Inyección de dependencias (Puertos):
        :param repo: Adaptador de PostgreSQL
        :param cliente_service: Adaptador de HTTP para MS_Clientes
        :param publisher: Adaptador de RabbitMQ
        """
        self.repo = repo
        self.cliente_service = cliente_service
        self.publisher = publisher

    async def ejecutar(self, cliente_id: int, producto: str, cantidad: int):

        existe = await self.cliente_service.verificar_cliente(cliente_id)
        
        if not existe:
            return {
                "error": "Validación fallida",
                "detalle": f"El cliente con ID {cliente_id} no existe en la base de datos MySQL."
            }


        datos_pedido = {
            "cliente_id": cliente_id,
            "producto": producto,
            "cantidad": cantidad
        }
        
        try:

            nuevo_pedido = self.repo.save(datos_pedido)
        except Exception as e:
            return {
                "error": "Error de persistencia",
                "detalle": f"No se pudo guardar en PostgreSQL: {str(e)}"
            }


        evento = {
            "evento": "PEDIDO_CREADO",
            "pedido_id": nuevo_pedido.id,
            "cliente_id": cliente_id,
            "producto": producto,
            "cantidad": cantidad
        }
        

        self.publisher.publish(json.dumps(evento))


        return {
            "status": "success",
            "message": "Pedido procesado integralmente",
            "data": {
                "id_db": nuevo_pedido.id,
                "validacion_ms_cliente": "OK (MySQL)",
                "persistencia_ms_pedido": "OK (PostgreSQL)",
                "notificacion_broker": "OK (RabbitMQ)"
            }
        }