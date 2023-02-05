import json
import os
from kafka import KafkaConsumer
from services import LocationService


TOPIC_NAME = 'locations'
KAFKA_SERVER = '10.43.136.92:9092'
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
print("Start listening")
for message in consumer:
    try:
        print(message)
        print(message.value)
        x = message.value.decode('utf-8')
        print(x)
        location = json.loads(x)
        LocationService.create(location)
    except Exception as e:
        print("Some error happened " + str(e))