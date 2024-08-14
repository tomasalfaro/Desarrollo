from flask import Blueprint, request
from app.mapping import WorkoutSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.workout_service import WorkoutService

workout_bp = Blueprint('workout', __name__)
workout_schema = WorkoutSchema()
response_schema = ResponseSchema()
workout_service = WorkoutService()

@workout_bp.route('/workouts', methods=['GET'])
def index():
    return {"workouts": workout_schema.dump(workout_service.all(), many=True)}, 200

@workout_bp.route('/workouts/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    workout = workout_service.find(id)
    if workout:
        response_builder.add_message("Workout found").add_status_code(100).add_data(workout_schema.dump(workout))
    else:
        response_builder.add_message("Workout not found").add_status_code(404).add_data({"id": id})
    return response_schema.dump(response_builder.build()), 200

@workout_bp.route('/workouts/add', methods=['POST'])
def post_workout():
    workout = workout_schema.load(request.json)
    saved_workout = workout_service.save(workout)
    return {"workout": workout_schema.dump(saved_workout)}, 201

@workout_bp.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id: int):
    workout = workout_schema.load(request.json)
    updated_workout = workout_service.update(workout, id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Workout updated").add_status_code(100).add_data(workout_schema.dump(updated_workout))
    return response_schema.dump(response_builder.build()), 200

@workout_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id: int):
    workout_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Workout deleted").add_status_code(100).add_data({"id": id})
    return response_schema.dump(response_builder.build()), 200
