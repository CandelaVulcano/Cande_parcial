class TipoDocumentoValidator:

    @staticmethod
    def validate_tipo_documento(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        return errors
