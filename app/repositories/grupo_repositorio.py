from app.models.grupo import Grupo
from app import db

class GrupoRepository:
    @staticmethod
    def crear(grupo):
        db.session.add(grupo)
        db.session.commit()
        return grupo

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Grupo).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Grupo).all()

    @staticmethod
    def actualizar(grupo):
        grupo_existente = db.session.merge(grupo)
        db.session.commit()
        return grupo_existente

    @staticmethod
    def borrar_por_id(id: int):
        grupo = db.session.query(Grupo).filter_by(id=id).first()
        if not grupo:
            return None
        db.session.delete(grupo)
        db.session.commit()
        return grupo
