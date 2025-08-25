class DepartamentoValidator:
    @staticmethod
    def validate_departamento(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre del departamento es obligatorio.')
        if not data.get('facultad_id'):
            errors.append('El ID de facultad es obligatorio.')
        return errors
