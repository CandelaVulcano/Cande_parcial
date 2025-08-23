from .alumno_resource import alumno_bp
from .area_resource import area_bp
from .autoridad_resource import autoridad_bp
from .cargo_resource import cargo_bp
from .categoria_cargo_resource import categoria_cargo_bp
from .certificado_resource import certificado_bp
from .cursada_resource import cursada_bp
from .departamento_resource import departamento_bp
from .especialidad_resource import especialidad_bp
from .evaluacion_resource import evaluacion_bp
from .facultad_resource import facultad_bp
from .grado_resource import grado_bp
from .grupo_resource import grupo_blueprint
from .home import home_bp
from .inscripcion_resource import inscripcion_bp
from .materia_resource import materia_blueprint
from .nota_resource import nota_bp
from .orientacion_resource import orientacion_blueprint
from .plan_resource import plan_bp
from .tipo_documento_resource import tipo_documento_blueprint
from .universidad_resource import universidad_bp


def register_resources(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(universidad_bp)
    app.register_blueprint(departamento_bp)
    app.register_blueprint(cargo_bp)
    app.register_blueprint(categoria_cargo_bp)
    app.register_blueprint(autoridad_bp)
    app.register_blueprint(grupo_blueprint)
    app.register_blueprint(tipo_documento_blueprint)
    app.register_blueprint(materia_blueprint)
    app.register_blueprint(orientacion_blueprint)
    app.register_blueprint(especialidad_bp)
    app.register_blueprint(plan_bp)
    app.register_blueprint(grado_bp)
    app.register_blueprint(certificado_bp)
    app.register_blueprint(alumno_bp)
    app.register_blueprint(inscripcion_bp)
    app.register_blueprint(cursada_bp)
    app.register_blueprint(evaluacion_bp)
    app.register_blueprint(nota_bp)
    app.register_blueprint(facultad_bp)
    app.register_blueprint(area_bp)
