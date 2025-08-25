from app.models.nota import Nota
from app import db

class NotaRepository:
    @staticmethod
    def buscar_todos():
        return db.session.query(Nota).all()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Nota).filter_by(id=id).first()
