import logging
from typing import Dict
import os

from models import Location
from schemas import LocationSchema
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.ext.declarative import declarative_base

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


engine = sqlalchemy.create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Base = declarative_base()


class LocationService:

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        session = sessionmaker(bind=engine)
        session.add(new_location)
        session.commit()

        return new_location
