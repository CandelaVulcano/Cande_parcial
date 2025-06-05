from app.models.plan import Plan
from app.repositories.session import get_session

def agregar_plan(plan):
    session = get_session()
    session.add(plan)
    session.commit()
    session.close()

def obtener_plan_por_codigo(codigo):
    session = get_session()
    result = session.query(Plan).filter_by(plan=codigo).first()
    session.close()
    return result
