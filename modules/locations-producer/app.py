from kafka import KafkaProducer
import time
import json
from bson import json_util
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

TOPIC_NAME = 'locations'
KAFKA_SERVER = '10.43.136.92:9092'


class ItemServicer(location_pb2_grpc.LocationServiceServicer):

    def Create(self, request, context):
        try:
            print(str(request))
            request_value = {
                "id": request.id,
                "person_id": request.person_id,
                "longitude": request.longitude,
                "latitude": request.latitude,
                "creation_time": request.creation_time
            }
            message = json.dumps(request_value)
            print(message)
            producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
            producer.send(TOPIC_NAME, json.dumps(request_value, default=json_util.default).encode('utf-8'))
            producer.flush()
            return location_pb2.LocationMessage(**request_value)
        except Exception as e:
            print("Some error happened " + str(e))


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(ItemServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
