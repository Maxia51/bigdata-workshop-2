# from kafka import KafkaProducer
# from kafka.errors import KafkaError

# producer = KafkaProducer(security_protocol="PLAINTEXT",bootstrap_servers=['localhost:9092'], api_version = (0,10,2,0), request_timeout_ms=5000)

# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)
#     print("success")

# def on_send_error(excp):
#     print ("error")
#     print (excp)

#     print ('I am an errback', exc_info=excp)
#     # handle exception

# for _ in range(100):
#     producer.send('test', b'some_message_bytes').add_callback(on_send_success).add_errback(on_send_error)
# producer.flush()


# Other Lib

from pykafka import KafkaClient

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics['test']
with topic.get_sync_producer() as producer:
    for i in range(25):

        string = "message : " + str(i)

        producer.produce(string.encode())
