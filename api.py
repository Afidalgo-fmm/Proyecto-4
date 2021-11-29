from flask import Flask, request
from flask import jsonify
import src.Paraget as pg
import src.Parapost as pp
from pymongo import MongoClient

app = Flask(__name__)
connection = MongoClient('localhost', 27017)
db = connection.get_database("ironhack")
c = db.get_collection('4-proyecto')


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





if __name__ == '__main__':
    app.run(debug = False)