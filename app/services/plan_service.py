from app.models.plan import Plan
from app.repositories.plan_repositorio import PlanRepository

class PlanService:
    @staticmethod
    def crear_plan(plan: Plan):
        return PlanRepository.crear(plan)

    @staticmethod
    def buscar_por_id(id: int) -> Plan:
        return PlanRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Plan]:
        return PlanRepository.buscar_todos()

    @staticmethod
    def actualizar_plan(plan: Plan) -> Plan:
        return PlanRepository.actualizar(plan)

    @staticmethod
    def borrar_por_id(id: int) -> Plan:
        return PlanRepository.borrar_por_id(id)
