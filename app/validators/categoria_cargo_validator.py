
class CategoriaCargoValidator:

    @staticmethod
    def validate_categoria_cargo(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        return errors