class TipoEspecialidadValidator:

    @staticmethod
    def validate_tipo_especialidad(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        if not data.get('nivel'):
            errors.append('El nivel es obligatorio.')
        return errors