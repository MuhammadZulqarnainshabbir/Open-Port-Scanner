from flask_restful import Api
from app import app
from .ports import Ports

restServer = Api(app)
restServer.add_resource(Ports, "/api/v1.0/ports")
