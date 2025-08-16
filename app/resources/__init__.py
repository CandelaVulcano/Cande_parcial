from .certificado_resource import certificado_bp
from .alumno_resource import alumno_bp
from .inscripcion_resource import inscripcion_bp
from .cursada_resource import cursada_bp
from .evaluacion_resource import evaluacion_bp
from .nota_resource import nota_bp
from .facultad_resource import facultad_bp
from .area_resource import area_bp

def register_resources(app):
    app.register_blueprint(certificado_bp)
    app.register_blueprint(alumno_bp)
    app.register_blueprint(inscripcion_bp)
    app.register_blueprint(cursada_bp)
    app.register_blueprint(evaluacion_bp)
    app.register_blueprint(nota_bp)
    app.register_blueprint(facultad_bp)
    app.register_blueprint(area_bp)
