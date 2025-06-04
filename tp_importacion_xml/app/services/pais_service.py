from app.models.pais import Pais
from app.repositories.pais_repositorio import agregar_pais, obtener_pais_por_codigo

def crear_o_actualizar_pais(codigo, nombre):
    pais = obtener_pais_por_codigo(codigo)
    if not pais:
        pais = Pais(pais=codigo, nombre=nombre)
        agregar_pais(pais)
    else:
        pais.nombre = nombre
        agregar_pais(pais)
    return pais
