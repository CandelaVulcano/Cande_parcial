from app.models.grado import Grado
from app import db

#KISS
# En nuestros repositorios (y en general, models, services) tratamos de usar una 
# estructura simple y que no sea difícil de leer y tampoco aplicamos 
# sobreingenieria (crear soluciones a problemas en los que ya hay funciones que 
# los resuelven) por lo que considero que se aplico el principio de KISS, se 
# puede ver eso en la linea: 
# return db.session,query(Grado).filter_by(id=id).first()

#DRY 
#Este principio esta aplicado al tener funciones que realizan acciones 
# especificas asi no es necesario reescribir esos fragmentos de código cada que 
# se quiera lograr cierto objetivo.

#YAGNI
#Considero que se cumplió ya que solo implementamos funciones que serán usadas 
# que son las operaciones de CRUD. No considero que hayan mas funciones de las 
# necesarias o que no se usen.

class GradoRepository:
    @staticmethod
    def crear(grado):
        db.session.add(grado)
        db.session.commit()
        return grado

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Grado).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Grado).all()

    @staticmethod
    def actualizar(grado):
        grado_existente = db.session.merge(grado)
        db.session.commit()
        return grado_existente

    @staticmethod
    def borrar_por_id(id: int):
        grado = db.session.query(Grado).filter_by(id=id).first()
        if not grado:
            return None
        db.session.delete(grado)
        db.session.commit()
        return grado
