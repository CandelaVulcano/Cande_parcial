from app.models.cursada import Cursada
from app import db

class CursadaRepository:
    @staticmethod
    def buscar_todos():
        return db.session.query(Cursada).all()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Cursada).filter_by(id=id).first()
