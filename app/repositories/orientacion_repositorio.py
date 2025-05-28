from app.models.orientacion import Orientacion
from app import db

class OrientacionRepository:
    @staticmethod
    def crear(orientacion):
        db.session.add(orientacion)
        db.session.commit()
        return orientacion

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Orientacion).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Orientacion).all()

    @staticmethod
    def actualizar(orientacion):
        orientacion_existente = db.session.merge(orientacion)
        db.session.commit()
        return orientacion_existente

    @staticmethod
    def borrar_por_id(id: int):
        orientacion = db.session.query(Orientacion).filter_by(id=id).first()
        if not orientacion:
            return None
        db.session.delete(orientacion)
        db.session.commit()
        return orientacion