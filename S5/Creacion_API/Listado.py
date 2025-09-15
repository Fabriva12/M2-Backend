from ClassPgM import PgManager
from flask import Flask,jsonify, request

app = Flask(__name__)

db_manager = PgManager(
        dbname="postgres", user="postgres", password="postgres", host="localhost", port = "5432"
        )
@app.route("/select_user", methods=["GET"])
def select_user():

    filters = request.args
    query = ("SELECT * FROM lyfter_car_rental.users")
    params = []
    if filters:
        conditions = []
        for key, value in filters.items():
            conditions.append(f"{key} = %s")
            params.append(value)
        query += " WHERE " + " AND ".join(conditions)
        results = db_manager.execute_query(query, *params)
        db_manager.close_connection()
    return jsonify(f"{results}")


if __name__ == "__main__":
    app.run(host="localhost", debug=True)