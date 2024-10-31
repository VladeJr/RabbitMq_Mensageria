import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(f" [x] Recebeu '{body.decode()}'")
    time.sleep(1) 
    print(" [x] Tarefa concluída")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print(" [*] Esperando por mensagens. Para sair pressione CTRL+C")
channel.start_consuming()
