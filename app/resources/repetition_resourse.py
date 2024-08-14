from flask import Blueprint, request
from app.mapping import RepetitionSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services.repetition_service import RepetitionService

repetition_bp = Blueprint('repetition', __name__)
repetition_schema = RepetitionSchema()
response_schema = ResponseSchema()
repetition_service = RepetitionService()

@repetition_bp.route('/repetitions', methods=['GET'])
def index():
    return {"repetitions": repetition_schema.dump(repetition_service.all(), many=True)}, 200

@repetition_bp.route('/repetitions/<int:id>', methods=['GET'])
def find(id: int):
    response_builder = ResponseBuilder()
    repetition = repetition_service.find(id)
    if repetition:
        response_builder.add_message("Repetition found").add_status_code(100).add_data(repetition_schema.dump(repetition))
    else:
        response_builder.add_message("Repetition not found").add_status_code(404).add_data({"id": id})
    return response_schema.dump(response_builder.build()), 200

@repetition_bp.route('/repetitions/add', methods=['POST'])
def post_repetition():
    repetition = repetition_schema.load(request.json)
    saved_repetition = repetition_service.save(repetition)
    return {"repetition": repetition_schema.dump(saved_repetition)}, 201

@repetition_bp.route('/repetitions/<int:id>', methods=['PUT'])
def update_repetition(id: int):
    repetition = repetition_schema.load(request.json)
    updated_repetition = repetition_service.update(repetition, id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Repetition updated").add_status_code(100).add_data(repetition_schema.dump(updated_repetition))
    return response_schema.dump(response_builder.build()), 200

@repetition_bp.route('/repetitions/<int:id>', methods=['DELETE'])
def delete_repetition(id: int):
    repetition_service.delete(id)
    response_builder = ResponseBuilder()
    response_builder.add_message("Repetition deleted").add_status_code(100).add_data({"id": id})
    return response_schema.dump(response_builder.build()), 200
