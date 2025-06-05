from app.models.universidad import Universidad
from app.repositories.universidad_repositorio import agregar_universidad, obtener_universidad_por_codigo

def crear_o_actualizar_universidad(codigo, nombre):
    universidad = obtener_universidad_por_codigo(codigo)
    if not universidad:
        universidad = Universidad(universida=codigo, nombre=nombre)
        agregar_universidad(universidad)
    else:
        universidad.nombre = nombre
        agregar_universidad(universidad)
    return universidad
