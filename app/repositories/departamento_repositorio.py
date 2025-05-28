from app.models.departamento import Departamento
from app import db

class DepartamentoRepository:
    @staticmethod
    def crear(departamento):
        db.session.add(departamento)
        db.session.commit()
        return departamento

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Departamento).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Departamento).all()

    @staticmethod
    def actualizar(departamento):
        departamento_existente = db.session.merge(departamento)
        db.session.commit()
        return departamento_existente

    @staticmethod
    def borrar_por_id(id: int):
        departamento = db.session.query(Departamento).filter_by(id=id).first()
        if not departamento:
            return None
        db.session.delete(departamento)
        db.session.commit()
        return departamento
