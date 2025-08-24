class FacultadValidator:
    @staticmethod
    def validate_facultad(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre de la facultad es obligatorio.')
        if not data.get('codigo'):
            errors.append('El código de la facultad es obligatorio.')
    
        return errors