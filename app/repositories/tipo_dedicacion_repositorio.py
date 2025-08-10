from app import db
from app.models.tipo_dedicacion import TipoDedicacion


class TipoDedicacionRepository:
    @staticmethod
    def crear(tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        db.session.add(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion

    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        return db.session.query(TipoDedicacion).filter_by(id=id).first()

    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        return db.session.query(TipoDedicacion).all()

    @staticmethod
    def actualizar(tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        tipo_dedicacion_existente = db.session.merge(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion_existente

    @staticmethod
    def borrar_por_id(id: int) -> TipoDedicacion:
        tipo_dedicacion = db.session.query(
            TipoDedicacion).filter_by(id=id).first()
        if not tipo_dedicacion:
            return None
        db.session.delete(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion
