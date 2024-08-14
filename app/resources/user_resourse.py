from flask import Blueprint, request, jsonify
from app.mapping import UserSchema, ResponseSchema 
from app.services.response_message import ResponseBuilder
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()
response_schema = ResponseSchema()
user_service = UserService()

@user_bp.route('/users', methods=['GET'])
def index():
    users = user_service.all()
    return jsonify({"users": user_schema.dump(users, many=True)}), 200

@user_bp.route('/users/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    user = user_service.find(id)
    if user:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return jsonify(response_schema.dump(response_builder.build())), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(404)
        return jsonify(response_schema.dump(response_builder.build())), 404

@user_bp.route('/users', methods=['POST'])
def post_user():
    user_data = user_schema.load(request.json)
    user = user_service.save(user_data)
    return jsonify({"user": user_schema.dump(user)}), 201

@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id: int):
    user_data = user_schema.load(request.json)
    response_builder = ResponseBuilder()
    user = user_service.update(user_data, id)
    if user:
        response_builder.add_message("Usuario actualizado").add_status_code(100).add_data(user_schema.dump(user))
        return jsonify(response_schema.dump(response_builder.build())), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(404)
        return jsonify(response_schema.dump(response_builder.build())), 404

@user_bp.route('/users/username/<username>', methods=['GET'])
def find_by_username(username: str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_username(username)
    if user:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return jsonify(response_schema.dump(response_builder.build())), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(404).add_data({'username': username})
        return jsonify(response_schema.dump(response_builder.build())), 404

@user_bp.route('/users/email/<email>', methods=['GET'])
def find_by_email(email: str):
    response_builder = ResponseBuilder()
    user = user_service.find_by_email(email)
    if user:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(user))
        return jsonify(response_schema.dump(response_builder.build())), 200
    else:
        response_builder.add_message("Usuario no encontrado").add_status_code(404).add_data({'email': email})
        return jsonify(response_schema.dump(response_builder.build())), 404

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    user_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario borrado").add_status_code(100).add_data({'id': id})
    return jsonify(response_schema.dump(response_builder.build())), 200