from app.repositories.cursada_repositorio import CursadaRepository
from app.models.cursada import Cursada
from app import db

class CursadaService:
    @staticmethod
    def buscar_todos():
        return CursadaRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id: int):
        return CursadaRepository.buscar_por_id(id)

    @staticmethod
    def crear(data):
        nueva_cursada = Cursada(**data)
        db.session.add(nueva_cursada)
        db.session.commit()
        return nueva_cursada

    @staticmethod
    def actualizar(id: int, data):
        cursada = CursadaRepository.buscar_por_id(id)
        if not cursada:
            return None
        for key, value in data.items():
            setattr(cursada, key, value)
        db.session.commit()
        return cursada

    @staticmethod
    def borrar_por_id(id: int):
        cursada = CursadaRepository.buscar_por_id(id)
        if not cursada:
            return None
        db.session.delete(cursada)
        db.session.commit()
        return cursada
