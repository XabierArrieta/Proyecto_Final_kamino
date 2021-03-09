from flask import Flask, request, Response, jsonify
from mongoConnection import *
from bson import json_util, ObjectId
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util


app = Flask("Kaminoapi")

# Endpoints

#Bienvenid@ a la API!

@app.route("/") 
def bienvenida():
    print("Bienvenido a la API de Kamino")
    localidad = input("¿En qué localidad se encuentra?")
    return localidad

# Mostrar todos los alojamientos;

@app.route("/alojamiento") 
def get_alojamiento_Pamplona():
    res_a = get_alojamiento_Pamplona()
    return jsonify(qts)



app.run(debug=True)