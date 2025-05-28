from app.models.cargo import Cargo
from app import db

class CargoRepository:
    @staticmethod
    def crear(cargo):
        db.session.add(cargo)
        db.session.commit()
        return cargo

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Cargo).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Cargo).all()

    @staticmethod
    def actualizar(cargo):
        cargo_existente = db.session.merge(cargo)
        db.session.commit()
        return cargo_existente

    @staticmethod
    def borrar_por_id(id: int):
        cargo = db.session.query(Cargo).filter_by(id=id).first()
        if not cargo:
            return None
        db.session.delete(cargo)
        db.session.commit()
        return cargo
