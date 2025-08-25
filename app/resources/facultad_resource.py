
from flask import Blueprint, request, jsonify
from app.services.facultad_service import FacultadService
from app.mapping.facultad_mapping import FacultadMapping
from app.validators.facultad_validator import validate_facultad


facultad_bp = Blueprint('facultad', __name__)
facultad_mapping = FacultadMapping()

@facultad_bp.route('/facultades', methods=['GET'])
def read_all():
    facultades = FacultadService.buscar_todos()
    return facultad_mapping.dump(facultades, many=True), 200

@facultad_bp.route('/facultad/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    facultad = FacultadService.buscar_por_id(id)
    if not facultad:
        return jsonify({"error": "Facultad no encontrada"}), 404
    return facultad_mapping.dump(facultad), 200

@facultad_bp.route('/facultad', methods=['POST'])
def create():
    data = request.get_json()
    errors = validate_facultad(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        nueva_facultad = FacultadService.crear_facultad(data)
        return facultad_mapping.dump(nueva_facultad), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@facultad_bp.route('/facultad/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    errors = validate_facultad(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        facultad_actualizada = FacultadService.actualizar_facultad(id, data)
        if not facultad_actualizada:
            return jsonify({"error": "Facultad no encontrada"}), 404
        return facultad_mapping.dump(facultad_actualizada), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@facultad_bp.route('/facultad/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = FacultadService.borrar_facultad(id)
    if not eliminado:
        return jsonify({"error": "Facultad no encontrada"}), 404
    return jsonify({"message": "Facultad eliminada"}), 200