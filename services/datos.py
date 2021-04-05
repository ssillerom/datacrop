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


def app():
    menu = ["Análisis Preguntas del reto", "Pandas EDA", "SweetViz Report"]
    choice = st.selectbox("Menu", menu)

    if choice == "Pandas EDA":
        # Se carga el CSV
        with st.header('1. Carga tus datos en CSV'):
            uploaded_file = st.file_uploader(
                "Porfavor, cargue los datos a analizar", type=["csv"])

        # Pandas Profiling Report
        if uploaded_file is not None:
            @st.cache(allow_output_mutation=True, suppress_st_warning=True)
            def load_csv():
                csv = pd.read_csv(uploaded_file)
                return csv
            df = load_csv()
            pr = ProfileReport(df, explorative=True)
            st.header('**DataFrame Cargado**')
            st.write(df)
            st.write('---')
            st.header('**Reporte de Pandas Profiling**')
            st_profile_report(pr)
        else:
            st.info('Recuerde cargar el CSV para poder generar el reporte.')

    elif choice == "SweetViz Report":
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            if st.button("Generar reporte"):
                report = sv.analyze(df)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")

    elif choice == "Análisis Preguntas del reto":
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
        # TO-DO
        st.markdown("hello world :)")
