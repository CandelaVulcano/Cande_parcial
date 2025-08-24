class InscripcionValidator:
    @staticmethod
    def validate_inscripcion(data):
        errors = []
        if not data.get('alumno_id'):
            errors.append('El ID de alumno es obligatorio.')
        if not data.get('materia_id'):
            errors.append('El ID de materia es obligatorio.')
        if not data.get('fecha'):
            errors.append('La fecha es obligatoria.')
        return errors
