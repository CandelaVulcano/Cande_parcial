from flask import Blueprint, request, jsonify
from app.services.departamento_service import DepartamentoService
from app.mapping.departamento_mapping import DepartamentoMapping
departamento_bp = Blueprint('departamento', __name__)
departamento_mapping = DepartamentoMapping()
# GET /departamentos - Obtener todos los departamentos
@departamento_bp.route('/departamentos', methods=['GET'])
def read_all():
    departamentos = DepartamentoService.buscar_todos()
    return departamento_mapping.dump(departamentos, many=True), 200
# GET /departamento/<id> - Obtener un departamento por ID
@departamento_bp.route('/departamento/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    departamento = DepartamentoService.buscar_por_id(id)
    if not departamento:
        return jsonify({"error": "Departamento no encontrado"}), 404
    return departamento_mapping.dump(departamento), 200
# POST /departamento - Crear un nuevo departamento
@departamento_bp.route('/departamento', methods=['POST'])
def create():
    data = request.get_json()
    try:
        nuevo_departamento = DepartamentoService.crear_departamento(data)
        return departamento_mapping.dump(nuevo_departamento), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# PUT /departamento/<id> - Actualizar un departamento
@departamento_bp.route('/departamento/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    try:
        departamento_actualizado = DepartamentoService.actualizar_departamento(id, data)
        if not departamento_actualizado:
            return jsonify({"error": "Departamento no encontrado"}), 404
        return departamento_mapping.dump(departamento_actualizado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# DELETE /departamento/<id> - Eliminar un departamento
@departamento_bp.route('/departamento/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = DepartamentoService.borrar_departamento(id)
    if not eliminado:
        return jsonify({"error": "Departamento no encontrado"}), 404
    return jsonify({"message": "Departamento eliminado"}), 200