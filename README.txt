# Proyecto DDS

Este proyecto es una aplicación para la gestión académica, desarrollada en Python. Incluye modelos, repositorios, servicios y pruebas automatizadas.

## Estructura del proyecto

- **app/**: Código principal de la aplicación.
  - **models/**: Definición de modelos de datos (Alumno, Materia, etc).
  - **repositories/**: Acceso y manipulación de datos.
  - **mapping/**: Mapeo de entidades.
  - **config/**: Configuración de la aplicación.
  - **resources/**, **services/**, **static/**, **templates/**, **validators/**: Recursos adicionales, servicios, archivos estáticos, plantillas y validadores.
- **servidor-docker/**: Archivos para despliegue con Docker.
- **test/**: Pruebas unitarias y de integración.
- **requirements.txt**: Dependencias del proyecto.
- **install.py**: Script de instalación.

## Requisitos previos

- Python 3.8 o superior
- Docker (opcional, para despliegue)
- Instalar dependencias con:
  ```
  pip install -r requirements.txt
  ```

## Instalación y ejecución

1. Clona el repositorio.
2. Instala las dependencias.
3. Ejecuta la aplicación principal:
   ```
   python app/__init__.py
   ```
   O usa Docker:
   ```
   cd servidor-docker
   docker-compose up
   ```

## Pruebas

Para ejecutar los tests:
```
python -m unittest discover test
```

## Alumnos
- Alonso Adriel
- Bettiol Giuliana
- Martinez Jimena
- Ruiz Alejandro
- Sanchez Juan
- Velazco Franco
- Vulcano Candela

## Licencia
Este proyecto es de uso académico.
