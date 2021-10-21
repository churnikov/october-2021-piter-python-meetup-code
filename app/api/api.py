from flask import jsonify, request

from app.validators import validate_add_data

from ..crud import add_data_to_db
from .main import app


@app.post("/v0/add-data")
def add_data():
    data = request.json
    validate_add_data(data)
    add_data_to_db(data)
    return jsonify({"result": "success"}), 200
