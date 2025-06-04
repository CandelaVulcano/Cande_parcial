from app.models.materia import Materia
from app.repositories.session import get_session

def agregar_materia(materia):
    session = get_session()
    session.add(materia)
    session.commit()
    session.close()

def obtener_materia_por_codigo(codigo):
    session = get_session()
    result = session.query(Materia).filter_by(materia=codigo).first()
    session.close()
    return result
