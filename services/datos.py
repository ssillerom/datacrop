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
from utils import download_button

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_pregunta(ruta_archivo):
    csv = pd.read_csv(ruta_archivo)
    return csv


def st_display_sweetviz(report_html, width=1000, height=500):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    stc.html(page, width=width, height=height, scrolling=True)


def app():
    menu2 = ['Reto: Pregunta 1', 'Reto: Pregunta 2', 'Reto: Pregunta 3']
    choice = st.sidebar.radio(
        'Seleccione el analisis de la pregunta que desee del reto: ', menu2)
    if choice == "Reto: Pregunta 1":
        df1 = load_pregunta('./data/consumoF_H_Limpio.csv')
        st.dataframe(df1)
    elif choice == "Reto: Pregunta 2":
        df2 = load_pregunta('./data/comercioExterior_Limpio.csv')
        st.dataframe(df2)
    elif choice == "Reto: Pregunta 3":
        df3 = load_pregunta('./data/covid19DatosEU_Limpio.csv')
        st.dataframe(df3)
    else:
        st.info("Esperando a que seleccione alguna de las preguntas...")
