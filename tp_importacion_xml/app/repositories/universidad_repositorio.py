from app.models.universidad import Universidad
from app.repositories.session import get_session

def agregar_universidad(universidad):
    session = get_session()
    session.add(universidad)
    session.commit()
    session.close()

def obtener_universidad_por_codigo(codigo):
    session = get_session()
    result = session.query(Universidad).filter_by(universida=codigo).first()
    session.close()
    return result
