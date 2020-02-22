import os
from flask import Flask
from flask import json as fjson
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId


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
mongo = MongoClient(mongouri)
mlfdb = mongo['mlfabrique']
archs = mlfdb['nnarchs']


@app.route('/ping', methods=['GET'])
def ping():
    return "OK"


@app.route('/architecture', methods=['POST'])
def insert_architecture():
    archjson = request.json
    print(archjson, flush=True)
    arch_id = archs.insert_one(archjson).inserted_id
    return str(arch_id)


@app.route('/architecture/<arch_id>', methods=['GET'])
def get_architecture(arch_id):
    arch = archs.find_one({"_id": ObjectId(arch_id)})
    return str(arch)

