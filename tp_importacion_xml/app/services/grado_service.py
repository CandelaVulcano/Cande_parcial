from app.models.grado import Grado
from app.repositories.grado_repositorio import agregar_grado, obtener_grado_por_codigo

def crear_o_actualizar_grado(codigo, nombre):
    grado = obtener_grado_por_codigo(codigo)
    if not grado:
        grado = Grado(grado=codigo, nombre=nombre)
        agregar_grado(grado)
    else:
        grado.nombre = nombre
        agregar_grado(grado)
    return grado
