import os
import requests
from models.response import Response
from flask import Flask, request, jsonify, render_template
from configuration.firebase_manager import FireStoreService

app = Flask(__name__)
fb_service = FireStoreService()

@app.route('/', methods=['GET'])
def index():
    """
    View for the landing page.
    :return: redirection to product listings.
    """
    return render_template("header.html")

@app.route('/create/worker', methods= ["GET","POST"])
def create_worker():
    if request.method == 'GET':
        res = requests.get("http://localhost:5000/api/category/select",
                           headers=headers).json()
        return render_template("create_product.html", categories=res['data'])
    if request.method == 'POST':
        form = request.form
        new_product = Product(form['id'], form['name'], form['details'],
                              form['price'], form['quantity'], form['stock'],
                              request.form.get('select_category'),
                              form['image'])
        print(new_product)
        res = requests.post("http://localhost:5000/api/product/create",
                            json=new_product.__dict__, headers=headers).json()
        print("res req: ", res)
        if res['status'] == 200:
            return redirect(url_for('index'))  # redirect to index
        else:
            return jsonify(res), 500  # returns json error

@app.route('/api/worker/create', methods=["POST"])
def api_create_worker():

    try:
        data = request.json
        fb_service.create_worker(data)
        res = Response.new_response(None)
        return jsonify(res.__dict__), 200
    except Exception as e:
        res = Response.new_error(str(e), 500)
        return jsonify(res.__dict__), 500


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, host='localhost', port=port)