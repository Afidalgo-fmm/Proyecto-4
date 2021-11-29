from flask import Flask, request
from flask import jsonify
import s.Paraget as pg
import s.Parapost as pp
from pymongo import MongoClient



app = Flask(__name__)

@app.route("/")
def inicio():
    return 'inicio api'

@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    diccionario = {"scene": request.form.get("escena"),
    "character_name": request.form.get("personaje"), 
    "dialogue": request.form.get("frase")}
    return pp.inchar(diccionario)
    
@app.route("/frases/<name>")
def todas(name):
    person = name
    frases = pg.todas_frases(person)
    return jsonify(frases)


@app.route("/personaje/<temp>")
def person(temp):
    persona = pg.personaje(temp)
    return persona

if __name__ == '__main__':
    app.run(debug = False)