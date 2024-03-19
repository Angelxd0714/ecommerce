import pika



def callback(ch=None,method=None,properties=None,body=None):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='messaje')
    channel.basic_publish(exchange='', routing_key='auth', body=body)
    connection.close()
