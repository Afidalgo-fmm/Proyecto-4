from flask import Flask, request
from flask import jsonify
import s.Paraget as pg
import s.Parapost as pp
from pymongo import MongoClient



app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def inicio():
    return 'inicio api'

@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    print(request.get_json())
    return pp.insertar(request.get_json())


@app.route("/frases/<name>", methods = ['GET'])
def todas(name):
    person = name
    frases = pg.todas_frases(person)
    return jsonify(frases)


@app.route("/personaje/<temp>", methods = ['GET'])
def person(temp):
    persona = pg.personaje(temp)
    return persona



if __name__ == '__main__':
    app.run(debug = False)