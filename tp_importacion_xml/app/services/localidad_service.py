from app.models.localidad import Localidad
from app.repositories.localidad_repositorio import agregar_localidad, obtener_localidad_por_codigo

def crear_o_actualizar_localidad(codigo, ciudad, provincia, pais_del_c):
    localidad = obtener_localidad_por_codigo(codigo)
    if not localidad:
        localidad = Localidad(codigo=codigo, ciudad=ciudad, provincia=provincia, pais_del_c=pais_del_c)
        agregar_localidad(localidad)
    else:
        localidad.ciudad = ciudad
        localidad.provincia = provincia
        localidad.pais_del_c = pais_del_c
        agregar_localidad(localidad)
    return localidad
