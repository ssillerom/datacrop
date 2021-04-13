
import streamlit as st
from multiapp import MultiApp
from services import inicio, datos, autoML, dashboard, eda, limpieza

try:
    st.set_page_config(page_title='Datacrop Platform', page_icon="https://i.imgur.com/2b7fItD.png",layout='wide', initial_sidebar_state='expanded')
except:
    pass

# Se añade al objeto multi app todas las aplicaciones que componen la plataforma para que sean ejecutadas cuando se ejecute el servicio
app = MultiApp()

app.add_app("Inicio", inicio.app)
app.add_app("Limpieza de Datos", limpieza.app)
app.add_app("Analisis de los Datos", datos.app)
app.add_app("Dashboards", dashboard.app)
app.add_app("Datacrop Exploratory Service", eda.app)
app.add_app("Datacrop AutoML Service", autoML.app)


# ejecucion app principal
app.run()




# Remover el footer de made with streamlit

