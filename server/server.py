from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/get_products', methods=['GET'])
def get_products():
    django_url = 'http://127.0.0.1:8000/api/products/'  
    response = requests.get(django_url)
    products = response.json()
    return jsonify(products)

@app.route('/get_product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    django_url = f'http://127.0.0.1:8000/api/products/{product_id}/'  
    response = requests.get(django_url)
    if response.status_code == 200:
        product = response.json()
        return jsonify(product)
    else:
        return f'Error al obtener el producto con ID {product_id}'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
