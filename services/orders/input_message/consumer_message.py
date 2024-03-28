import pika
import threading
mensaje_recibido = None
lock = threading.Lock()
def callback(channel, method, properties, body):
    global mensaje_recibido
    with lock:
        mensaje_recibido = body.decode()
        print(f"Mensaje recibido: {mensaje_recibido}")
        

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='auth', durable=False)
    channel.basic_consume(queue='auth', on_message_callback=callback, auto_ack=True)
    
    print(" [*] Esperando mensajes. Presiona CTRL+C para salir")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Proceso interrumpido. Saliendo.")
    finally:
        connection.close()

if __name__ == "__main__":
    consume_messages()
