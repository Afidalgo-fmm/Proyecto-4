from pymongo import MongoClient
import json
client = MongoClient("localhost:27017")
db = client.get_database("Ironhack")
c = db.get_collection('4-proyecto')

#Necesito una funcion para sacar las temporadas de los personajes



# Necesito una funcionn que me saque las frases de los personajes
projfrases = {'_id':0, 'character': 1, 'line': 1}
def todas_frases(nombre):
    query = {"character": f"{nombre}"}
    frases = list(c.find(query,projfrases)) # El ID hay que quitarlo si no, no voy a poder jsonizar y la api va a dar error
    return frases

#Query para sacar el nombre del personaje segun la temporada que me digan

projcharacter = {'_id':0 , 'character': 1, 'Season':1}

def personaje(temp):
    query2 = {'Season': f'{temp}'}
    personaje = list(c.find(query2, projcharacter))
    return personaje




'''
#Query para sacar el personaje mas hablador segun la temporada.
projmashablador = {'_id':0 , 'character': 1, 'Season':1}
def mashablador(temp):
    query3 = {'Season': f'{temp}'}
    #for i in a:
    mas = list(c.find(query3, projmashablador))
    return mas 
'''



