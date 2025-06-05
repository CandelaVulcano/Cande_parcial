from app.models.localidad import Localidad
from app.repositories.session import get_session

def agregar_localidad(localidad):
    session = get_session()
    session.add(localidad)
    session.commit()
    session.close()

def obtener_localidad_por_codigo(codigo):
    session = get_session()
    result = session.query(Localidad).filter_by(codigo=codigo).first()
    session.close()
    return result
