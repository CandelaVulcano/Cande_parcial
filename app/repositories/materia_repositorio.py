from app.models.materia import Materia
from app import db

class MateriaRepository:
    @staticmethod
    def crear(materia):
        db.session.add(materia)
        db.session.commit()
        return materia

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Materia).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Materia).all()

    @staticmethod
    def actualizar(materia):
        materia_existente = db.session.merge(materia)
        db.session.commit()
        return materia_existente

    @staticmethod
    def borrar_por_id(id: int):
        materia = db.session.query(Materia).filter_by(id=id).first()
        if not materia:
            return None
        db.session.delete(materia)
        db.session.commit()
        return materia
