from flask import Flask, request, jsonify, Response, Blueprint
from encode_decode import token_required
from querys import DB_Manager
from redis_manager import CacheManager

db_manager = DB_Manager()
product_bp = Blueprint('product', __name__)


@product_bp.route('/new_product', methods=['POST'])
@token_required()
def new_product(decoded):
    try:
        if decoded.get("state") != "admin":
            return Response("No autorizado", status=403)

        data = request.get_json()
        if not data or "name" not in data or "price" not in data or "stock" not in data:
            return Response("Datos incompletos", status=400)

        db_manager.insert_product(data["name"],data["price"],data["stock"])
        return jsonify({"success": True, "message": "Producto agregado correctamente"})

    except Exception as e:
        import traceback
        print("Error en /new_product:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)

@product_bp.route('/see_products', methods =['GET','POST'])
@token_required()
def see_products(decoded):
    try:
        if decoded.get("state") == False:
            return Response("No estas registrado", status=403)
        data = request.get_json()
        if not data or "ID" not in data:
            return Response("Necesitas el ID del producto" , status=400)
        product_ID=  data["ID"] 
        product= CacheManager.get_data(product_ID)
        if product is None:
            product = db_manager.get_product(product_ID)
            CacheManager.store_data(product)
            if product is None:
                return Response("Producto no encontrado", status=404)
        return jsonify(product)

    except Exception as e:
        import traceback
        print("Error en /market:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)
    
@product_bp.route('/buy', methods=['POST'])
@token_required()
def buy_product(decoded):
    try:
        if decoded.get("state") == False:
            return Response("No estas registrado", status=403)
        user_ID = decoded.get("id")

        data= request.get_json()
        if not data or "ID" not in data or "quantity" not in data:
            return Response("Necesitas el ID y cantidad del producto", status=400)
        product_ID=  data["ID"]
        quantity= data["quantity"]
        db_manager.buy(user_ID,product_ID,quantity)
        return jsonify("compra realizada")
    
    except Exception as e:
        import traceback
        print("Error en /buy_product:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)


@product_bp.route('/update_product', methods=['PUT'])
@token_required()
def update_product(decoded):
    try:
        if decoded.get("state") != "admin":
            return Response("No autorizado", status=403)

        data = request.get_json()
        if not data or "ID" not in data:
            return Response("Datos incompletos", status=400)
        product_ID = data["ID"]
        db_manager.update_product(product_ID, data)
        CacheManager.delete_data(product_ID)
        return jsonify({"success": True, "message": "Producto actualizado correctamente"})

    except Exception as e:
        return Response("Error interno", status=500)
    

@product_bp.route('/delete_product', methods=['DELETE'])
@token_required()
def delete_product(decoded):
    try:
        if decoded.get("state") != "admin":
            return Response("No autorizado", status=403)

        data = request.get_json()
        if not data or "ID" not in data:
            return Response("Datos incompletos", status=400)
        product_ID = data["ID"]
        db_manager.delete_product(product_ID)
        CacheManager.delete_data(product_ID)
        return jsonify({"success": True, "message": "Producto eliminado correctamente"})

    except Exception as e:
        return Response("Error interno", status=500)
