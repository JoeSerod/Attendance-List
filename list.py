import os
import requests
import json
from models.response import Response
from models.product import Product
from flask import Flask, request, jsonify, render_template, redirect, url_for
from configuration.firebase_manager import FireStoreService


headers = {'Content-Type': "application/json", 'Accept': "application/json"}
app = Flask(__name__)
fb_service = FireStoreService()


@app.route('/', methods=["GET", "POST"])
def index():
    """
    View for the landing page.
    :return: redirection to product listings.
    """
    return render_template("index.html")


@app.route('/product/create', methods=["GET", "POST"])
def create_product():
    if request.method == "GET":

        return render_template("create_product.html")
    if request.method == "POST":
        form = request.form
        new_product = Product(form['product_name'], form['id'],
                              form['product_details'], form['price'])
        print(new_product)
        res = requests.post("http://localhost:5000/api/product/create",
                            json=new_product.__dict__, headers=headers).json()
        print("res req: ", res)
        if res['status'] == 200:
            return redirect(url_for('index')) # redirect to index
        else:
            return jsonify(res), 500  # returns json error


@app.route('/api/product/create', methods=["POST"])
def api_create_product():

    try:
        data = request.json
        fb_service.create_product(data)
        res = Response.new_response(None)
        return jsonify(res.__dict__), 200
    except Exception as e:
        res = Response.new_error(str(e), 500)
        return jsonify(res.__dict__), 500


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, host='localhost', port=port)
