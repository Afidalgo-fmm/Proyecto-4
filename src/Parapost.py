from pymongo import MongoClient
import pandas as pd
import os 
import json


connection = MongoClient('localhost', 27017)
db = connection.get_database("Ironhack")
c = db.get_collection('4-proyecto')

df = pd.read_csv('../datos/Data.csv')

records = json.loads(df.T.to_json()).values()
c.insert_many(records)

def insertar():
    pass

'''
no me sirve
def inchar(data):
    header = ['index','Season', 'Epi_number', 'Epi_name', 'character', 'line']
    for i in data:
        row= {}
        for j in header:
            row[j] = i
        a = c.insert_many(csv_to_json(data, header=0))
    return a
'''
        