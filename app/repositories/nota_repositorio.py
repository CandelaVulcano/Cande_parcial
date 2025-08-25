from app.models.nota import Nota
from app import db

class NotaRepository:
    @staticmethod
    def crear(nota: Nota) -> Nota:
        db.session.add(nota)
        db.session.commit()
        return nota

    @staticmethod
    def buscar_todos():
        return db.session.query(Nota).all()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Nota).filter_by(id=id).first()
    
    @staticmethod
    def actualizar(nota: Nota) -> Nota:
        nota_existente = db.session.merge(nota)
        db.session.commit()
        return nota_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Nota:
        nota = db.session.query(Nota).filter_by(id=id).first()
        if nota:
            db.session.delete(nota)
            db.session.commit()
        return nota
