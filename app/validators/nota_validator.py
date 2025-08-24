class NotaValidator:
    @staticmethod
    def validate_nota(data):
        errors = []
        valor = data.get('valor')
        if valor is None:
            errors.append('El valor de la nota es obligatorio.')
        elif not (1 <= valor <= 10):
            errors.append('La nota debe estar entre 1 y 10.')
        if not data.get('inscripcion_id'):
            errors.append('El ID de inscripción es obligatorio.')
        return errors
