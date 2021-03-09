import pandas as pd
import folium
from src.mongoConnection import *

from folium import Choropleth, Circle, Marker, Icon, Map
from geopy.geocoders import Nominatim

import requests
import json

def carga_data():
    aloj = pd.read_csv('data/kamino_aloj_final.csv')
    rest = pd.read_csv('data/kamino_rest_final.csv')
    patr = pd.read_csv('data/kamino_patr_final.csv')
    return aloj

def lista_localidades():
    data = carga_data()
    return list(data.LOCALIDAD.unique())

def localidad(localidad):
    
    """
    La función recibe un input del usuario; la localización en la que se encuentra y a través de Geocoder
    devuelve el nombre de la localidad y las coordenadas.
    
    Input: Nombre de la localidad
    Output: Nombre de la localidad y las coordenadas de la localidad
    
    """
    
    #localidad = (input("Localidad: ")).upper() #Convierte el input en mayúsculas para que es´te igual que en la BBDD.
    
    locator = Nominatim(user_agent = "myGeocoder")
    location = locator.geocode(localidad)
    coordenadas = location.latitude, location.longitude
 
    return localidad, list(coordenadas)


def locali_colec_coord(coleccion, *lugar):
    
    """
    La función recibe una colección y un lugar; hace una query a la colección seleccionada y el lugar
    especifivado y devuelve las coordenadas de los lugares encontrados.
   
    
    Input: Nombre de la colección y localidad
    Output: Las coordenadas de la localidad
    
    """
    bbdd = db[f'{coleccion}']
    query = {"LOCALIDAD":f"{lugar[0]}"}
    coordenadas = list(bbdd.find(query,{"_id":0,"COORDENADAS":1}))
    return coordenadas

def markers(coleccion):
    
        if coleccion == "Alojamiento":
            icono = Icon(color = "blue",
                    prefix = "fa",
                    icon = "hotel",
                    icon_color = "black")
            
        elif coleccion == "Patrimonio":   
            icono = Icon(color = "orange",
                    prefix = "fa",
                    icon = "camera",
                    icon_color = "black")
            
        else:
            icono = Icon(color = "green",
                    prefix = "fa",
                    icon = "spoon",
                    icon_color = "black")

        return icono

def mapa (pueblo, coleccion):
    
    """
    Función creada para mostrar en un mapa la información relacionada con cada colección dependiendo de la localidad
    
    input : localidad y colección
    output : mapa
    
    
    """
    
    #nombre, punto_inicio = localidad() #Devuelve el nombre de la localidad y las coordenadas
    
    query = locali_colec_coord(coleccion, pueblo) #Hace una query con el nombre de la localidad
    
    mapa = folium.Map(location = localidad(pueblo)[1], zoom_start=15) #Devuelve un mapa con las coordenadas
    

    for cada_entrada in query:
        coordenadas = list(cada_entrada.values())
        lat = coordenadas[0].split(",")[0][1:]
        lon = coordenadas[0].split(",")[1][:-1]
                         
        loc = {"location":[lat,lon],
          "tooltip": f"{coleccion}"}

        marker_of = Marker(**loc, icon = markers(coleccion) , popup=f"{coleccion}")
        marker_of.add_to(mapa)
    
    return mapa


    
