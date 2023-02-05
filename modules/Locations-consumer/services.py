import logging
from typing import Dict


from models import Location
from schemas import LocationSchema
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2.functions import ST_Point

db = SQLAlchemy()


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
        db.session.add(new_location)
        db.session.commit()

        return new_location
