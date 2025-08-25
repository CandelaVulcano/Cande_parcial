
from flask import Blueprint, request, jsonify
from app.services.tipo_documento_service import TipoDocumentoService
from app.mapping.tipo_documento_mapping import TipoDocumentoMapping
from app.validators.tipo_documento_validator import TipoDocumentoValidator


tipo_documento_blueprint = Blueprint('tipo_documento', __name__)
tipo_documento_mapping = TipoDocumentoMapping()

@tipo_documento_blueprint.route('/tipos_documento', methods=['GET'])
def get_all_tipos_documento():
    tipos_documento = TipoDocumentoService.buscar_todos()
    return tipo_documento_mapping.dump(tipos_documento, many=True), 200

@tipo_documento_blueprint.route('/tipo_documento/<hashid:id>', methods=['GET'])
def get_tipo_documento_by_id(id: int):
    tipo_documento = TipoDocumentoService.buscar_por_id(id)
    if not tipo_documento:
        return jsonify({"error": "Tipo de documento no encontrado"}), 404
    return tipo_documento_mapping.dump(tipo_documento), 200

@tipo_documento_blueprint.route('/tipo_documento', methods=['POST'])
def create_tipo_documento():
    data = request.get_json()
    errors = TipoDocumentoValidator.validate_tipo_documento(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        nuevo_tipo_documento = TipoDocumentoService.crear_tipo_documento(data)
        return tipo_documento_mapping.dump(nuevo_tipo_documento), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tipo_documento_blueprint.route('/tipo_documento/<hashid:id>', methods=['PUT'])
def update_tipo_documento(id: int):
    data = request.get_json()
    errors = TipoDocumentoValidator.validate_tipo_documento(data)
    if errors:
        return jsonify({'errors': errors}), 400
    try:
        tipo_documento_actualizado = TipoDocumentoService.actualizar_tipo_documento(id, data)
        if not tipo_documento_actualizado:
            return jsonify({"error": "Tipo de documento no encontrado"}), 404
        return tipo_documento_mapping.dump(tipo_documento_actualizado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tipo_documento_blueprint.route('/tipo_documento/<hashid:id>', methods=['DELETE'])
def delete_tipo_documento(id: int):
    eliminado = TipoDocumentoService.borrar_tipo_documento(id)
    if not eliminado:
        return jsonify({"error": "Tipo de documento no encontrado"}), 404
    return jsonify({"message": "Tipo de documento eliminado"}), 200
