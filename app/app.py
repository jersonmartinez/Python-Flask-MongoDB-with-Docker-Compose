import json
from flask import Flask, json, Response
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

app = Flask(__name__)

class ConnectionMongoDB:
    def __init__(self, data):
        self.server     = data['server']
        self.port       = data['port']
        self.username   = data['username']
        self.password   = data['password']
        self.db         = data['db']
        
    def getDB(self):
        mongoClient = MongoClient("mongodb://" + str(self.username) + ":" + str(self.password) + "@" + str(self.server) + ":" + str(self.port) + "/?authMechanism=DEFAULT&authSource=" + str(self.db), serverSelectionTimeoutMS=500)

        try:
            if mongoClient.admin.command('ismaster')['ismaster']:
                return "Connected to the MongoDB Server!"
        except OperationFailure:
            return ("Database not found.")
        except ServerSelectionTimeoutError:
            return ("MongoDB Server is down.")

@app.route('/api')
def get_api():
    data = {
        "server":   "cs_mongodb",
        "port":     '27017',
        "username": "root-crashell",
        "password": "password-crashell",
        "db":       "db_crashell"
    }

    response = ConnectionMongoDB(data).getDB()
    return Response(response=json.dumps(response), status=200, mimetype='application/json')

@app.route('/', methods=('GET', 'POST'))
def hello():
    return '<h1 style="background-color: #262626; color: white; padding: 20px; text-align:center;">Hello, Crashell!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)