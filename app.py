
import streamlit as st
from multiapp import MultiApp
from services import inicio,datos,autoML,modelo_analisis,dashboard # import your app modules here


FAVICON_URL = "https://i.imgur.com/2b7fItD.png"

st.set_page_config(
    page_title="Datacrop Service", page_icon=FAVICON_URL,
)

app = MultiApp()

app.add_app("Inicio", inicio.app)
app.add_app("Analisis de los Datos", datos.app)
#app.add_app("Analisis del Modelo", modelo_analisis.app)
app.add_app("Dashboards", dashboard.app)
#app.add_app("AutoML", autoML.app)
#app.add_app("AgroML Service")
#app.add_app("AutoML Service")
# The main app
app.run()


## Remover el footer de made with streamlit
hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)