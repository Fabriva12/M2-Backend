from ClassPgM import PgManager
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/user", methods=["POST"])
def create_user():
    db_manager = PgManager(
        dbname="postgres", user="postgres", password="postgres", host="localhost", port = "5432"
    )
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    name = data.get("name")
    birthdate = data.get("birthdate")
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    if not name or not birthdate or not email or not password or not username:
        return jsonify({"error": "Missing required fields "}), 400
        
    query = ("INSERT INTO lyfter_car_rental.users (name, birthdate, email, password, username, count_state) VALUES(%s,%s,%s,%s,%s,'active');")
    results = db_manager.execute_query(query, name, birthdate, email, password, username)
    db_manager.close_connection()
    return jsonify({"message": "Se agregó el nuevo usuario"})




@app.route("/car", methods=["POST"])
def create_car():
    db_manager = PgManager(
        dbname="postgres", user="postgres", password="postgres", host="localhost", port = "5432"
    )
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    Brand = data.get("Brand")
    Model = data.get("Model")
    Year = data.get("Year")
    if not Brand or not Model or not Year:
        return jsonify({"error": "Missing required fields "}), 400
    
    query = ("INSERT INTO lyfter_car_rental.Cars(Brand, Model, Year, State) values (%s, %s, %s, 'available');")
    results = db_manager.execute_query(query, Brand, Model, Year)
    db_manager.close_connection()
    return jsonify({"message": "Se agregó el vehiculo"})



@app.route("/rent_car", methods=["POST"])
def create_rent_car():
    db_manager = PgManager(
        dbname="postgres", user="postgres", password="postgres", host="localhost", port = "5432"
    )
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    User_ID = data.get("User_ID")
    Car_ID = data.get("Car_ID")
    State = data.get("State")
    if not User_ID or not Car_ID or not State:
        return jsonify({"error": "Missing required fields "}), 400
    
    query = ("INSERT INTO lyfter_car_rental.Rent_Cars(User_ID, Car_ID, State) VALUES(%s,%s,%s);")
    results = db_manager.execute_query(query, User_ID, Car_ID, State )
    db_manager.close_connection()
    return jsonify({"message": "Se agregó la nueva renta"})


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
