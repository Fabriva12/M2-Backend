from flask import request, jsonify, Response,Blueprint
from queries.product_queries_proyect import Product_DB
from token_valid import token_required
from redis_manager import CacheManager
import traceback

product_bp = Blueprint('product', __name__)
db_manager= Product_DB()




# Con la siguiente funcion creamos un endpoint para registrar productos
@product_bp.route('/new_product', methods=['POST'])
@token_required()
def new_product(decoded):
    try:
        if decoded['role'] != 'admin':
            return Response("No autorizado", status=403)
    
        data = request.get_json()
        if data is None:
            return jsonify({'message':'Invalid JSON'}),400
        name= data.get('name')
        SKU= data.get('SKU')
        price=data.get('price')
        stock=data.get('stock')

        if not name or not SKU or not price or not stock:
            return jsonify({'message':'name, SKU, price and stock are required'}),400
        else:
            db_manager.insert_product(data.get('name'), data.get('SKU'), data.get('price'), data.get('stock'))
            return jsonify("producto registrado exitosamente"),201 
    except Exception as e:
        print("Error en /new_product:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)

# Con esta funcion permite ver productos y los almacena en la cache
@product_bp.route('/see_product', methods=['GET'])
@token_required()
def see_product(decoded):
    try:
        if decoded.get("role") not in ["admin", "user"]:
            return Response("No autorizado", status=403)

        data = request.get_json()
        if data is None or "ID" not in data:
            return jsonify({'message':' ID is required'}),400

        product_ID = data.get('ID')
        entity_type= 'producto'
        cached_product = CacheManager.get_data(entity_type ,product_ID)
        if cached_product:
            return jsonify(cached_product), 200

        product = db_manager.get_product(product_ID)
        if product is None:
            return Response("Producto no encontrado", status=404)

        CacheManager.store_data(entity_type,product)
        return jsonify(product), 200
    except Exception as e:
        import traceback
        print("Error en /see_product:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)

# Esta funcion elimina un producto de la base de datos y tambien de la cache
@product_bp.route('/delete_product', methods=['DELETE'])
@token_required()
def delete_product(decoded):
    try:
        if decoded.get("role") != "admin":
            return Response("No autorizado", status=403)

        data = request.get_json()
        if data is None or "ID" not in data:
            return jsonify({'message':'ID is required'}),400

        product_ID = data.get('ID')
        entity_type= "producto"
        db_manager.delete_product(product_ID)
        CacheManager.delete_data(entity_type, product_ID)
        return jsonify({"success": True, "message": "Producto eliminado correctamente"}), 200
    except Exception as e:
        print("Error en /delete_product:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)
    

# Con la siguiente funcion creamos un endpoint para actualizar productos y los eliminados de la cache
@product_bp.route('/upgrade_product', methods=['PUT'])
@token_required()
def upgrade_product(decoded):
    try:
        if decoded.get("role") != "admin":
            return Response("No autorizado", status=403)
        data = request.get_json()
        
        if data is None or "ID" not in data:
            return jsonify({'message':'ID es requerido'}),400

        product_ID = data.get('ID')
        entity_type = "producto"
        update_data = {
            k: v for k, v in data.items()
            if k in {"name", "SKU", "price", "stock"} and v is not None
        }

        if not update_data:
            return jsonify({"message": "No se proporcionaron campos válidos para actualizar"}), 400
        db_manager.update_product(product_ID, update_data)
        CacheManager.delete_data(entity_type, product_ID)
        return jsonify({"success": True, "message": "Producto actualizado correctamente"}), 200
    except Exception as e:
        print("Error en /upgrade_product:", e)
        traceback.print_exc()
        return Response("Error interno", status=500) 