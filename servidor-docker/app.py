from flask import Flask, jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy
import os
import sys

# Ajustamos el path para encontrar los módulos de la aplicación
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Inicializar Flask y extensiones
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Inicializar la base de datos
db = SQLAlchemy(app)

# Configurar autenticación
auth = HTTPBasicAuth()

# Usuarios predefinidos
class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

users = {
    "amigo1": User("amigo1", pwd_context.hash("clave1")),
    "amigo2": User("amigo2", pwd_context.hash("clave2")),
    "amigo3": User("amigo3", pwd_context.hash("clave3")),
    "amigo4": User("amigo4", pwd_context.hash("clave4")),
    "amigo5": User("amigo5", pwd_context.hash("clave5")),
    "amigo6": User("amigo6", pwd_context.hash("clave6"))
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        user = users.get(username)
        if pwd_context.verify(password, user.password_hash):
            return user
    return None

# Importar modelos y servicios
from app.models.facultad import Facultad
from app.services import FacultadService

# Crear blueprint para facultades
facultad_bp = Blueprint('facultad', __name__, url_prefix='/api/facultades')

@facultad_bp.route('', methods=['GET'])
@auth.login_required
def get_facultades():
    """Obtiene todas las facultades"""
    facultades = FacultadService.buscar_todos()
    return jsonify([{
        'id': f.id,
        'nombre': f.nombre,
        'abreviatura': f.abreviatura,
        'directorio': f.directorio,
        'sigla': f.sigla,
        'codigo_postal': f.codigo_postal,
        'ciudad': f.ciudad,
        'domicilio': f.domicilio,
        'telefono': f.telefono,
        'contacto': f.contacto,
        'email': f.email
    } for f in facultades])

@facultad_bp.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_facultad(id):
    """Obtiene una facultad por id"""
    facultad = FacultadService.buscar_por_id(id)
    if not facultad:
        return jsonify({'message': 'Facultad no encontrada'}), 404
    
    return jsonify({
        'id': facultad.id,
        'nombre': facultad.nombre,
        'abreviatura': facultad.abreviatura,
        'directorio': facultad.directorio,
        'sigla': facultad.sigla,
        'codigo_postal': facultad.codigo_postal,
        'ciudad': facultad.ciudad,
        'domicilio': facultad.domicilio,
        'telefono': facultad.telefono,
        'contacto': facultad.contacto,
        'email': facultad.email
    })

# Rutas principales de la API
@app.route('/')
@auth.login_required
def index():
    return jsonify({
        "message": f"¡Bienvenido al sistema académico!",
        "status": "active"
    })

@app.route('/test')
@auth.login_required
def test_connection():
    return jsonify({
        "status": "ok", 
        "message": "Conexión establecida correctamente",
        "user": auth.current_user().username
    })

# Registrar blueprints
app.register_blueprint(facultad_bp)

# Crear base de datos si no existe
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# Para uso con gunicorn
def create_app():
    return app