from flask import Flask, request, jsonify, Response, Blueprint   
from encode_decode import JWT_Manager
from querys import DB_Manager

user_bp = Blueprint('user', __name__)
db_manager= DB_Manager()
jwt_manager = JWT_Manager()

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()  
    if(data.get('user') == None or data.get('password') == None or data.get('state')== None):
        return Response(status=400) 
    else:
        result = db_manager.insert_user(data.get('user'), data.get('password'), data.get('state'))

        token = jwt_manager.encode({"id": result["ID"],"state": result["state"]})
        print(f"{token}")
        return jsonify(token=token)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()  
    if(data.get('user') == None or data.get('password') == None):
        return Response("Usuario no registrado o datos incorrectos",status=400)
    else:
        result = db_manager.get_user(data.get('user'), data.get('password'))

        if(result == None):
            return Response(status=403)
        else:
            token = jwt_manager.encode({"id": result["ID"],"state": result["state"]})
        
            return jsonify(token=token)