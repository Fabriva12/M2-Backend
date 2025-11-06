from flask import request, jsonify, Response,Blueprint
from queries.user_queries_proyect import User_DB
from jwt_manager_proyect import JWT_Manager
from token_valid import token_required
import traceback


user_bp = Blueprint('user', __name__)
db_manager= User_DB()
jwt_manager= JWT_Manager()



# Con la siguiente funcion creamos un endpoint para registrar usuarios 
@user_bp.route('/register', methods=['POST'])
def register():
    try:

        data = request.get_json()  
        if not data.get('email') or not data.get('password')or not data.get('role'):
            return jsonify({"error":"datos incorrectos ingrese email, password y role"}),400 
        
        db_manager.insert_user(data.get('email'), data.get('password'), data.get('role'))
        return jsonify("usuario registrado exitosamente"),200
    
    except Exception as e:
        print("Error en /register:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)


# Con la siguiente fucion creamos un endpoint para loguear usuarios lo que nos devuelve un token necesario para acceder a los demas endpoints
@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"error":"datos incorrectos ingrese email y password"}),400
        
        result = db_manager.get_user(data.get('email'), data.get('password'))
        if result == None:
                return jsonify({"error":"Usuario no registrado"}),401 
        
        token = jwt_manager.encode({"id": result["ID"],"role": result["role"]})
        return jsonify(token=token)
    except Exception as e:
        print("Error en /login:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)

# Esta funcion elimina un usuario de la base de datos
@user_bp.route('/delete', methods=['DELETE']) 
@token_required()
def delete_user(decoded):
    try:
        if  not decoded['role']== 'admin':
            return Response("No autorizado", status=403)
        data = request.get_json()
        if data is None or "ID" not in data:
            return jsonify({'message':'ID is required'}),403
        user_ID = data.get('ID')
        db_manager.delete_user(user_ID)
        return jsonify("usuario eliminado exitosamente"),200
    except Exception as e:
        print("Error en /delete_user:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)