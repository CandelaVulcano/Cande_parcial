# Trabajo Práctico: Importación de XML - SYSACAD

## Descripción
Este proyecto importa datos desde archivos XML (grados, universidad, facultades, materias, localidades, especialidades, orientaciones, planes, países) a una base de datos PostgreSQL usando SQLAlchemy y lxml.

## Estructura
- `app/` : Modelos, repositorios y servicios.
- `archivos_xml/` : Archivos XML a importar.
- `importar_todos.py` : Script principal de importación.
- `main.py` : Ejecuta la importación completa.
- `requirements.txt` : Dependencias Python.
- `docker-compose.yml` : Levanta la base de datos PostgreSQL.

## Uso
1. Levanta la base de datos:
   ```powershell
   docker-compose up -d
   ```
2. Instala dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Ejecuta la importación:
   ```powershell
   python main.py
   ```

## Tests
Los tests se encuentran en la carpeta `tests/` y pueden ejecutarse con:
```powershell
python -m unittest discover tests
```

## Consideraciones
- Los XML deben estar en `archivos_xml/` y codificados en Windows-1252.
- Cada registro importado tiene un identificador único.
- El código sigue principios de código limpio y es fácilmente extensible.

## Autor
Franco
