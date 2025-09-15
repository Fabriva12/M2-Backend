from ClassPgM import PgManager
from flask import Flask, jsonify,request

app = Flask(__name__)

db_manager = PgManager(
        dbname="postgres", user="postgres", password="postgres", host="localhost", port = "5432"
    )

@app.route("/state_car", methods=["PUT"])
def update_car():
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    state = data.get("state")
    ID = data.get("ID")
    
    if not state or not ID:
        return jsonify({"error": "Missing required fields "}), 400
        
    query = ("UPDATE lyfter_car_rental.cars SET state = %s Where ID =%s;")
    results = db_manager.execute_query(query, state, ID )
    db_manager.close_connection()
    return jsonify({"message": f"Se cambio el estado a {state} del carro {ID}"})


@app.route("/state_user", methods=["PUT"])
def update_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    count_state = data.get("count_state")
    ID = data.get("ID")
    
    if not count_state or not ID:
        return jsonify({"error": "Missing required fields "}), 400
        
    query = ("UPDATE lyfter_car_rental.users SET count_state = %s Where ID =%s;")
    results = db_manager.execute_query(query, count_state, ID )
    db_manager.close_connection()
    return jsonify({"message": f"Se cambio a {count_state} el estado del usuario {ID}"})

@app.route("/completed_rent", methods=["PUT"])
def completed_rent():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    ID = data.get("ID")
    
    if not ID:
        return jsonify({"error": "Missing required fields "}), 400
        
    query = ("UPDATE lyfter_car_rental.rent_cars SET state = 'completed' Where ID =%s;")
    results = db_manager.execute_query(query, ID )
    db_manager.close_connection()
    return jsonify({"message": f"Renta {ID} completada"})



@app.route("/state_rent", methods=["PUT"])
def update_rent_cars():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    ID = data.get("ID")
    state = data.get ("state")
    if not ID or not state:
        return jsonify({"error": "Missing required fields "}), 400
        
    query = ("UPDATE lyfter_car_rental.rent_cars SET state = %s Where ID =%s;")
    results = db_manager.execute_query(query, ID, state )
    db_manager.close_connection()
    return jsonify({"message": f"Se actualizo a {state} la renta {ID}"})



@app.route("/defaulter_user", methods=["PUT"])
def defaulter_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    ID = data.get("ID")
    
    if not ID:
        return jsonify({"error": "Missing required fields "}), 400
        
    query = ("UPDATE lyfter_car_rental.users SET count_state = 'defaulter' Where ID =%s;")
    results = db_manager.execute_query(query, ID )
    db_manager.close_connection()
    return jsonify({"message": f"El usuario {ID} esta moroso"})

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
