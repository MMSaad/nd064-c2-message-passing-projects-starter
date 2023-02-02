# Configure Kafka Connection

# Create GRPC Contracts and endpoint

# Save Create Location to Kafka Topic

from kafka import KafkaProducer


TOPIC_NAME = 'locations'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!!')
producer.send(TOPIC_NAME, b'Sample goes here')
producer.flush()
