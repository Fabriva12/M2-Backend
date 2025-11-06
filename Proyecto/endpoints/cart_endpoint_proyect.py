from flask import Blueprint, request, jsonify, Response
from queries.cart_queries_proyect import Buy_DB
from token_valid import token_required
import traceback


cart_bp = Blueprint('cart', __name__)
db_manager= Buy_DB()



# Con la siguiente funcion creamos un endpoint para crear un nuevo carrito de compras 
@cart_bp.route('/new_cart', methods=['POST'])
@token_required()
def new_cart(decoded):
    try:
        if  not decoded['role']:
            return Response("No autorizado", status=403)
    
        data = request.get_json()
        if data is None:
            return jsonify({'message':'Invalid JSON', }),400
        user_ID= decoded.get('id')
        product_ID= data.get('product_ID')
        quantity=data.get('quantity')

        if not user_ID or not product_ID or not quantity:
            return jsonify({'message':'user_ID, product_ID and quantity are required'}),400
        else:
            db_manager.new_cart(user_ID, product_ID, quantity)
            return jsonify("carrito creado y producto añadido exitosamente"),201 
    except Exception as e:
        print("Error en /new_cart:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)
    
# Con esta funcion añadimos productos a un carrito existente



# Esta funcion permite ver los carritos de un usuario
@cart_bp.route('/my_carts', methods=['GET'])
@token_required()
def my_carts(decoded):
    try:
        if  not decoded['role']:
            return Response("No autorizado", status=403)
    
        user_ID= decoded.get('id')

        if not user_ID:
            return jsonify({'message':'user_ID is required'}),400
        else:
            my_carts = db_manager.see_my_carts(user_ID)
            return jsonify(my_carts),200
    except Exception as e:
        print("Error en /see_my_carts:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)


# Esta permite ver los items de un carrito
@cart_bp.route('/view_cart/', methods=['GET'])
@token_required()
def view_cart_items(decoded,):
    try:
        if  not decoded['role']:
            return Response("No autorizado", status=403)
        data = request.get_json()
        user_ID= decoded.get('id')
        cart_ID= data.get('cart_ID')

        if not user_ID or not cart_ID:
            return jsonify({'message':'user_ID and cart_ID are required'}),400
        else:
            cart_contents = db_manager.view_cart_items(cart_ID)
            return jsonify(cart_contents),200 
    except Exception as e:
        print("Error en /view_cart:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)

# Con esta funcion creamos un endpoint para comprar los carritos anteriormente creado
@cart_bp.route('/buy_cart', methods=['POST'])
@token_required()
def buy_cart(decoded):
    try:    
        if  not decoded['role']:
            return Response("No autorizado", status=403)
    
        data = request.get_json()
        if data is None:
            return jsonify({'message':'Invalid JSON', }),400
        user_ID= decoded.get('id')
        cart_ID= data.get('cart_ID')
        address= data.get('address')
        payment_method= data.get('payment_method')

        if not user_ID or not cart_ID or not address or not payment_method:
            return jsonify({'message':'user_ID cart_ID address and payment_method are required'}),400
        else:
            db_manager.buy_cart(user_ID, cart_ID, address, payment_method)
            return jsonify("compra realizada exitosamente"),201 
    except Exception as e:
        print("Error en /buy_cart:", e)
        traceback.print_exc()
        return Response("Error interno", status=500)