import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def send_message(message):
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2, 
        )
    )
    print(f" [x] Enviou '{message}'")

if __name__ == "__main__":
    message = "Processamento de pedido ID Esquerda 9, Direita 15, Esquerda 7 (Cofre dos S.T.A.R.S RE2 Remake)"
    send_message(message)
    connection.close()
