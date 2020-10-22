from flask import Flask, request
from flask_cors import CORS
from controllers.Activo import activo

app = Flask(__name__)
CORS(app)

@app.route('/activos',methods=['GET'])
def getAll():
    return (activo.list())

@app.route('/activos/<id>',methods=['GET'])
def getOne(id):
    return (activo.find(id))

@app.route('/activos',methods=['POST'])
def post():
    body = request.json
    return (activo.create(body))

@app.route('/activos/<id>',methods=['DELETE'])
def delete(id):
   #body = request.json
    return (activo.delete(id))


app.run(port=5000,debug=True)