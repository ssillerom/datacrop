import streamlit as st
import streamlit.components.v1 as stc


def app():

    menu = ["Comercio y COVID19", "Informe del comercio exterior", "Comparación de Andalucía, MercaMadrid, MercaBarna",
            "Comparativa consumo y precio", "Comparativa producción y consumo 2018,2019 y 2020"]
    choice = st.selectbox(
        "Porfavor, seleccione el reporte que desea visualizar de PowerBI: ", menu)

    if choice == "Comercio y COVID19":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiMWEzM2QzMTQtODBmZC00OWQ3LThiNjYtM2RmYzdmODg4MzJmIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

    elif choice == "Comparación de Andalucía, MercaMadrid, MercaBarna":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiOGQyNWJlYjUtYWU0Ny00OTRlLWIwNzctODMxYzA5ZDY0YjIyIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

    elif choice == "Informe del comercio exterior":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzUwMTNkNDctNDFkYi00ZDk5LWJjMmYtMGU1MDFjODZmMTBhIiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

    elif choice == "Comparativa consumo y precio":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTVkM2VjNWMtMzFiYy00NjI5LWI0NzMtZTdiZGYwODg2MDk3IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)

    elif choice == "Comparativa producción y consumo 2018,2019 y 2020":
        stc.iframe("https://app.powerbi.com/view?r=eyJrIjoiYmYzYzBlZWMtYjBmMy00ZDZiLTljM2UtMTQ3MWExNmNkMzE2IiwidCI6IjZhZmVhODVkLWMzMjMtNDI3MC1iNjlkLWE0ZmIzOTI3YzI1NCIsImMiOjl9", height=635, width=1200)
    else:
        st.info("Seleccione alguno de los Dashboards...")