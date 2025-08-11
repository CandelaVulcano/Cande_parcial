from flask import Blueprint, request, jsonify
from app.services.plan_service import PlanService
from app.mapping.plan_mapping import PlanMapping

plan_bp = Blueprint('plan', __name__)
plan_mapping = PlanMapping()
# GET /planes - Obtener todos los planes
@plan_bp.route('/planes', methods=['GET'])
def read_all():
    planes = PlanService.buscar_todos()
    return plan_mapping.dump(planes, many=True), 200
# GET /plan/<id> - Obtener un plan por ID
@plan_bp.route('/plan/<hashid:id>', methods=['GET'])
def read_by_id(id: int):
    plan = PlanService.buscar_por_id(id)
    if not plan:
        return jsonify({"error": "Plan no encontrado"}), 404
    return plan_mapping.dump(plan), 200
# POST /plan - Crear un nuevo plan
@plan_bp.route('/plan', methods=['POST'])
def create():
    data = request.get_json()
    try:
        nuevo_plan = PlanService.crear_plan(data)
        return plan_mapping.dump(nuevo_plan), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
# PUT /plan/<id> - Actualizar un plan
@plan_bp.route('/plan/<hashid:id>', methods=['PUT'])
def update(id: int):
    data = request.get_json()
    try:
        plan_actualizado = PlanService.actualizar_plan(id, data)
        if not plan_actualizado:
            return jsonify({"error": "Plan no encontrado"}), 404
        return plan_mapping.dump(plan_actualizado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    def test_borrar_grupo(self):
        grupo = self.__nuevoGrupo()
        GrupoService.crear_grupo(grupo)
        resultado = GrupoService.borrar_grupo(grupo.id)
        self.assertTrue(resultado)
        grupo_buscado = GrupoService.buscar_por_id(grupo.id)
        self.assertIsNone(grupo_buscado)
# DELETE /plan/<id> - Eliminar un plan
@plan_bp.route('/plan/<hashid:id>', methods=['DELETE'])
def delete(id: int):
    eliminado = PlanService.borrar_plan(id)
    if not eliminado:
        return jsonify({"error": "Plan no encontrado"}), 404
    return jsonify({"message": "Plan eliminado"}), 200

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    app.register_blueprint(plan_bp)
    app.run(debug=True)