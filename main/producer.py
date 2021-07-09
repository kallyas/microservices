import pika, json

params = pika.URLParameters('amqps://trqbpooo:AauGtuEno6qeHfjJqC6CsA_Trk3_mOLW@snake.rmq2.cloudamqp.com/trqbpooo')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)