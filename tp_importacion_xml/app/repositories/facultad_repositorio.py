from app.models.facultad import Facultad
from app.repositories.session import get_session

def agregar_facultad(facultad):
    session = get_session()
    session.add(facultad)
    session.commit()
    session.close()

def obtener_facultad_por_codigo(codigo):
    session = get_session()
    result = session.query(Facultad).filter_by(facultad=codigo).first()
    session.close()
    return result
