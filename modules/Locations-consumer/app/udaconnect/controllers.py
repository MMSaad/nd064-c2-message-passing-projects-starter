from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.services import ConnectionService, LocationService, PersonService
from flask_restx import Namespace

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect Locations", description="Connections via geolocation.")  # noqa

def saveLocation(location) -> Location:
    result = LocationService.create(location)
    return result

