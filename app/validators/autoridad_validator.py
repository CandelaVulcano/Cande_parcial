class AutoridadValidator:

    @staticmethod
    def validate_autoridad(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        if not data.get('cargo'):
            errors.append('El cargo es obligatorio.')
        if not data.get('email'):
            errors.append('El email es obligatorio.')
        if not data.get('facultad_id'):
            errors.append('La facultad es obligatoria.')
        return errors