
from flask import Blueprint, request, jsonify
from app.services.orientacion_service import OrientacionService
from app.mapping.orientacion_mapping import OrientacionMapping
from app.validators.orientacion_validator import OrientacionValidator


orientacion_blueprint = Blueprint('orientacion', __name__)
orientacion_mapping = OrientacionMapping()

@orientacion_blueprint.route('/orientaciones', methods=['GET'])
def get_all_orientaciones():
    orientaciones = OrientacionService.buscar_todos()
    return orientacion_mapping.dump(orientaciones, many=True), 200

@orientacion_blueprint.route('/orientacion/<hashid:id>', methods=['GET'])
def get_orientacion_by_id(id: int):
    orientacion = OrientacionService.buscar_por_id(id)
    if not orientacion:
        return jsonify({"error": "Orientación no encontrada"}), 404
    return orientacion_mapping.dump(orientacion), 200

@orientacion_blueprint.route('/orientacion', methods=['POST'])
def create_orientacion():
    data = request.get_json()
    errors = OrientacionValidator.validate_orientacion(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        nueva_orientacion = OrientacionService.crear_orientacion(data)
        return orientacion_mapping.dump(nueva_orientacion), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@orientacion_blueprint.route('/orientacion/<hashid:id>', methods=['PUT'])
def update_orientacion(id: int):
    data = request.get_json()
    errors = OrientacionValidator.validate_orientacion(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        orientacion_actualizada = OrientacionService.actualizar_orientacion(id, data)
        if not orientacion_actualizada:
            return jsonify({"error": "Orientación no encontrada"}), 404
        return orientacion_mapping.dump(orientacion_actualizada), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@orientacion_blueprint.route('/orientacion/<hashid:id>', methods=['DELETE'])
def delete_orientacion(id: int):
    eliminado = OrientacionService.borrar_orientacion(id)
    if not eliminado:
        return jsonify({"error": "Orientación no encontrada"}), 404
    return jsonify({"message": "Orientación eliminada"}), 200
