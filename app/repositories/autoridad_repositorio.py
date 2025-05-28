from app.models.autoridad import Autoridad
from app import db

class AutoridadRepository:
    @staticmethod
    def crear(autoridad):
        db.session.add(autoridad)
        db.session.commit()
        return autoridad

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Autoridad).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Autoridad).all()

    @staticmethod
    def actualizar(autoridad):
        autoridad_existente = db.session.merge(autoridad)
        db.session.commit()
        return autoridad_existente

    @staticmethod
    def borrar_por_id(id: int):
        autoridad = db.session.query(Autoridad).filter_by(id=id).first()
        if not autoridad:
            return None
        db.session.delete(autoridad)
        db.session.commit()
        return autoridad
