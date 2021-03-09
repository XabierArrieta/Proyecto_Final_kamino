import streamlit as st
import src.manage_data as dat
from PIL import Image
#import src.manage_data as dat
#import plotly.express as px
#import pandas as pd
import folium
#import codecs
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map

#import streamlit.components.v1 as components

imagen = Image.open("images/kamino1.jpg")
st.image(imagen)

st.write("""
# ¡Bienvenido/a a Kamino!
### Le ayudamos a encontrar lo que necesite durante el Kamino.

"""
)

pueblo = st.selectbox(
    " ¿En qué localidad se encuentra?", dat.lista_localidades())
st.write("Opción seleccionada:", pueblo)


eleccion = st.radio("¿Qué es lo que está buscando?", ("Alojamiento", "Restauración", "Puntos de interés"))
if eleccion == "Alojamiento":
    st.info("Ha seleccionado: Alojamiento")
elif eleccion == "Restauración":
    st.success("Ha seleccionado: Restauración")
else:
    st.warning("Ha seleccionado: Puntos de interés")


#las dos variables son: localidad y eleccion


folium_static(dat.mapa(pueblo, eleccion))


#nombre, punto_inicio = dat.localidad()
        
#query = dat.locali_colec_coord(coleccion, nombre)
                                
#mapassss = folium.Map(location = punto_inicio, zoom_start=15)
#folium_static(mapassss)




datos = dat.carga_data()
st.dataframe(datos)




