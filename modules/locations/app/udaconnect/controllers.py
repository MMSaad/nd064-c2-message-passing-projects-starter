from datetime import datetime

from app.udaconnect.models import  Location
from app.udaconnect.schemas import (
    LocationSchema
)
from app.udaconnect.services import  LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect Locations", description="Connections via geolocation.")  # noqa




@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location