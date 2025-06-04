from app.models.orientacion import Orientacion
from app.repositories.session import get_session

def agregar_orientacion(orientacion):
    session = get_session()
    session.add(orientacion)
    session.commit()
    session.close()

def obtener_orientacion_por_codigo(codigo):
    session = get_session()
    result = session.query(Orientacion).filter_by(orientacion=codigo).first()
    session.close()
    return result
