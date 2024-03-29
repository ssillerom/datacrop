import streamlit as st
import pandas as pd
import codecs 
import sweetviz as sv
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)


def app():
    st.header("¿Quieres ver de una forma rápida y sencilla la calidad de tus datos?")
    st.subheader("Usa EDS y consigue un reporte estadistico exploratorio sobre tus datos. Dispones de dos tipos de reportes diferentes: Pandas EDA y Sweetviz Report.")

    st.markdown('##')
    st.markdown("Tiempo medio de ejecución: 30 segundos")


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
            st.info('Generando informe con Pandas EDA espere unos segundos...')
            pr = ProfileReport(df, explorative=True)
            st.header('**DataFrame Cargado**')
            st.write(df)
            st.write('---')
            st.header('**Reporte de Pandas Profiling**')
            st_profile_report(pr)
            pr.to_file(output_file='PandasEDA_Datacrop.html')

        else:
            st.info('Recuerde cargar el CSV para poder generar el reporte.')
            if st.button("Usar datos de ejemplo"):
                st.info(
                    "Generando informe de ejemplo con Pandas EDA porfavor espere...")
                df_test = pd.read_csv("./data/Consumo_Comunidades_F_H.csv")
                pr = ProfileReport(df_test, explorative=True)
                st.header('**DataFrame Cargado**')
                st.write(df_test)
                st.write('---')
                st.header('**Reporte de Pandas Profiling**')
                st_profile_report(pr)
                pr.to_file(output_file='PandasEDA_Datacrop.html')
            else:
                pass

    elif choice == "SweetViz Report":
        data_file = st.file_uploader("Upload CSV", type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head())
            if st.button("Generar reporte"):
                report = sv.analyze(df)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.HTML")
            else:
                pass
        else:
            st.info("Esperando a recibir datos en CSV...")
            if st.button("Usar datos de ejemplo"):
                st.info('Generando informe, porfavor espere...')
                df_test = pd.read_csv("./data/Consumo_Comunidades_F_H.csv")
                report = sv.analyze(df_test)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.HTML")

    # Remover el footer de made with streamlit
    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
