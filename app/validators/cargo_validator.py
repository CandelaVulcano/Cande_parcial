class CargoValidator:

    @staticmethod
    def validate_cargo(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        if not data.get('puntos'):
            errors.append('Los puntos son obligatorios.')
        if not data.get('categoria_cargo_id'):
            errors.append('La categoría de cargo es obligatoria.')
        if not data.get('tipo_dedicacion_id'):
            errors.append('El tipo de dedicación es obligatorio.')
        return errors