import os
from flask import Flask
from flask import json as fjson
from flask import request
from pymongo import MongoClient


app = Flask(__name__)
mongouri = os.getenv('MONGO_URI')
if mongouri == None:
    mongohost = os.getenv('MONGO_HOST')
    mongoport = os.getenv('MONGO_PORT')
    if mongohost != None and mongoport != None:
        mongouri = "mongodb://{}:{}/".format(mongohost, mongoport)
    else:
        mongouri = "mongodb://localhost:27017/"
print("Using MongoDB URI: {}".format(mongouri), flush=True)


@app.route('/ping', methods=['GET'])
def ping():
    return "OK"


@app.route('/upload', methods=['POST'])
def upload():
    j = request.json
    print(j)
    return "{\"error\": \"NOT IMPLEMENTED YET\", \"received\": " + str(j) + "}"

