from app.repositories.cursada_repositorio import CursadaRepository

class CursadaService:
    @staticmethod
    def buscar_todos():
        return CursadaRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id: int):
        return CursadaRepository.buscar_por_id(id)
