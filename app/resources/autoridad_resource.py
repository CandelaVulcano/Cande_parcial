from flask import Blueprint, request, jsonify
from app.services.autoridad_service import AutoridadService
from app.mapping.autoridad_mapping import AutoridadMapping

autoridad_bp = Blueprint('autoridad', __name__)
autoridad_mapping = AutoridadMapping()


# GET /autoridades - Obtener todas las autoridades
@autoridad_bp.route('/autoridades', methods=['GET'])
def read_all():
    autoridades = AutoridadService.buscar_todos()
    return autoridad_mapping.dump(autoridades, many=True), 200


# GET /autoridad/<id> - Obtener una autoridad por ID
@autoridad_bp.route('/autoridad/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    autoridad = AutoridadService.buscar_por_id(id)
    if not autoridad:
        return jsonify({"error": "Autoridad no encontrada"}), 404
    return autoridad_mapping.dump(autoridad), 200


# POST /autoridad - Crear una nueva autoridad
@autoridad_bp.route('/autoridad', methods=['POST'])
def create():
    data = request.get_json()
    try:
        nueva_autoridad = AutoridadService.crear_autoridad(data)
        return autoridad_mapping.dump(nueva_autoridad), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# PUT /autoridad/<id> - Actualizar una autoridad
@autoridad_bp.route('/autoridad/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    try:
        autoridad_actualizada = AutoridadService.actualizar_autoridad(id, data)
        if not autoridad_actualizada:
            return jsonify({"error": "Autoridad no encontrada"}), 404
        return autoridad_mapping.dump(autoridad_actualizada), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# DELETE /autoridad/<id> - Eliminar una autoridad
@autoridad_bp.route('/autoridad/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = AutoridadService.borrar_autoridad(id)
    if not eliminado:
        return jsonify({"error": "Autoridad no encontrada"}), 404
    return jsonify({"message": "Autoridad eliminada"}), 200
