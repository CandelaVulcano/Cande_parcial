class MateriaValidator:
    @staticmethod
    def validate_materia(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre de la materia es obligatorio.')
        if not data.get('codigo'):
            errors.append('El código es obligatorio.')
        if not data.get('departamento_id'):
            errors.append('El ID de departamento es obligatorio.')
        return errors
