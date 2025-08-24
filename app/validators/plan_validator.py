class PlanValidator:
    @staticmethod
    def validate_plan(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre del plan es obligatorio.')
        if not data.get('fecha_inicio'):
            errors.append('La fecha de inicio es obligatoria.')
        if not data.get('orientacion_id'):
            errors.append('El ID de orientación es obligatorio.')
        return errors
