from app.models.categoria_cargo import CategoriaCargo
from app import db

class CategoriaCargoRepository:
    @staticmethod
    def crear(categoria_cargo):
        db.session.add(categoria_cargo)
        db.session.commit()
        return categoria_cargo

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(CategoriaCargo).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(CategoriaCargo).all()

    @staticmethod
    def actualizar(categoria_cargo):
        categoria_cargo_existente = db.session.merge(categoria_cargo)
        db.session.commit()
        return categoria_cargo_existente

    @staticmethod
    def borrar_por_id(id: int):
        categoria_cargo = db.session.query(CategoriaCargo).filter_by(id=id).first()
        if not categoria_cargo:
            return None
        db.session.delete(categoria_cargo)
        db.session.commit()
        return categoria_cargo
