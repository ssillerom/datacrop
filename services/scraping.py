import streamlit as st
import streamlit.components.v1 as stc

def app():
    st.header("Enriquecimiento de los datos a través de técnicas de Scraping con Selenium")

    st.markdown("""
    Para ello se ha usado librerías como Selenium para automatizar la extracción a través de etiquetas HTML de los datos que se encontraban alojados en sitios web. Además de la búsqueda de otras fuentes de datos donde se podían bajar los mismos directamente en formato csv.
    """)

    HtmlFile = open('./data/scraping_datacrop.html',
                            'r', encoding='utf-8')
    source_code = HtmlFile.read()

    stc.html(source_code, width=1400, height=650, scrolling=True)
    


