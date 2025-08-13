from app.models.inscripcion import Inscripcion
from app import db

class InscripcionRepository:
    @staticmethod
    def buscar_todos():
        return db.session.query(Inscripcion).all()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Inscripcion).filter_by(id=id).first()

    @staticmethod
    def crear(inscripcion):
        db.session.add(inscripcion)
        db.session.commit()
        return inscripcion

    @staticmethod
    def actualizar(inscripcion):
        inscripcion_existente = db.session.merge(inscripcion)
        db.session.commit()
        return inscripcion_existente

    @staticmethod
    def borrar_por_id(id: int):
        inscripcion = db.session.query(Inscripcion).filter_by(id=id).first()
        if not inscripcion:
            return None
        db.session.delete(inscripcion)
        db.session.commit()
        return inscripcion
