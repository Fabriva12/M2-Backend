from flask import Flask
from endpoints.user_endpoint_proyect import user_bp
from endpoints.product_endpoint_proyect import product_bp
from endpoints.cart_endpoint_proyect import cart_bp
from endpoints.bill_endpoint_proyect import bill_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(product_bp, url_prefix='/product')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(bill_bp, url_prefix='/bill')

if __name__ == "__main__":
    app.run(debug=True)