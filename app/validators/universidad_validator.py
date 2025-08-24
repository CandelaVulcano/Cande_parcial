class UniversidadValidator:

    @staticmethod
    def validate_universidad(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        if not data.get('sigla'):
            errors.append('La sigla es obligatoria.')
        return errors
