from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from utility import *

app = Flask(__name__)
CORS(app)

#Initialize ProtVec
model = initialize()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/protein/embed", methods=['POST'])
def embed():
    content = request.get_json(silent=True)
    first, second, third = embedding(model, content['seq'])
    return jsonify(split_one = first, split_two = second, split_three = third)
