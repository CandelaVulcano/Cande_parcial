from app.models.area import Area
from app import db

class AreaRepository:
    @staticmethod
    def crear(area):
        db.session.add(area)
        db.session.commit()
        return area

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Area).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Area).all()

    @staticmethod
    def actualizar(area):
        area_existente = db.session.merge(area)
        db.session.commit()
        return area_existente

    @staticmethod
    def borrar_por_id(id: int):
        area = db.session.query(Area).filter_by(id=id).first()
        if not area:
            return None
        db.session.delete(area)
        db.session.commit()
        return area
