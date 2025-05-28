from app.models.grado import Grado
from app import db

class GradoRepository:
    @staticmethod
    def crear(grado):
        db.session.add(grado)
        db.session.commit()
        return grado

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Grado).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Grado).all()

    @staticmethod
    def actualizar(grado):
        grado_existente = db.session.merge(grado)
        db.session.commit()
        return grado_existente

    @staticmethod
    def borrar_por_id(id: int):
        grado = db.session.query(Grado).filter_by(id=id).first()
        if not grado:
            return None
        db.session.delete(grado)
        db.session.commit()
        return grado
