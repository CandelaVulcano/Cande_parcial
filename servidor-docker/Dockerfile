FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto completo
COPY . .

# Configurar variables de entorno
ENV PYTHONPATH=/app
ENV FLASK_APP=servidor-docker/app.py

# Exponer el puerto
EXPOSE 5000

# Comando simple para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "servidor-docker.app:app"]