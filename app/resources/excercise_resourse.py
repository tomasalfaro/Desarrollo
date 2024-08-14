from flask import Blueprint, request
from app.mapping import ExcerciseSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.excercise_sevice import ExcerciseService

exercise_bp = Blueprint('exercise', __name__)
exercise_schema = ExcerciseSchema()
response_schema = ResponseSchema()
exercise_service = ExcerciseService()

@exercise_bp.route('/exercises', methods=['GET'])
def index():
    return {"exercises": exercise_schema.dump(exercise_service.all(), many=True)}, 200

@exercise_bp.route('/exercises/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    exercise = exercise_service.find(id)
    if exercise:
        response_builder.add_message("Exercise found").add_status_code(100).add_data(exercise_schema.dump(exercise))
    else:
        response_builder.add_message("Exercise not found").add_status_code(404).add_data({"id": id})
    return response_schema.dump(response_builder.build()), 200

@exercise_bp.route('/exercises/add', methods=['POST'])
def post_exercise():
    exercise = exercise_schema.load(request.json)
    saved_exercise = exercise_service.save(exercise)
    return {"exercise": exercise_schema.dump(saved_exercise)}, 201

@exercise_bp.route('/exercises/<int:id>', methods=['PUT'])
def update_exercise(id: int):
    exercise = exercise_schema.load(request.json)
    updated_exercise = exercise_service.update(exercise, id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Exercise updated").add_status_code(100).add_data(exercise_schema.dump(updated_exercise))
    return response_schema.dump(response_builder.build()), 200

@exercise_bp.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id: int):
    exercise_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Exercise deleted").add_status_code(100).add_data({"id": id})
    return response_schema.dump(response_builder.build()), 200
