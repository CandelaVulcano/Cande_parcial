from app.models.grado import Grado
from app.repositories.session import get_session

def agregar_grado(grado):
    session = get_session()
    session.add(grado)
    session.commit()
    session.close()

def obtener_grado_por_codigo(codigo):
    session = get_session()
    result = session.query(Grado).filter_by(grado=codigo).first()
    session.close()
    return result
