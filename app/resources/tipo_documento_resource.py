from flask import Blueprint, request, jsonify
from app.services.tipo_documento_service import TipoDocumentoService
from app.models.tipo_documento import TipoDocumento
from app import db

tipo_documento_blueprint = Blueprint('tipo_documento', __name__)
# GET /tipos_documento - Obtener todos los tipos de documento
@tipo_documento_blueprint.route('/tipos_documento', methods=['GET'])
def get_all_tipos_documento():
    tipos_documento = TipoDocumentoService.buscar_todos()
    return jsonify([tipo.to_dict() for tipo in tipos_documento]), 200
# GET /tipo_documento/<id> - Obtener un tipo de documento por ID
@tipo_documento_blueprint.route('/tipo_documento/<hashid:id>', methods=['GET'])
def get_tipo_documento_by_id(id: int):
    tipo_documento = TipoDocumentoService.buscar_por_id(id)
    if not tipo_documento:
        return jsonify({"error": "Tipo de documento no encontrado"}), 404
    return jsonify(tipo_documento.to_dict()), 200
# POST /tipo_documento - Crear un nuevo tipo de documento
@tipo_documento_blueprint.route('/tipo_documento', methods=['POST'])
def create_tipo_documento():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        nuevo_tipo_documento = TipoDocumentoService.crear_tipo_documento(data)
        return jsonify(nuevo_tipo_documento.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# PUT /tipo_documento/<id> - Actualizar un tipo de documento
@tipo_documento_blueprint.route('/tipo_documento/<hashid:id>', methods=['PUT'])
def update_tipo_documento(id: int):
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "Datos inválidos"}), 400
    try:
        tipo_documento_actualizado = TipoDocumentoService.actualizar_tipo_documento(id, data)
        if not tipo_documento_actualizado:
            return jsonify({"error": "Tipo de documento no encontrado"}), 404
        return jsonify(tipo_documento_actualizado.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# DELETE /tipo_documento/<id> - Eliminar un tipo de documento
@tipo_documento_blueprint.route('/tipo_documento/<hashid:id>', methods=['DELETE'])
def delete_tipo_documento(id: int):
    eliminado = TipoDocumentoService.borrar_tipo_documento(id)
    if not eliminado:
        return jsonify({"error": "Tipo de documento no encontrado"}), 404
    return jsonify({"message": "Tipo de documento eliminado"}), 200
