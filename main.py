import streamlit as st
import src.manage_data as dat
from PIL import Image
#import src.manage_data as dat
#import plotly.express as px
#import pandas as pd
#import folium
#import codecs
#from streamlit_folium import folium_static
#import streamlit.components.v1 as components

imagen = Image.open("images/kamino1.jpg")
st.image(imagen)

st.write("""
# Kamino APP - ¡Bienvenido/a a Kamino!
### Le ayudamos a encontrar lo que necesite durante el Kamino.

"""
)

st.write("""

### ¿En qué localidad se encuentra?

"""
)

localidad = st.selectbox(
    "Seleccione uno de la lista", ["Roncesvalles", "Zubiri", "Pamplona", "Puente la Reina", "Estella"]
)
st.write("Opción seleccionada:", localidad)


st.write("""

### ¿Qué busca?

"""
)
st.header("¿Qué busca?")


opcion = st.selectbox(
    "Seleccione uno de la lista", ["Alojamiento", "Restauración", "Puntos de interés"]
)
st.write("Opción seleccionada:", opcion)

st.subheader("¿Qué busca?")
# Radio Buttons
eleccion = st.radio("Qué es lo que está buscando?", ("Alojamiento", "Restauración", "Puntos de interés"))
if eleccion == "Alojamiento":
    st.info("Ha seleccionado: Alojamiento")
elif eleccion == "Restauración":
    st.success("Ha seleccionado: Restauración")
else:
    st.warning("Ha seleccionado: Puntos de interés")

st.write("""
#Datos de los alojamientos
"""
)
#st.subheader("Balloons")
# Balloons
st.stars()

datos = dat.carga_data()
st.dataframe(datos)

localidad = st.selectbox(
    "¿En qué localidad se encuentra?", dat.lista_localidades()
    )


