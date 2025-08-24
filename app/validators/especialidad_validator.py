class EspecialidadValidator:
    @staticmethod
    def validate_especialidad(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre de la especialidad es obligatorio.')
        if not data.get('tipo_especialidad_id'):
            errors.append('El ID de tipo de especialidad es obligatorio.')
        return errors
