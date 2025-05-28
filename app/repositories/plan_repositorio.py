from app.models.plan import Plan
from app import db

class PlanRepository:
    @staticmethod
    def crear(plan):
        db.session.add(plan)
        db.session.commit()
        return plan

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Plan).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Plan).all()

    @staticmethod
    def actualizar(plan):
        plan_existente = db.session.merge(plan)
        db.session.commit()
        return plan_existente

    @staticmethod
    def borrar_por_id(id: int):
        plan = db.session.query(Plan).filter_by(id=id).first()
        if not plan:
            return None
        db.session.delete(plan)
        db.session.commit()
        return plan
