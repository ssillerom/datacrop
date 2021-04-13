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

        st.markdown('##')

        if st.checkbox('Ver Jupyter Notebook'):
            HtmlFile = open('./data/analisis/a2/evol_precios.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=650, scrolling=True)
        else:
            pass

        st.markdown('##')

        st.markdown("""
        El estallido de la Covid-19 y la consecuente crisis sanitaria provocó una bajada inicial de precios. Sin embargo, como ya se vaticinaba en el análisis 1, el aumento de la demanda unido a las dificultades en la producción desembocó en un aumento de la volatilidad de los precios de ciertos alimentos, lo que provocó una inestabilidad del mercado que desembocó finalmente en un escenario alcista con una elevación significativa de los precios en frutas y hortalizas.
         
        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiNDZlZDcwODItMjZjNy00ZmZjLTllNDktOTk1ODU3MjM5YjE4IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9&amp;pageName=ReportSection",height=635,width=1200)

        st.markdown('##')

        st.markdown("""
        La demanda de frutas como fuente de vitaminas incrementó los precios de los cítricos, los melocotones (289.37%), la sandía (58.40%), el melón (82.54%) o la uva (67.32%). El precio del aguacate, considerado por sus grandes propiedades nutricionales como un “superalimento” también creció un 76.41%. También el de ciertas hortalizas como la berenjena (125%) o el calabacín (101%). El temor de la población a la enfermedad también se tradujo en sus hábitos a la hora de realizar la compra, optando por productos envueltos en plástico antes que aquellos que están expuestos (como ocurre con la lechuga (45.59%)).
        
        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiN2JjOTMyMzAtZTM3NC00YzAyLWIzMzYtOGE2NzZjOWVlMzNiIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height=635, width=1200)

        st.markdown('##')

        st.markdown("""
        Los precios que se alcanzaron en cada mercado dependieron de muchos factores, entre ellos la capacidad productiva de la comunidad autónoma a la que pertenece el mercado. En Cataluña se produjo una gran demanda de frutas de hueso como la nectarina, pero por la falta de capacidad productiva, los precios subieron. De hecho, si comparamos los precios de las nectarinas o de los melocotones entre mercaMadrid y mercaBarna se comprueba que el precio medio es mayor en el segundo. Este fenómeno justificó la decisión de utilizar fondos covid en el campo catalán para modernizar el regadío y digitalizar el sector.
        
        """)

        st.markdown("""
        En la otra cara de la moneda se encontraba Andalucía con el caso de las fresas de Huelva. Como se explicaba en el análisis 1, el inicio de la crisis sanitaria y la época de recolección coincidieron desencadenando graves problemas en la producción como consecuencia de la falta de mano de obra estacional y, por lo tanto, bajadas en los precios. Todo ello queda perfectamente reflejado en el informe que presentamos a continuación.
        
        """)

        st.markdown("##")

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjYyNDYyYzctZWI3Yy00NDFiLWI3YmMtYjM2NTgxNTkwZTM0IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9&amp;pageName=ReportSectionab929194a7fa9d1d65ba",height=635,width=1200)


    elif choice == "Análisis 3":
        st.header('¿Qué efecto ha tenido sobre las importaciones/exportaciones de F&H?¿Ha tenido algún efecto especial el periodo de excepción (Marzo, abril y mayo)?')
        
        st.markdown('##')

        if st.checkbox('Ver Jupyter Notebook'):
            HtmlFile = open('./data/analisis/a3/comercio_exterior.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=650, scrolling=True)
        else:
            pass
            
        
        st.markdown('##')

        st.markdown("""
        España fue el primer exportador hortofrutícula de toda la unión europea en el año 2020 y tercero mundial ya que sólo la superan EEUU y China. La mitad de la producción nacional se exporta fuera de nuestras fronteras y principalmente a la Unión Europea sobre todo las hortalizas de invierno además de los cítricos, como hemos podido observar en otro análisis del reto, han subido su demanda debido a la pandemia.
        
        """)

        st.markdown("""
Durante el periodo de enero-diciembre de 2020 y con una pandemia de por medio, el sector agroalimentario español no sólo no redujo sus exportaciones, sino que creció un 5,4% más con respecto al mismo periodo de 2019. En concreto las exportaciones de frutas y hortalizas crecieron en torno a un 7,7% en conjunto. Todo ello con el impacto inicial que causó la covid-19 en el saldo comercial durante los dos primeros meses de la pandemia y que causó el cierre de las fronteras de los países de la UE y su evolución como veremos mas adelante con el auge de España en las exportaciones. En el siguiente PowerBI podemos observas las importaciones/exportaciones de los distintos paises de la UE con respecto a España.
        
        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZTE0YTU3NjctNzg1ZC00NTlhLTk4YmYtZDQ2NzZkZDczNzc2IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

        st.markdown('##')

        st.markdown("""
        Como podemos observar, los países que más frutas y hortalizas importaron de España durante el periodo de marzo a noviembre fueron: Alemania, Francia, Holanda, Italia y Portugal. Sin embargo, la mayor parte de las transacciones se produjeron a partir de mayo como hemos mencionado anteriormente tras empezar la desescalada generalizada por parte de todos los países de la unión. Por ejemplo, en Alemania el 67,8% de las importaciones provenientes de España durante el periodo mencionado anteriormente se produjeron a partir de dicho mes clave para la desescalada. Por otro lado, aquellos países que más frutas y hortalizas exportaron hacia España fueron Francia, Portugal, Países Bajos e Italia.
        """)

        st.subheader("¿Por qué ocurrió el boom exportador de España a la UE durante el final de la cuarentena?")

        st.markdown("""
        Durante los peores meses del confinamiento que fueron marzo y abril para el sector (dado que la cadena de suministro agroalimentaria está integrada y opera a través de las fronteras) el cierre fronterizo bloqueó el suministro y perturbó terriblemente la actividad durante estos meses tanto a nivel logístico como a nivel productivo. Al ser un sector donde los trabajadores suelen ser jornaleros de origen inmigrante y estar restringido el movimiento de personas entre países provocó una escasez de mano de obra. Estos obstáculos acabaron desencadenando en una rotura de stock en ciertas frutas y hortalizas en la Unión Europea sobre todo en los cítricos, fruta que España es la que más exporta a la UE y que aumentó su demanda exponencialmente durante el confinamiento. Por ello en mayo, cuando se empezaron a relajar las medidas y a abrir las fronteras entre países a través de corredores especiales para evitar desabastecimiento en la UE, España experimentó un crecimiento exponencial de su exportaciones de las frutas y hortalizas.
        
        """)

        st.markdown("""
        La necesidad de importar frutas y hortalizas por parte de los distintos países y el cambio de patrones de consumo provocó que el balance comercial en el sector agroalimentario de España cerrase 2020 en positivo con 14.025 millones de euros aproximadamente. Para concluir, la exportación de hortalizas en nuestro país durante 2020 creció un 4,6%. Por otro lado, la exportación de frutas en ese mismo periodo creció un 10% más que en 2019. El valor de los productos más exportados fue el de los cítricos debido a que durante la covid-19 ha aumentado el consumo de productos ricos en vitaminas debido al confinamiento domiciliario y una alimentación más saludable.
        
        
        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZmIxNTM4N2EtZGQ3NS00ZmYyLWIxNTctYjEwMjRhNGE0ODEzIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)


    elif choice == "Análisis 4":
        st.header(
            '¿Existe correlación entre los casos de COVID-19 y las importaciones/exportaciones a nivel de la Unión Europea?')

        st.markdown('##')

        if st.checkbox('Ver Jupyter Notebook'):
            HtmlFile = open('./data/analisis/a4/covid_19_comercioExt.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=650, scrolling=True)
        else:
            pass

        st.markdown('##')

        st.markdown("""
        Tras realizar un estudio de correlaciones entre los datos de la COVID-19 y el comercio exterior en la Unión Europea se ha llegado a la conclusión de que existe una correlación positiva entre el número de casos y las importaciones/exportaciones. Obteniendo resultados diferentes si comparamos los casos con el valor de la transacción o el número de kilos exportados/importados:
        
        """)

        st.markdown('##')

        st.image('./img/img4.png', use_column_width=True)

        st.markdown('##')

        st.markdown("""
        La correlación entre el número de kilos importados por parte de España desde los distintos países de la UE es de 0.28. Por otro lado, la correlación entre el número de kilos exportados por España a los diferentes países de la UE aumenta hasta 0.32 . Es decir, por cada 100 kg de frutas o verduras exportadas había en torno a 32 casos de Covid-19 en Europa. Además, comparando el valor en euros de las importaciones/exportaciones con el número de casos se ha obtenido prácticamente el mismo grado de correlación, por cada euro en comercio exterior se incrementa el número de casos en 0.26
        
        """)

        st.header("¿ A qué podría deberse estos resultados con respecto a la correlación y España?"
        
        )

        st.markdown("""
        Los diferentes ritmos de la recuperación de los distintos países de la Unión Europea durante el primer confinamiento domiciliario, sumado a las restricciones de movilidad, la escasa mano de obra, la dificultad logística y el gran problema de la rotura de stock además de la mayor demanda de consumo de F&H en toda la UE debido a una mejora de los hábitos alimenticios debido al mayor sedentarismo que suponía el confinamiento domiciliario, generó una fuerte dependencia hacia las importaciones por parte de los distintos países de la Unión Europea, sobre todo con respecto a España. Por ello la correlación aunque sea débilmente positiva, es suficiente para poder realizar hipótesis sobre ella. Los corredores especiales durante la desescalada, además de la conocida capacidad productiva de F&H en España supusieron una dependencia al comercio exterior por parte de los países europeos al no poder satisfacer la demanda nacional con su producción. 
        
        
        """)

        st.markdown('##')

        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZmIxNTM4N2EtZGQ3NS00ZmYyLWIxNTctYjEwMjRhNGE0ODEzIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)



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
