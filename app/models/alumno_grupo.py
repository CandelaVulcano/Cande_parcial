from app import db

alumno_grupo = db.Table(
    'alumno_grupo',
    db.Column('alumno_id', db.Integer, db.ForeignKey(
        'alumnos.id'), primary_key=True),
    db.Column('grupo_id', db.Integer, db.ForeignKey(
        'grupos.id'), primary_key=True)
)
