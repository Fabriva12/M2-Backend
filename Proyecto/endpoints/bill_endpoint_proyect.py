from flask import Blueprint, request, jsonify, Response
from queries.bill_queries_proyect import Bill_DB
from token_valid import token_required
import traceback


bill_bp = Blueprint('bill', __name__)
db_manager= Bill_DB()

# Con la siguiente funcion creamos un endpoint para ver una factura despues de una compra
@bill_bp.route('/view_bill', methods=['POST'])
@token_required()
def view_bills(decoded):
    try:
        if  not decoded['role']:
            return Response("No autorizado", status=403)
        if decoded['role'] == 'user':
            data = request.get_json()
            user_ID= decoded.get('id')
            cart_ID= data.get('cart_ID')
            result = db_manager.view_bills(user_ID, cart_ID)
            return jsonify(f"{result}"),200
        elif decoded['role'] == 'admin':
            data = request.get_json()
            user_ID= data.get('bill_ID')
            cart_ID= data.get('cart_ID')
            result = db_manager.view_bills(user_ID, cart_ID)
            return jsonify(f"{result}"),200
    except Exception as e:
        print("Error en /view_bill:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)

# con la siguiente funcion creamos un endpoint pata retornar facturas
@bill_bp.route('/return_bill', methods=['POST'])
@token_required()
def return_bill(decoded):
    try:
        if  not decoded['role']== 'admin':
            return Response("No autorizado", status=403)
        data= request.get_json()
        bill_ID= data.get('bill_ID')
        result =db_manager.return_bill(bill_ID)
        return jsonify(f"{result}"),200
    
    except Exception as e:
        print("Error en /return_bill:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)
