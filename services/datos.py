# Paquetes Core
import numpy as np
import pandas as pd
import codecs
import streamlit as st
# Paquetes necesarios para el EDA Automático
import streamlit.components.v1 as stc
import sweetviz as sv
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_pregunta(ruta_archivo):
    csv = pd.read_csv(ruta_archivo)
    return csv


def st_display_sweetviz(report_html, width=1000, height=500):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    stc.html(page, width=width, height=height, scrolling=True)

# •	ENTRADA 1: - ¿De qué manera se ha visto afectado el consumo y la producción de frutas y hortalizas durante la pandemia con respecto a años anteriores? 
# •	ENTRADA 2: Evolución de los precios en las principales plataformas de distribución de España.
# •	ENTRADA 3: Impacto de la COVID-19 en el comercio exterior 
# •	ENTRADA 4: ¿Existe correlación entre los casos de COVID-19 y las importaciones/exportaciones a nivel de la Unión Europea? 
# •	ENTRADA 5: El estado de alarma revoluciona los hábitos de consumo
# •	ENTRADA 6: Página Web


def app():
    menu2 = ['Análisis 1', 'Análisis 2', 'Análisis 3', 'Análisis 4', 'Análisis 5']
    choice = st.sidebar.radio(
        'Seleccione el analisis de la pregunta que desee del reto: ', menu2)
    if choice == "Análisis 1":
        st.header("¿De qué manera se ha visto afectado el consumo y la producción de frutas y hortalizas durante la pandemia con respecto a años anteriores?")
        df1 = load_pregunta('./data/consumoF_H_Limpio.csv')
        st.dataframe(df1)
    elif choice == "Análisis 2":
        st.header('Evolución de los precios en las principales plataformas de distribución de España.')
        df2 = load_pregunta('./data/comercioExterior_Limpio.csv')
        st.dataframe(df2)
    elif choice == "Análisis 3":
        st.header('Impacto de la COVID-19 en el comercio exterior')
        df3 = load_pregunta('./data/covid19DatosEU_Limpio.csv')
        st.dataframe(df3)
    elif choice == "Análisis 4":
        st.header('¿Existe correlación entre los casos de COVID-19 y las importaciones/exportaciones a nivel de la Unión Europea?')
        df3 = load_pregunta('./data/covid19DatosEU_Limpio.csv')
        st.dataframe(df3)
    elif choice == "Análisis 5":
        st.header('El estado de alarma revoluciona los hábitos de consumo')
        df3 = load_pregunta('./data/covid19DatosEU_Limpio.csv')
        st.dataframe(df3)
    else:
        st.info("Esperando a que seleccione alguna de las preguntas...")

    # Remover el footer de made with streamlit
    hide_footer_style = """
        <style>
        .reportview-container .main footer {visibility: hidden;}    
        """
    st.markdown(hide_footer_style, unsafe_allow_html=True)

