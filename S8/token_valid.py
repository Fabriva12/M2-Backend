from functools import wraps
from flask import request, Response
from encode_decode import JWT_Manager

jwt_manager = JWT_Manager()

def token_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return Response("Token requerido", status=403)
            
            decoded = jwt_manager.decode(token.replace("Bearer ", ""))
            if not decoded:
                return Response("Token inválido", status=403)

            return f(decoded=decoded, *args, **kwargs)
        return wrapper
    return decorator