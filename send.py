from pykafka import KafkaClient

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics['test']
with topic.get_sync_producer() as producer:
    for i in range(25):

        string = "message : " + str(i)

        producer.produce(string.encode())
