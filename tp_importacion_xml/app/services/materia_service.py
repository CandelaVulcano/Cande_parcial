from app.models.materia import Materia
from app.repositories.materia_repositorio import agregar_materia, obtener_materia_por_codigo

def crear_o_actualizar_materia(especialidad, plan, codigo, nombre, ano):
    materia = obtener_materia_por_codigo(codigo)
    if not materia:
        materia = Materia(especialidad=especialidad, plan=plan, materia=codigo, nombre=nombre, ano=ano)
        agregar_materia(materia)
    else:
        materia.nombre = nombre
        materia.ano = ano
        agregar_materia(materia)
    return materia
