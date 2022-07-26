import json
from pydoc import resolve
from urllib import response
from flask import Flask, jsonify, request, json, Response
from pymongo import MongoClient
import logging as log
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

app = Flask(__name__)

class ConnectionMongoDB:
    def __init__(self, data):
        self.server     = data['server']
        self.username   = data['username']
        self.password   = data['password']
        self.db         = data['db']
        
    def getDB(self):

        # client = MongoClient("cs_mongodb", 27017, serverSelectionTimeoutMS=500)
        
        # db = client.db_name

        mongoClient = MongoClient("mongodb://root-crashell:password-crashell@cs_mongodb:27017/?authMechanism=DEFAULT&authSource=db_crashell", serverSelectionTimeoutMS=500)

        try:
            if mongoClient.admin.command('ismaster')['ismaster']:
                return "Connected!"
        except OperationFailure:
            return ("Database not found.")
        except ServerSelectionTimeoutError:
            return ("MongoDB Server is down.")

@app.route('/api')
def get_api():
    # return ("Nada de nada")
    data = {
        "server":   "cs_mongodb",
        "username": "root-crashell",
        "password": "password-crashell",
        "db":       "db-crashell"
    }

    response = str(ConnectionMongoDB(data).getDB())
    # print(response)
    # response = {'message': 'List all teams available in the DB.'}
    # return jsonify(response)
    return response
    # return Response(response=json.dumps(response), status=200, mimetype='application/json')

@app.route('/', methods=('GET', 'POST'))
def hello():
    return '¡Hola, Crashell!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)