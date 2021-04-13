import streamlit as st
import streamlit.components.v1 as stc


def app():
    st.header(
        'Jupyter Notebook con la limpieza de todos los datasets utilizados en el reto:')
    st.subheader(
        '*Si no consigue visualizar el notebook entero, cierre el menú lateral con la pestaña superior izquierda*')
    
    menu = ['Limpieza Datasets Originales',
            'Limpieza Datasets de Enriquecimiento']

    choice = st.selectbox('Elija que Jupyter Notebook desea ver:', menu)

    if choice == 'Limpieza Datasets Originales':
        HtmlFile = open('./data/limpieza_doriginales.html',
                        'r', encoding='utf-8')
        source_code = HtmlFile.read()
        print(source_code)
        stc.html(source_code, width=1600, height=900, scrolling=True)

    elif choice == 'Limpieza Datasets de Enriquecimiento':
        st.subheader(
            'Se divide en tres Notebooks, marque cual desea visualizar:')

        col1, col2, col3 = st.beta_columns(3)

        if col1.checkbox('Limpieza para Análisis 1'):
            st.markdown(
                '*Desmarque la casilla para poder seleccionar otro notebook*')
            HtmlFile = open(
                './data/limpieza_datosproduccion.html', 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=800, scrolling=True)
        elif col2.checkbox('Limpieza para Análisis 2'):
            st.markdown(
                '*Desmarque la casilla para poder seleccionar otro notebook*')
            HtmlFile = open('./data/limpieza_lugarcompra.html',
                            'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=800, scrolling=True)

        elif col3.checkbox('Limpieza para Análisis 5'):
            st.markdown(
                '*Desmarque la casilla para poder seleccionar otro notebook*')
            HtmlFile = open(
                './data/limpieza_precionacsemanal.html', 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            stc.html(source_code, width=1400, height=800, scrolling=True)
    else:
        pass
