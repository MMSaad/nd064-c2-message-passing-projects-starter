System now it spliced into 5 microservices
## 1. Frontend 
As it's was separated from API

## 2. Locations API
Move to it's own micro-service since it's not depend on other micro-services and that's allow to scale up and down from other micro-service
## 3. Persons API
Move to it's own micro-service since it's not depend on other microservices and that's allow to scale up and down from other micro-services

## 4. Locations Updates Ingested (Locations Producer)
separated GRPC service for receiving locations updates - from persons or other integrated systems - and push it to Kafka for further processing,
This we we separated receiving location update from processing it and it's can cancel independent from other microservices

## 5. Locations Updates Processor (Locations Consumer)
That's a patch job working in background with no interaction from users or systems, which pulling Kafka locations updates and process it and store it in database


