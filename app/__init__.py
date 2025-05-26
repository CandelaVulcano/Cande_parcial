from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Crear instancia de la base de datos
db = SQLAlchemy()

def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Configurar la aplicación según el entorno
    if os.environ.get('FLASK_CONTEXT') == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    # Si hay configuración de prueba, aplicarla
    if test_config:
        app.config.update(test_config)
    
    # Inicializar extensiones con la aplicación
    db.init_app(app)
    
    # Asegurarse de que exista el directorio de instancia
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Configura rutas iniciales (opcional)
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app