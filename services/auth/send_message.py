import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Crear una cola llamada 'mi_cola'
channel.queue_declare(queue='mi_cola')

# Publicar un mensaje en la cola 'mi_cola'
channel.basic_publish(exchange='',
                      routing_key='mi_cola',
                      body='Hola, RabbitMQ!')

print("Mensaje enviado")

# Cerrar la conexión
connection.close()