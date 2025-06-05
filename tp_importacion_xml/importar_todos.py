import os
from lxml import etree
from app.services.pais_service import crear_o_actualizar_pais
from app.services.localidad_service import crear_o_actualizar_localidad
from app.services.grado_service import crear_o_actualizar_grado
from app.services.facultad_service import crear_o_actualizar_facultad
from app.services.universidad_service import crear_o_actualizar_universidad
from app.services.materia_service import crear_o_actualizar_materia
from app.services.especialidad_service import crear_o_actualizar_especialidad
from app.services.orientacion_service import crear_o_actualizar_orientacion
from app.services.plan_service import crear_o_actualizar_plan
from app.models.base import Base
from app.repositories.session import engine

# Crear tablas si no existen
Base.metadata.create_all(engine)

# --- Importar Países ---
def importar_paises():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'paises.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        codigo = int(elem.findtext('pais'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_pais(codigo, nombre)
    print('Países importados')

# --- Importar Localidades ---
def importar_localidades():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'localidades.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_exportar'):
        codigo = int(elem.findtext('codigo'))
        ciudad = elem.findtext('ciudad')
        provincia = elem.findtext('provincia')
        pais_del_c = elem.findtext('pais_del_c')
        crear_o_actualizar_localidad(codigo, ciudad, provincia, pais_del_c)
    print('Localidades importadas')

def importar_grados():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'grados.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        codigo = int(elem.findtext('grado'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_grado(codigo, nombre)
    print('Grados importados')

def importar_facultades():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'facultades.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        codigo = int(elem.findtext('facultad'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_facultad(codigo, nombre)
    print('Facultades importadas')

def importar_universidades():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'universidad.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        codigo = int(elem.findtext('universida'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_universidad(codigo, nombre)
    print('Universidades importadas')

def importar_materias():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'materias.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        especialidad = int(elem.findtext('especialidad'))
        plan = int(elem.findtext('plan'))
        codigo = int(elem.findtext('materia'))
        nombre = elem.findtext('nombre')
        ano_text = elem.findtext('ano')
        try:
            ano = int(ano_text)
        except (TypeError, ValueError):
            ano = None
        crear_o_actualizar_materia(especialidad, plan, codigo, nombre, ano)
    print('Materias importadas')

def importar_especialidades():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'especialidades.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        codigo = int(elem.findtext('especialidad'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_especialidad(codigo, nombre)
    print('Especialidades importadas')

def importar_orientaciones():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'orientaciones.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        especialidad = int(elem.findtext('especialidad'))
        plan = int(elem.findtext('plan'))
        codigo = int(elem.findtext('orientacion'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_orientacion(especialidad, plan, codigo, nombre)
    print('Orientaciones importadas')

def importar_planes():
    xml_path = os.path.join(os.path.dirname(__file__), 'archivos_xml', 'planes.xml')
    parser = etree.XMLParser(encoding='Windows-1252')
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()
    for elem in root.findall('.//_expxml'):
        especialidad = int(elem.findtext('especialidad'))
        codigo = int(elem.findtext('plan'))
        nombre = elem.findtext('nombre')
        crear_o_actualizar_plan(especialidad, codigo, nombre)
    print('Planes importados')

if __name__ == '__main__':
    importar_paises()
    importar_localidades()
    importar_grados()
    importar_facultades()
    importar_universidades()
    importar_materias()
    importar_especialidades()
    importar_orientaciones()
    importar_planes()
