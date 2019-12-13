from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")

topic = client.topics['test']

consumer = topic.get_simple_consumer()

for message in consumer:
    if message is not None:
        print (message.offset, message.value)