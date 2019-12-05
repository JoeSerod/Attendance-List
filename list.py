
import requests
from flask import Flask, request, jsonify, render_template
from configuration.firebase_manager import FireStoreService

app = Flask(__name__)
fb_service = FireStoreService()


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()