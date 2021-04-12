import streamlit as st
from utils import open_link
import webbrowser


# TO-DO
def app():
    st.header(":tractor: Datacrop Advanced Agro-Analytics Services v0.2.0 :deciduous_tree:")

    st.subheader("""¡Bienvenidos a nuestra plataforma creada para la fase nacional del "Reto Cajamar Agro Analysis"

    Recuerde que puede ver la documentación de la plataforma en nuestra página web donde se explica su estructura y cómo funciona

    El menú principal que hay a su izquierda se compone de:
    - Análisis de los Datos del reto
    - Dashboards de PowerBI
    - Datacrop Exploratory Service
    - Datacrop AutoML Service

    Porfavor no desmarque la casilla de inicio de sesión para poder acceder al resto de contenido de la web

    """)

    link = '[Acceder a la Documentación](https://datacrop.es/recursos-y-descargas/)'
    st.markdown(link, unsafe_allow_html=True)   
    
    col1,col2,col3 = st.beta_columns(3)

    col1.header("Formado por:")
    col1.image('./img/logo-light.png')
    col1.image('./img/datagri.png')
    
    col2.image('./img/sergio.png',width= 200)
    col2.markdown('Sergio Sillero')
    col3.image ('./img/jimena.png',width= 200)
    col3.markdown('Jimena Areta')

    







