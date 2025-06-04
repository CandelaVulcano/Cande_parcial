from app.models.pais import Pais
from app.repositories.session import get_session

def agregar_pais(pais):
    session = get_session()
    session.add(pais)
    session.commit()
    session.close()

def obtener_pais_por_codigo(codigo):
    session = get_session()
    result = session.query(Pais).filter_by(pais=codigo).first()
    session.close()
    return result
