from flask import Blueprint, request, jsonify
from app.services.cargo_service import CargoService
from app.mapping.cargo_mapping import CargoMapping

cargo_bp = Blueprint('cargo', __name__)
cargo_mapping = CargoMapping()


# GET /cargos - Obtener todos los cargos
@cargo_bp.route('/cargos', methods=['GET'])
def read_all():
    cargos = CargoService.buscar_todos()
    return cargo_mapping.dump(cargos, many=True), 200


# GET /cargo/<id> - Obtener un cargo por ID
@cargo_bp.route('/cargo/<int:id>', methods=['GET'])
def read_by_id(id: int):
    cargo = CargoService.buscar_por_id(id)
    if not cargo:
        return jsonify({"error": "Cargo no encontrado"}), 404
    return cargo_mapping.dump(cargo), 200


# POST /cargo - Crear un nuevo cargo
@cargo_bp.route('/cargo', methods=['POST'])
def create():
    data = request.get_json()
    try:
        nuevo_cargo = CargoService.crear_cargo(data)
        return cargo_mapping.dump(nuevo_cargo), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# PUT /cargo/<id> - Actualizar un cargo
@cargo_bp.route('/cargo/<int:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    try:
        cargo_actualizado = CargoService.actualizar_cargo(id, data)
        if not cargo_actualizado:
            return jsonify({"error": "Cargo no encontrado"}), 404
        return cargo_mapping.dump(cargo_actualizado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# DELETE /cargo/<id> - Eliminar un cargo
@cargo_bp.route('/cargo/<int:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = CargoService.borrar_cargo(id)
    if not eliminado:
        return jsonify({"error": "Cargo no encontrado"}), 404
    return jsonify({"message": "Cargo eliminado"}), 200
