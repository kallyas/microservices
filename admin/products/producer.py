import pika, json

params = pika.URLParameters('amqps://ukexzcwg:skL7gAOh0AT3Ef4tx9Iipu0em9Gav-ro@kebnekaise.lmq.cloudamqp.com/ukexzcwg')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)