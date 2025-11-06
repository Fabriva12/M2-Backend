from functools import wraps
from flask import request, Response
from jwt_manager_proyect import JWT_Manager

jwt_manager = JWT_Manager()

# creamos un decorador para validar el token del usuario
def token_required(role=None,test_decoded=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if test_decoded is not None:
                return f(decoded=test_decoded, *args, **kwargs)
            token = request.headers.get('Authorization')
            if not token:
                return Response("Token requerido", status=403)
            
            decoded = jwt_manager.decode(token.replace("Bearer ", ""))
            if not decoded:
                return Response("Token inválido", status=403)

            return f(decoded=decoded, *args, **kwargs)
        return wrapper
    return decorator