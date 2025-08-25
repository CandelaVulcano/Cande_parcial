
from flask import Blueprint, request, jsonify
from app.services.inscripcion_service import InscripcionService
from app.mapping.inscripcion_mapping import InscripcionMapping
from app.validators.inscripcion_validator import InscripcionValidator

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

# Endpoint para crear una inscripción
@inscripcion_bp.route('/inscripciones', methods=['POST'])
def create_inscripcion():
    data = request.get_json()
    errors = InscripcionValidator.validate_inscripcion(data)
    if errors:
        return jsonify({'errors': errors}), 400
    nueva_inscripcion = InscripcionService.crear(data)
    return inscripcion_mapping.dump(nueva_inscripcion), 201

# Endpoint para actualizar una inscripción
@inscripcion_bp.route('/inscripcion/<int:id>', methods=['PUT'])
def update_inscripcion(id):
    data = request.get_json()
    errors = InscripcionValidator.validate_inscripcion(data)
    if errors:
        return jsonify({'errors': errors}), 400
    inscripcion_actualizada = InscripcionService.actualizar(id, data)
    if not inscripcion_actualizada:
        return jsonify({'error': 'Inscripción no encontrada'}), 404
    return inscripcion_mapping.dump(inscripcion_actualizada), 200
