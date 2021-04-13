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
import webbrowser


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
    menu2 = ['Análisis 1', 'Análisis 2',
             'Análisis 3', 'Análisis 4', 'Análisis 5']
    st.subheader('Seleccione el análisis que desea visualizar: ')
    choice = st.selectbox(
        'Seleccione el analisis de la pregunta que desee del reto: ', menu2)
    if choice == "Análisis 1":

        st.header("¿De qué manera se ha visto afectado el consumo y la producción de frutas y hortalizas durante la pandemia con respecto a años anteriores?")
        st.markdown('###')
        st.subheader('Jupyter Notebooks: ')

        col1, col2, col3 = st.beta_columns(3)

        if col1.checkbox('Variación Consumo/Precio'):
            st.markdown(
                '*Desmarque la casilla para poder seleccionar otro notebook*')
            HtmlFile = open('./data/analisis/a1/analisis1.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=650, scrolling=True)
        elif col2.checkbox('Consumo vs Producción'):
            st.markdown(
                '*Desmarque la casilla para poder seleccionar otro notebook*')
            HtmlFile = open('./data/analisis/a1/analisis1_2.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=650, scrolling=True)

        elif col3.checkbox('Composición Atmosférica'):
            st.markdown(
                '*Desmarque la casilla para poder seleccionar otro notebook*')
            HtmlFile = open('./data/analisis/a1/analisis1_3.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=650, scrolling=True)

        st.markdown('##')

        st.markdown("""
        La pandemia ha impulsado la búsqueda de un estilo de vida más saludable que tiene como pilar fundamental una alimentación rica en frutas y verduras. Un síntoma de esta tendencia son campañas como la de la Federación Española de Asociaciones de Productores Exportadores de Frutas y Hortalizas (Fepex) llevó a cabo en abril de 2020 la campaña ‘Vive Saludablemente. Frutas y Verduras '' con el objetivo de “impulsar hábitos de consumo saludables y mostrar la riqueza y variedad de la producción hortofrutícola nacional” y buscando en estos alimentos un aliado contra la pandemia. La campaña sumaba en mayo 120 empresas adheridas.

        Con la finalidad de poder analizar cómo afectó la pandemia al mercado agrícola, más en concreto la variación del consumo y precio de frutas y hortalizas, se incluye a continuación un informe general que compara la variación de 2020 con 2019 y de 2019 con 2018 por cada comunidad autónoma y producto.

        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiMjc0ODAzMjgtOWEwNS00MjVkLWIzZTUtNTUwNjc1Mjc1YjAxIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

        st.markdown('##')
        
        st.markdown("""El consumo total de frutas y de hortalizas se disparó en el mes de abril alcanzando valores de crecimiento del 35.56 % y el 44.04% respectivamente, valores que disminuyeron con la desescalada hasta estabilizarse con la llegada de la “nueva normalidad”.  
        """)

        st.markdown('##')

        st.image('./img/img1.png', use_column_width='auto')

        st.markdown('##')

        st.markdown("""
        Las frutas que más se consumieron fueron aquellas con más vitamina C (como es el caso de las naranjas) al igual que limones, manzanas, plátanos y peras. Resulta muy interesante el caso de la nectarina que en el mes de marzo había sufrido una caída del 11% para pasar a un crecimiento del 165% en abril. Al igual que la nectarina, en la tabla de la izquierda (top 10 crecimientos del consumo), también aparecen otras frutas de hueso como el melocotón o el albaricoque.
        Sin embargo, tal y como se observa en la tabla de la derecha (top 10 caídas del consumo) , las fresas protagonizaron una dramática caída de la demanda tanto en el mercado interior como de exportación, coincidente además con el periodo de máxima producción.
        En cuanto a las hortalizas, las más consumidas fueron aquellas consideradas más saludables como las coles, el brócoli, las zanahorias, las berenjenas o los calabacines. Llama la atención el caso de Navarra y la Rioja por el cambio brusco en sus hábitos alimentarios (aumento masivo de coles en Navarra y de ciruelas en la Rioja).
        
        """)

        st.markdown('##')

        st.image('./img/img2.png',use_column_width='auto')

        st.markdown('##')

        st.markdown("""
        Al mismo tiempo la producción se vio afectada por la falta de jornaleros, mano de obra muy específica que provenía en gran parte de personal inmigrante. El cierre de fronteras dificultó que pudieran llevar a cabo su labor. Estas dificultades afectaron a la producción del año 2020, que se vio reducida con respecto a 2018 y 2019 como se observa en informe presentado a continuación. 
        
        """)
        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZGVkNDBhMzUtYTU4YS00MWVkLWEwNjYtYzRlY2ZiMTVmODhhIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

        st.markdown('##')

        st.markdown("""
        Las estrictas normas de seguridad que tenían que seguir los agricultores doblaron los precios de logística y transporte en el campo, además de que tuvieron que asumir la compra de material sanitario de protección (mascarillas y otros productos). Esto provocó que en muchas zonas no se pudiese cubrir la demanda existente de ciertos productos como el melocotón o la nectarina y que se dispararan los precios (explicación en detalle en el análisis 2).
        También afectaron a la producción variables exógenas como la temperatura, la humedad o la contaminación. 
        En el mapa que incluimos a continuación se pueden ver las diferentes estaciones atmosféricas españolas que recogen datos de compuestos químicos, algunos claramente perjudiciales para la producción agrícola, como el dióxido de azufre (SO2) o el dióxido de nitrógeno (NO2) y otros de dudoso efecto como el ozono (O3).

        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzRjMzgyZmQtN2YzOC00NjliLWEzZDYtOWFiMmFhYTQ3YjUxIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)
        
        st.markdown('##')

        st.markdown("""
        Durante los meses del estado de alarma, en el que la población española fue obligada a permanecer en su domicilio, se observa un descenso en las emisiones de compuestos contaminantes como el dióxido de nitrógeno o el dióxido de azufre. Una menor concentración de estos compuestos en la atmósfera favoreció la mejora en la producción agrícola, ya que el exceso de nitrógeno empeora la calidad del aire, del suelo y tiene importantes efectos sobre la salud humana. Es interesante comprobar que el descenso no es homogéneo en todo el país, seguramente como consecuencia de diferencias locales en las medidas de confinamientos adoptadas. Sin embargo, con la desescalada esos valores volvieron a la normalidad. Al igual que disminuyó la polución, se esperaba que también lo hiciese la concentración de ozono. Sin embargo, los datos mostraron el resultado contrario. Durante los meses del estado de alarma, pasó de haber un 7% de concentración a un 9%. La explicación de este fenómeno no es clara pero la posible influencia de otros factores atmosféricos como la temperatura, las precipitaciones, el viento, las horas de sol o las presiones mínimas y máximas en los niveles de polución podrían ser parte de la explicación.

        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZTNhNTQ2ZGYtNjcxNy00OTA1LWFmMDItOWI5ZTlmMjk3YjhlIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9&amp;pageName=ReportSectionb09c803e00d05d8a769d", height=635, width=1200)

        st.markdown('##')

        st.markdown("""
        Sí parece que existe una correlación entre los diferentes compuestos químicos que se encuentran en la atmósfera y la producción. Para corroborar si esto era así, se representó una matriz de correlación con los datos de la producción y de la composición atmosférica de los 3 últimos años. El resultado fue el siguiente.
        
        """)

        st.markdown('##')

        st.image('./img/img3.png', use_column_width='auto')

        st.markdown('##')

        st.markdown("""
        Si se observa la fila de la producción, existe una correlación negativa (inversamente proporcional) entre la producción y el NO2 y el SO2 (más fuerte en el caso del NO2). Sin embargo, la correlación con el O3 es positiva (directamente proporcional). Los estudios demuestran que la cantidad de O3 en la troposfera en pequeñas cantidades es beneficioso, siempre y cuando no supere unos niveles a partir de los cuales deja de proteger a los cultivos de las plagas. 
        Hacen falta más datos para llegar a una respuesta concluyente sobre el efecto del ozono, pero a priori sabemos que la composición de la atmósfera es una variable a tener en cuenta si se quiere realizar una buena predicción de la producción.
        """)

    elif choice == "Análisis 2":
        st.header(
            'Evolución de los precios en las principales plataformas de distribución de España.')


    elif choice == "Análisis 3":
        st.header('Impacto de la COVID-19 en el comercio exterior')
        df2 = load_pregunta('./data/comercioExterior_Limpio.csv')
        st.dataframe(df2)
        df3 = load_pregunta('./data/covid19DatosEU_Limpio.csv')
        st.dataframe(df3)
    elif choice == "Análisis 4":
        st.header(
            '¿Existe correlación entre los casos de COVID-19 y las importaciones/exportaciones a nivel de la Unión Europea?')
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
