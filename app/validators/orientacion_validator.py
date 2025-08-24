class OrientacionValidator:
    @staticmethod
    def validate_orientacion(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre de la orientación es obligatorio.')
        if not data.get('plan_id'):
            errors.append('El ID de plan es obligatorio.')
        return errors
