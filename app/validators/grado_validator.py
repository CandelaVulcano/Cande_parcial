class GradoValidator:

    @staticmethod
    def validate_grado(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        return errors