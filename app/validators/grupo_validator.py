class GrupoValidator:
    @staticmethod
    def validate_grupo(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre del grupo es obligatorio.')
        return errors
