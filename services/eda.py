import streamlit as st
import pandas as pd
import sweetviz as sv
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from utils import download_button

def app():
    st.header("¿Quieres ver de una forma rápida y sencilla la calidad de tus datos?")
    st.subheader("##Usa EDS y consigue un reporte estadistico exploratorio sobre tus datos. Dispones de dos tipos de reportes diferentes: Pandas EDA y Sweetviz Report")


    menu = ["Pandas EDA", "SweetViz Report"]
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
            pr.to_file(output_file='PandasEDA_Datacrop.html')
            
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
                st.write(report)
            else:
                "pass"
