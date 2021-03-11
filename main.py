import streamlit as st
import src.manage_data as dat
from PIL import Image
#import src.manage_data as dat
#import plotly.express as px
import pandas as pd
import folium
#import codecs
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map
import webbrowser
#import streamlit.components.v1 as components

imagen = Image.open("images/kamino1.jpg")
st.image(imagen)

st.write("""
# ¡Bienvenido/a a Kamino!
### ¿Necesita ayuda?

"""
)

pueblo = st.selectbox(
    " ¿En qué localidad se encuentra?", dat.lista_localidades())
st.write("Opción seleccionada:", pueblo)


coleccion = st.radio("¿Qué es lo que está buscando?", ("Alojamiento", "Restauracion", "Patrimonio"))
if coleccion == "Alojamiento":
    st.info("Ha seleccionado: Alojamiento")
elif coleccion == "Restauracion":
    st.success("Ha seleccionado: Restauración")
else:
    st.warning("Ha seleccionado: Patrimonio")




#las dos variables son: localidad y eleccion


st.write("""
#### En el siguiente mapa se muestran todas las opciones:

Clikando sobre el punto que le interese, obtendrá un número que
podrá buscarlo en la lista
"""
)


folium_static(dat.mapa(pueblo, coleccion))


st.header("""
Introduzca el código que que quiera buscar
""")
texto = st.text_input("Código: ")

if st.button("Aceptar"):
    st.write("Buscando resultados")

    st.write("""
    #### En la siguiente tabla se muestran listadas, en detalle, todas las opciones:

    """
    )
    datos = dat.filtro(coleccion, texto)

    st.dataframe(datos)




st.sidebar.header("Sobre Kamino")

st.sidebar.write(
"""
Kamino es mi proyecto final del 
Bootcamp de Data Analytics de Ironhack 
en Madrid
"""
)

st.sidebar.header("Contacto")

st.sidebar.write(

"""Para cualquier consulta sobre el 
proyecto, escríbeme a la siguiente
dirección:

**xabier.arrieta@kamino.es**"""
)


add_imagen = imagen = Image.open("images/qr.png")
st.sidebar.image(imagen)


url = 'https://github.com/XabierArrieta/Proyecto_Final_kamino'

if st.sidebar.button('Proyecto Kamino'):
    webbrowser.open_new_tab(url)
