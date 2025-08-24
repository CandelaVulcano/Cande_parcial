from functools import wraps
from flask import request, jsonify


def validate_with(schema_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Crea una instancia del esquema y valida los datos del request
                schema = schema_class()
                data = schema.load(request.get_json())
            except Exception as err:
                return jsonify({"error": str(err)}), 400
            # Si la validación es exitosa, continúa con la función original
            return func(data, *args, **kwargs)
        return wrapper
    return decorator
