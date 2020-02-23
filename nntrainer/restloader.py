import os
from flask import Flask
from flask import json as fjson
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId

import nnmodel


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


@app.route('/info', methods=['GET'])
def info():
    inf_data = {
        "name": "nntrainer",
        "mongodb-uri": mongouri,
        "nnmodel": {
            "version": nnmodel.__version__,
            "license": nnmodel.__license__
        }
    }
    return str(inf_data)
