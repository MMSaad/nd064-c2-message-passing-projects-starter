import json
from kafka import KafkaConsumer
from services import LocationService


TOPIC_NAME = 'locations'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)
    print(message.value)
    x = message.value.decode('utf-8')
    print(x)
    location = json.loads(x)
    print(location)
    print(location['id'])
    LocationService.create(location.get_json())