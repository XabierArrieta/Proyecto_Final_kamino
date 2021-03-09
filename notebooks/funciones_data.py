import pandas as pd
import geopandas as gpd
import sys
from dotenv import load_dotenv
import os
import requests
import json
from functools import reduce
import operator
from cartoframes.viz import Map, Layer, popup_element
from haversine import haversine
from pymongo import MongoClient,GEOSPHERE
import shapely.geometry




def coord(direccion, localidad):
    
    """
    La función coord, metiendo una dirección y una localidad te devulve la latitud y longitud.
    
    Con el Try y except aseguramos que si hubiera un error nos lo printee y así poder saber dónde se ecnuentra.
    
    input: dirección y localidad
    output: coordenadas
    
  
    """
    
    try:

        direccion = direccion.replace(" ", "+")
        load_dotenv()
        gtok = os.getenv("gtok")

        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(direccion, gtok)
        cosas = requests.get(url).json()
        lat = cosas['results'][0].get('geometry')['location']['lat']
        lng = cosas['results'][0].get('geometry')['location']['lng']
        return lat, lng
    
    except:
        print("Error, no encuentra esta dirección", direccion)

