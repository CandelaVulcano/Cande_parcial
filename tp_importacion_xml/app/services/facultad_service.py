from app.models.facultad import Facultad
from app.repositories.facultad_repositorio import agregar_facultad, obtener_facultad_por_codigo

def crear_o_actualizar_facultad(codigo, nombre):
    facultad = obtener_facultad_por_codigo(codigo)
    if not facultad:
        facultad = Facultad(facultad=codigo, nombre=nombre)
        agregar_facultad(facultad)
    else:
        facultad.nombre = nombre
        agregar_facultad(facultad)
    return facultad
