from flask import Blueprint, request, jsonify
from app.services.especialidad_service import EspecialidadService
from app.models.especialidad import Especialidad
from app import db

# NO TIENE ARCHIVO VALIDATOR, HAY QUE CREARLO

especialidad_bp = Blueprint('especialidad', __name__)


@especialidad_bp.route('/especialidades', methods=['GET'])
def read_all():
    especialidades = EspecialidadService.buscar_todos()
    return jsonify([especialidad.to_dict() for especialidad in especialidades]), 200


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    especialidad = EspecialidadService.buscar_por_id(id)
    if not especialidad:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    return jsonify(especialidad.to_dict()), 200


@especialidad_bp.route('/especialidad', methods=['POST'])
def create():
    data = request.get_json()
    if not validate_json(data, Especialidad):
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        nueva_especialidad = EspecialidadService.crear_especialidad(data)
        return jsonify(nueva_especialidad.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    if not validate_json(data, Especialidad):
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        especialidad_actualizada = EspecialidadService.actualizar_especialidad(
            id, data)
        if not especialidad_actualizada:
            return jsonify({"error": "Especialidad no encontrada"}), 404
        return jsonify(especialidad_actualizada.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = EspecialidadService.borrar_especialidad(id)
    if not eliminado:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    return jsonify({"message": "Especialidad eliminada"}), 200
