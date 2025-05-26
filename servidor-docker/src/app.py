from flask import Flask, jsonify
from src.config import Config
from src.auth import auth
from app import db
from src import routes
import sys
import os

# Ajustamos el path para encontrar la app existente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Ruta principal con autenticación
    @app.route('/')
    @auth.login_required
    def index():
        return jsonify({
            "message": f"¡Bienvenido al sistema académico, {auth.current_user.username}!",
            "status": "active"
        })
    
    # Ruta para probar la conexión
    @app.route('/test')
    @auth.login_required
    def test_connection():
        return jsonify({
            "status": "ok", 
            "message": "Conexión establecida correctamente",
            "user": auth.current_user.username
        })
    
    # Registrar rutas
    for blueprint in routes.routes:
        app.register_blueprint(blueprint)
    
    # Crear base de datos si no existe
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))