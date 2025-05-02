from flask import Blueprint, jsonify, request
from app.models.sensor import Sensor
from app.providers.extensions import db
import logging

api_sensor = Blueprint('api_sensor', __name__, url_prefix='/api/sensors')

@api_sensor.route('/', methods=['POST'])
def create_sensor():
    try:
        return jsonify("test"), 201
    except Exception as e:
        logging.error(f"Error creating sensor: {e}")
        return jsonify({"error": "Failed to create sensor"}), 500
