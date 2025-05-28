from app.models.universidad import Universidad
from app import db

class UniversidadRepository:
    @staticmethod
    def crear(universidad):
        db.session.add(universidad)
        db.session.commit()
        return universidad

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Universidad).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Universidad).all()

    @staticmethod
    def actualizar(universidad):
        universidad_existente = db.session.merge(universidad)
        db.session.commit()
        return universidad_existente

    @staticmethod
    def borrar_por_id(id: int):
        universidad = db.session.query(Universidad).filter_by(id=id).first()
        if not universidad:
            return None
        db.session.delete(universidad)
        db.session.commit()
        return universidad
