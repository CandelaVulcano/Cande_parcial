from flask import Blueprint, request, jsonify
from app.services.facultad_service import FacultadService
from app.models.facultad import Facultad
from app import db
from app.utils import validate_json

facultad_bp = Blueprint('facultad', __name__)

@facultad_bp.route('/facultades', methods=['GET'])
def read_all():
    facultades = FacultadService.buscar_todos()
    return jsonify([facultad.to_dict() for facultad in facultades]), 200

@facultad_bp.route('/facultad/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    facultad = FacultadService.buscar_por_id(id)
    if not facultad:
        return jsonify({"error": "Facultad no encontrada"}), 404
    return jsonify(facultad.to_dict()), 200

@facultad_bp.route('/facultad', methods=['POST'])
def create():
    data = request.get_json()
    if not validate_json(data, Facultad):
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        nueva_facultad = FacultadService.crear_facultad(data)
        return jsonify(nueva_facultad.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@facultad_bp.route('/facultad/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    if not validate_json(data, Facultad):
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        facultad_actualizada = FacultadService.actualizar_facultad(id, data)
        if not facultad_actualizada:
            return jsonify({"error": "Facultad no encontrada"}), 404
        return jsonify(facultad_actualizada.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@facultad_bp.route('/facultad/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = FacultadService.borrar_facultad(id)
    if not eliminado:
        return jsonify({"error": "Facultad no encontrada"}), 404
    return jsonify({"message": "Facultad eliminada"}), 200