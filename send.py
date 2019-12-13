from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")

topic = client.topics['TopicMoumou2']
with topic.get_sync_producer() as producer:
    for i in range(25):
        string = "message : " + str(i)
        producer.produce(string.encode())
