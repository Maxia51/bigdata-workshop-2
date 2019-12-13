# from kafka import KafkaConsumer
# import sys

# # To consume latest messages and auto-commit offsets
# consumer = KafkaConsumer('test',
#                             group_id="group1",
#                          bootstrap_servers=['localhost:9092'], auto_offset_reset = 'earliest')


# try:
#     for message in consumer:
#         print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))

# except KeyboardInterrupt:
#     sys.exit()

# Other Lib

from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")

topic = client.topics['test']

consumer = topic.get_simple_consumer()

for message in consumer:
    if message is not None:
        print (message.offset, message.value)