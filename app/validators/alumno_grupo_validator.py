class AlumnoGrupoValidator:

    @staticmethod
    def validate_alumno_grupo(data):
        errors = []
        if not data.get('alumno_id'):
            errors.append('El alumno es obligatorio.')
        if not data.get('grupo_id'):
            errors.append('El grupo es obligatorio.')