from flask import Flask, jsonify, request, Response
from encode_decode import JWT_Manager
from querys import DB_Manager
from token_valid import token_required
from redis_manager import CacheManager, redis_client
app = Flask("user-service")
jwt_manager = JWT_Manager()
db_manager = DB_Manager()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  
    if(data.get('user') == None or data.get('password') == None or data.get('state')== None):
        return Response(status=400) 
    else:
        result = db_manager.insert_user(data.get('user'), data.get('password'), data.get('state'))

        token = jwt_manager.encode({"id": result["ID"],"state": result["state"]})
        print(f"{token}")
        return jsonify(token=token)

@app.route('/login', methods=['POST'])
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

@app.route('/new_product', methods=['POST'])
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

@app.route('/see_products', methods =['GET','POST'])
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
    
@app.route('/buy', methods=['POST'])
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


@app.route('/update_product', methods=['PUT'])
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
    

@app.route('/delete_product', methods=['DELETE'])
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


@app.route('/bills', methods=['GET'])
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
    
    
@app.route('/delete_bills', methods=['DELETE'])
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


@app.route('/update_bill', methods=['PUT'])
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

if __name__ == "__main__":
    app.run(debug=True)