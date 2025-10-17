from flask import Flask, jsonify, request, Response,Blueprint
from product_endpoint import product_bp
from user_endpoint import user_bp
from bill_endpoint import bill_bp

app = Flask("user-service")
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(bill_bp)

if __name__ == "__main__":
    app.run(debug=True)