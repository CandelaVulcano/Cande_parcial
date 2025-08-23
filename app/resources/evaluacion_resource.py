from flask import Blueprint, request, jsonify
from app.services.evaluacion_service import EvaluacionService
from app.mapping.evaluacion_mapping import EvaluacionMapping

evaluacion_bp = Blueprint('evaluacion', __name__)
evaluacion_mapping = EvaluacionMapping()

@evaluacion_bp.route('/evaluaciones', methods=['GET'])
def read_all():
    evaluaciones = EvaluacionService.buscar_todos()
    return evaluacion_mapping.dump(evaluaciones, many=True), 200

@evaluacion_bp.route('/evaluacion/<int:id>', methods=['GET'])
def read_by_id(id):
    evaluacion = EvaluacionService.buscar_por_id(id)
    return evaluacion_mapping.dump(evaluacion), 200
