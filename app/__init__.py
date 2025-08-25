import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_hashids import Hashids

from .config import config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name=None) -> None:
    config_name = config_name or os.getenv('FLASK_ENV') or 'development'
    app = Flask(__name__)
    config_class = config.get(config_name, config['default'])
    app.config.from_object(config_class)
    db.init_app(app)
    ma.init_app(app)

    from app.resources import home_bp, universidad_bp, departamento_bp, cargo_bp, categoria_cargo_bp, autoridad_bp
    from app.resources import grupo_blueprint, tipo_documento_blueprint, materia_blueprint, orientacion_blueprint
    from app.resources import especialidad_bp, plan_bp, grado_bp, certificado_bp, alumno_bp
    from app.resources import inscripcion_bp, cursada_bp, evaluacion_bp, nota_bp, area_bp, facultad_bp
    app.register_blueprint(home_bp, url_prefix='/api/v1')
    app.register_blueprint(universidad_bp, url_prefix='/api/v1')
    app.register_blueprint(departamento_bp, url_prefix='/api/v1')
    app.register_blueprint(cargo_bp, url_prefix='/api/v1')
    app.register_blueprint(categoria_cargo_bp, url_prefix='/api/v1')
    app.register_blueprint(autoridad_bp, url_prefix='/api/v1')
    app.register_blueprint(grupo_blueprint, url_prefix='/api/v1')
    app.register_blueprint(tipo_documento_blueprint, url_prefix='/api/v1')
    app.register_blueprint(materia_blueprint, url_prefix='/api/v1')
    app.register_blueprint(orientacion_blueprint, url_prefix='/api/v1')
    app.register_blueprint(especialidad_bp, url_prefix='/api/v1')
    app.register_blueprint(plan_bp, url_prefix='/api/v1')
    app.register_blueprint(grado_bp, url_prefix='/api/v1')
    app.register_blueprint(certificado_bp, url_prefix='/api/v1')
    app.register_blueprint(alumno_bp, url_prefix='/api/v1')
    app.register_blueprint(inscripcion_bp, url_prefix='/api/v1')
    app.register_blueprint(cursada_bp, url_prefix='/api/v1')
    app.register_blueprint(evaluacion_bp, url_prefix='/api/v1')
    app.register_blueprint(nota_bp, url_prefix='/api/v1')
    app.register_blueprint(facultad_bp, url_prefix='/api/v1')
    app.register_blueprint(area_bp, url_prefix='/api/v1')

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
            'db': db
        }

    return app
