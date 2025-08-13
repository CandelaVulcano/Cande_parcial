from flask import Blueprint, request, jsonify
from app.services.orientacion_service import OrientacionService
from app.models.orientacion import Orientacion
from app import db

orientacion_blueprint = Blueprint('orientacion', __name__)
# GET /orientaciones - Obtener todas las orientaciones
@orientacion_blueprint.route('/orientaciones', methods=['GET'])
def get_all_orientaciones():
    orientaciones = OrientacionService.buscar_todos()
    return jsonify([orientacion.to_dict() for orientacion in orientaciones]), 200
# GET /orientacion/<id> - Obtener una orientacion por ID
@orientacion_blueprint.route('/orientacion/<hashid:id>', methods=['GET'])
def get_orientacion_by_id(id: int):
    orientacion = OrientacionService.buscar_por_id(id)
    if not orientacion:
        return jsonify({"error": "Orientación no encontrada"}), 404
    return jsonify(orientacion.to_dict()), 200
# POST /orientacion - Crear una nueva orientacion
@orientacion_blueprint.route('/orientacion', methods=['POST'])
def create_orientacion():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        nueva_orientacion = OrientacionService.crear_orientacion(data)
        return jsonify(nueva_orientacion.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# PUT /orientacion/<id> - Actualizar una orientacion
@orientacion_blueprint.route('/orientacion/<hashid:id>', methods=['PUT'])
def update_orientacion(id: int):
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        orientacion_actualizada = OrientacionService.actualizar_orientacion(id, data)
        if not orientacion_actualizada:
            return jsonify({"error": "Orientación no encontrada"}), 404
        return jsonify(orientacion_actualizada.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# DELETE /orientacion/<id> - Eliminar una orientacion
@orientacion_blueprint.route('/orientacion/<hashid:id>', methods=['DELETE'])
def delete_orientacion(id: int):
    eliminado = OrientacionService.borrar_orientacion(id)
    if not eliminado:
        return jsonify({"error": "Orientación no encontrada"}), 404
    return jsonify({"message": "Orientación eliminada"}), 200
