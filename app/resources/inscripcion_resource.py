from flask import Blueprint, request, jsonify
from app.services.inscripcion_service import InscripcionService
from app.mapping.inscripcion_mapping import InscripcionMapping

inscripcion_bp = Blueprint('inscripcion', __name__)
inscripcion_mapping = InscripcionMapping()

@inscripcion_bp.route('/inscripciones', methods=['GET'])
def read_all():
    inscripciones = InscripcionService.buscar_todos()
    return inscripcion_mapping.dump(inscripciones, many=True), 200

@inscripcion_bp.route('/inscripcion/<int:id>', methods=['GET'])
def read_by_id(id):
    inscripcion = InscripcionService.buscar_por_id(id)
    return inscripcion_mapping.dump(inscripcion), 200