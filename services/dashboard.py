import streamlit as st
import streamlit.components.v1 as stc


def app():

    st.header('¡Bienvenido! Aqui podrá consultar todos los PowerBI usados en los análisis de forma sencilla')

    menu = ["Variación consumo y precio por producto y CCAA","Consumo y producción anual y nacional por producto",
           "Precios medios nacionales por producto y semana del 2020","Comparación precio Andalucia, MercaMadrid, MercaBarna",
           "Patrones de consumo: Canales físicos VS Canales online","Evolución consumo 2020 por lugar de compra",
           "Penetración (%) por producto y lugar de compra","Informe del comercio exterior","Comercio y COVID19",
           "Composición química de la atmósfera"]
    choice = st.selectbox(
           "Por favor, seleccione el reporte de PowerBI que desea visualizar: ", menu)

    if choice == "Variación consumo y precio por producto y CCAA":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiMjc0ODAzMjgtOWEwNS00MjVkLWIzZTUtNTUwNjc1Mjc1YjAxIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height=635,width=1200)
    elif choice == "Consumo y producción anual y nacional por producto":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZGVkNDBhMzUtYTU4YS00MWVkLWEwNjYtYzRlY2ZiMTVmODhhIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height = 635, width = 1200)    
    elif choice == "Precios medios nacionales por producto y semana del 2020":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiNDZlZDcwODItMjZjNy00ZmZjLTllNDktOTk1ODU3MjM5YjE4IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height = 635, width = 1200)
    elif choice == "Comparación precio Andalucia, MercaMadrid, MercaBarna":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjYyNDYyYzctZWI3Yy00NDFiLWI3YmMtYjM2NTgxNTkwZTM0IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height = 635, width = 1200)
    elif choice == "Patrones de consumo: Canales físicos VS Canales online":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiNWNiNjM1YjItMzZmYi00MDgxLWI4MTQtMTJhMjlhZDgxNTAyIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height= 635, width = 1200)
    elif choice == "Evolución consumo 2020 por lugar de compra":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiMjIwOGEwNWItZWNhYy00NmYyLWFjODEtMzRlOTg2YjkyZTg3IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height = 635, width = 1200)
    elif choice == "Penetración (%) por producto y lugar de compra":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiMDdhMjk5ZDUtOTBkMy00ZTQwLTg5YmUtYmQ1NTFjN2E1MGQwIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height=635,width=1200)
    elif choice == "Informe del comercio exterior":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiODRhNzg2MTktMzE4MC00N2M5LTk2ZmYtMWEyYzg3OTc1NjNiIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height = 635, width=1200)
    elif choice == "Comercio y COVID19":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZmIxNTM4N2EtZGQ3NS00ZmYyLWIxNTctYjEwMjRhNGE0ODEzIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height = 635,width=1200)
    elif choice == "Composición química de la atmósfera":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiZTNhNTQ2ZGYtNjcxNy00OTA1LWFmMDItOWI5ZTlmMjk3YjhlIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9",height = 635,width = 1200)
    

    hide_footer_style = """
        <style>
        .reportview-container .main footer {visibility: hidden;}    
        """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
