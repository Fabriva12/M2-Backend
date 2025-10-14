from flask import Flask, request, jsonify, Response,Blueprint
from encode_decode import token_required
from querys import DB_Manager
from redis_manager import CacheManager

db_manager = DB_Manager()
bill_bp = Blueprint('bill', __name__)

@bill_bp.route('/bills', methods=['GET'])
@token_required()
def get_bills(decoded):
    try:
        if decoded.get("state") == "admin":
            result=db_manager.get_bills()
            return jsonify(result)
        user_ID = decoded.get("id")
        if decoded.get("state") == "client":
            result=db_manager.get_bills_by_ID(user_ID)
            return jsonify(result)
    except Exception as e:
        import traceback
        print("Error en /get_bills:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)
    
    
@bill_bp.route('/delete_bills', methods=['DELETE'])
@token_required()
def delete_bills(decoded):
    try:
        if decoded.get("state") != "admin":
            return Response("No autorizado", status=403)

        data = request.get_json()
        if not data or "user_ID" not in data:
            return Response("Datos incompletos", status=400)
        user_ID = data["user_ID"]
        db_manager.delete_bills(user_ID)
        return jsonify({"success": True, "message": "Facturas eliminadas correctamente"})

    except Exception as e:
        return Response("Error interno", status=500) 


@bill_bp.route('/update_bill', methods=['PUT'])
@token_required()
def return_bill(decoded):
    try:
        if decoded.get("state") != "admin":
            return Response("No autorizado", status=403)

        data = request.get_json()
        if not data or "ID" not in data or "product_ID" not in data:
            return Response("Datos incompletos", status=400)
        bill_ID = data["ID"]
        product_ID = data["product_ID"]
        
        db_manager.return_bill(product_ID,bill_ID)
        CacheManager.delete_data(product_ID)
        return jsonify({"success": True, "message": "Factura actualizada correctamente"})

    except Exception as e:
        return Response("Error interno", status=500)