from flask import Flask
from flask import jsonify
from flask import request
from utility import *

app = Flask(__name__)

#Initialize ProtVec
model = initialize()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/protein/embed", methods=['POST'])
def embed():
    content = request.get_json(silent=True)
    print content
    first, second, third = embedding(model, content['seq'])
    return jsonify(split_one = first, split_two = second, split_three = third)
