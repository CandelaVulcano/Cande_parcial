from app.models.plan import Plan
from app.repositories.plan_repositorio import agregar_plan, obtener_plan_por_codigo

def crear_o_actualizar_plan(especialidad, codigo, nombre):
    plan = obtener_plan_por_codigo(codigo)
    if not plan:
        plan = Plan(especialidad=especialidad, plan=codigo, nombre=nombre)
        agregar_plan(plan)
    else:
        plan.nombre = nombre
        agregar_plan(plan)
    return plan
