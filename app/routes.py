# app/routes.py

from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "bio": "Seasoned Software Test Engineer with a Master’s in Electrical Engineering. Specializing in HIL/SIL testing, Python, C/C++, and software validation for vehicles."
    })

@main.route('/api/v1/resource', methods=['GET'])
def get_resource():
    return jsonify({"data": "Sample Data"})

@main.route('/api/v1/resource', methods=['POST'])
def create_resource():
    data = request.json
    if not data or not 'name' in data:
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"message": "Resource created", "data": data}), 201
