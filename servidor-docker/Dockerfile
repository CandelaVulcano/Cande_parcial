FROM python:3.9-slim

WORKDIR /app

# Copiar los requisitos y instalarlos primero para aprovechar la caché de Docker
COPY servidor-docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Configurar variables de entorno
ENV PYTHONPATH=/app
ENV FLASK_APP=servidor-docker/src/app.py

# Exponer el puerto
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "servidor-docker.src.app:create_app()"]