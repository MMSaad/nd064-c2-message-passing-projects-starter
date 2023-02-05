import os
import json
from app.udaconnect.controllers import saveLocation
from kafka import KafkaConsumer

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(debug=True)

TOPIC_NAME = 'locations'
KAFKA_SERVER = '10.43.136.92:9092'
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
print("Start listening")
for message in consumer:
    try:
        print(message.value)
        location = json.loads(message.value.decode('utf-8'))
        with app.app_context():
            savedLocation = saveLocation(location)
            print(str(savedLocation))
    except Exception as e:
        print("Some error happened " + str(e))
