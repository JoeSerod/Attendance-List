
import requests
from flask import Flask, request, jsonify, render_template
from configuration.firebase_manager import FireStoreService

app = Flask(__name__)
fb_service = FireStoreService()


@app.route('/api/worker/create')
def create_worker():
    try:
        data = request.json
        fb_service.create_worker(data)
        res = Response.new_response(None)
        return jsonify(res.__dict__), 200
    except Exception as e:
        res = Response.new_error(str(e), 500)
        return jsonify(res.__dict__), 500


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()