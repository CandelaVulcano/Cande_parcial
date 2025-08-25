from flask import Blueprint, request, jsonify
from app.services.especialidad_service import EspecialidadService
from app.mapping.especialidad_mapping import EspecialidadMapping
from app.validators.especialidad_validator import validate_especialidad


especialidad_bp = Blueprint('especialidad', __name__)
especialidad_mapping = EspecialidadMapping()


@especialidad_bp.route('/especialidades', methods=['GET'])
def read_all():
    especialidades = EspecialidadService.buscar_todos()
    return especialidad_mapping.dump(especialidades, many=True), 200


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    especialidad = EspecialidadService.buscar_por_id(id)
    if not especialidad:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    return especialidad_mapping.dump(especialidad), 200


@especialidad_bp.route('/especialidad', methods=['POST'])
def create():
    data = request.get_json()
    errors = validate_especialidad(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        nueva_especialidad = EspecialidadService.crear_especialidad(data)
        return especialidad_mapping.dump(nueva_especialidad), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    errors = validate_especialidad(data)
    if errors:
        return jsonify({'errors': errors}), 400
    especialidad_actualizada = EspecialidadService.actualizar_especialidad(id, data)
    if not especialidad_actualizada:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    return especialidad_mapping.dump(especialidad_actualizada), 200


@especialidad_bp.route('/especialidad/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = EspecialidadService.borrar_especialidad(id)
    if not eliminado:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    return jsonify({"message": "Especialidad eliminada"}), 200