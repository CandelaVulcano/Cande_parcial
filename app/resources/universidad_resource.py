
from flask import jsonify, Blueprint, request
from app.services import UniversidadService
from app.mapping.universidad_mapping import UniversidadMapping
from app.validators.universidad_validator import UniversidadValidator

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadMapping()


@universidad_bp.route('/universidad', methods=['GET'])
def index():
    universidades = UniversidadService.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200


@universidad_bp.route('/universidad/<hashid:id>', methods=['GET'])
def buscar_por_id(id: int):
    universidad = UniversidadService.buscar_por_id(id)
    return universidad_mapping.dump(universidad), 200


@universidad_bp.route('/universidad', methods=['POST'])
def crear_universidad():
    data = request.get_json()
    errors = UniversidadValidator.validate_universidad(data)
    if errors:
        return jsonify({'errors': errors}), 400
    universidad = UniversidadService.crear(data)
    return universidad_mapping.dump(universidad), 201


@universidad_bp.route('/universidad/<hashid:id>', methods=['DELETE'])
def eliminar_universidad(id: int):
    UniversidadService.eliminar(id)
    return jsonify('Universidad eliminada exitosamente'), 200



@universidad_bp.route('/universidad/<hashid:id>', methods=['PUT'])
def actualizar_universidad(id: int):
    data = request.get_json()
    errors = UniversidadValidator.validate_universidad(data)
    if errors:
        return jsonify({'errors': errors}), 400
    universidad = UniversidadService.actualizar(id, data)
    return universidad_mapping.dump(universidad), 200



