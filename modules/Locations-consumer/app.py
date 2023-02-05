import json
from kafka import KafkaConsumer
from services import LocationService
from config import config_by_name
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(config_by_name["test"])
db.init_app(app)

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