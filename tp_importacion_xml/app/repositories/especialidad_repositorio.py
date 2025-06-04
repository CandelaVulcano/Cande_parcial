from app.models.especialidad import Especialidad
from app.repositories.session import get_session

def agregar_especialidad(especialidad):
    session = get_session()
    session.add(especialidad)
    session.commit()
    session.close()

def obtener_especialidad_por_codigo(codigo):
    session = get_session()
    result = session.query(Especialidad).filter_by(especialidad=codigo).first()
    session.close()
    return result
