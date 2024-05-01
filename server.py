# server.py
"""
 flask app that executes a CRUD operation from a python dict
"""

import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from product import products


app = Flask("Product Server")
CORS(app)


# Example request - http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    """
    function that returns a python dictionary with a list of products
    """
    return jsonify(products)


# Example request - http://localhost:5000/products/144 - with method GET
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    """
    function that executes a GET request to get the product ID
    """
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)


# Example request - http://localhost:5000/products - with method POST
@app.route('/products', methods=['POST'])
def add_product():
    """
    function that adds a product
    """
    products.append(request.get_json())
    return '', 201

# Example request - http://localhost:5000/products/144 - with method PUT
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    """
    function that updates a product
    """
    id = int(id)
    product_update = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in product_update.items():
        product[key] = value
    return '', 204


# Example request - http://localhost:5000/products/144 - with method DELETE
@app.route('/products/<id>', methods=['DELETE'])
def remove_product(id):
    """
    function that deletes a product
    """
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204


if __name__=="__main__":
    app.run(debug=True)
# When no port is specified, starts at default port 5000
