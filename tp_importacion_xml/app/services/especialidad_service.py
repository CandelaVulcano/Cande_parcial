from app.models.especialidad import Especialidad
from app.repositories.especialidad_repositorio import agregar_especialidad, obtener_especialidad_por_codigo

def crear_o_actualizar_especialidad(codigo, nombre):
    especialidad = obtener_especialidad_por_codigo(codigo)
    if not especialidad:
        especialidad = Especialidad(especialidad=codigo, nombre=nombre)
        agregar_especialidad(especialidad)
    else:
        especialidad.nombre = nombre
        agregar_especialidad(especialidad)
    return especialidad
