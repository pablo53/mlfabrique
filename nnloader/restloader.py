from flask import Flask
from flask import json as fjson
from flask import request


app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return "OK"


@app.route('/upload', methods=['POST'])
def upload():
    j = request.json
    print(j)
    return "{\"error\": \"NOT IMPLEMENTED YET\", \"received\": " + str(j) + "}"

