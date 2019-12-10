from flask import Flask, request, render_template, jsonify, redirect, url_for
import os

import requests
from configuration.firebase_manager import FireStoreService

app = Flask(__name__)
fb_service = FireStoreService()


@app.route('/', methods=['GET'])
def index():
    """
    View for the landing page.
    :return: redirection to product listings.

    return redirect(url_for('product_select_list'))
    """
    return redirect(url_for('product_select_list'))


@app.route('/product/list', methods=['GET'])
def product_select_list():
    # if request.method == 'GET':
    return render_template('hola_mundo.html')


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, host='localhost', port=port)
