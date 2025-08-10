from app import db
from app.models import Facultad


class FacultadRepository:
    @staticmethod
    def crear(facultad):
        db.session.add(facultad)
        db.session.commit()
        return facultad

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Facultad).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Facultad).all()

    @staticmethod
    def actualizar_facultad(facultad) -> Facultad:

        facultad_existente = db.session.merge(facultad)
        if not facultad_existente:
            return None
        return facultad_existente

    @staticmethod
    def borrar_por_id(id: int) -> Facultad:
        facultad = db.session.query(Facultad).filter_by(id=id).first()
        if not facultad:
            return None
        db.session.delete(facultad)
        db.session.commit()
        return facultad
