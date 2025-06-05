from app.models.orientacion import Orientacion
from app.repositories.orientacion_repositorio import agregar_orientacion, obtener_orientacion_por_codigo

def crear_o_actualizar_orientacion(especialidad, plan, codigo, nombre):
    orientacion = obtener_orientacion_por_codigo(codigo)
    if not orientacion:
        orientacion = Orientacion(especialidad=especialidad, plan=plan, orientacion=codigo, nombre=nombre)
        agregar_orientacion(orientacion)
    else:
        orientacion.nombre = nombre
        agregar_orientacion(orientacion)
    return orientacion
