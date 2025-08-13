from app.repositories.nota_repositorio import NotaRepository

class NotaService:
    @staticmethod
    def buscar_todos():
        return NotaRepository.buscar_todos()

    @staticmethod
    def buscar_por_id(id: int):
        return NotaRepository.buscar_por_id(id)
