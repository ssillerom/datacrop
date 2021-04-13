
import streamlit as st
import h2o
import pandas as pd
import numpy as np
from h2o.automl import H2OAutoML
import base64

h2o.init()
# Funcion descargar dataframes en csv


def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Descargar predicciones en CSV</a>'


# Funcion carga de csv
@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_csv(upload_file):
    csv = pd.read_csv(upload_file)
    return csv

# Funcion para transformar los train/test dataset en objetos de H2O a modo que pueda ingestarlos en el entrenamiento del modelo


def load_h2o(train, test):
    h2o_train = h2o.H2OFrame(train)
    h2o_test = h2o.H2OFrame(test)
    return h2o_train, h2o_test


def app():

    st.title('📈 Datacrop AutoML Advanced Service')

    st.markdown("""
    ¡Bienvenido a DAAS nuestro servicio de Machine Learning avanzado! 
    Donde podrá entrenar varios modelos a la vez y elegir cual se adapta mejor a sus datos de agricultura para hacer sus propias predicciones, de una forma fácil y sencilla.
    
    Versión: v0.2.0 Snapshot
    """)

    # PASO 1 - IMPORTAR DATOS

    st.header("1. Importar los datos :seedling:")

    # Se pide que suba los datos
    uploaded_file = st.file_uploader(
        "Por favor, cargue los datos a analizar", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.subheader("Previsualización del Dataframe")
        st.dataframe(df)
        target_list = df.columns

        # PASO 2 - SELECCIONAR PARAMETROS

        st.header("2. Parametros de AutoML :herb:")

        st.subheader(
            "Seleccione las variables que quiere incluir en su Dataframe")

        # Parametro para customizar la composicion del dataframe con el que quieres entrenar el modelo
        selected_columns = st.multiselect(
            'Si no marca ninguna por defecto se incluira todas las features de su Dataframe', target_list)

        if len(selected_columns) != 0:
            df = df.loc[:, df.columns.isin(selected_columns)]
            st.dataframe(df)
        else:
            pass

        st.subheader("¿Qué tipo de modelos quiere entrenar?")

        model_type = st.radio("", ['Clasificación', 'Regresión'])

        st.subheader(
            "Seleccione el tamaño del dataframe para entrenar los modelos: ")

        st.info("""El '%' de datos restante se usará para testear los modelos.
         (Recomendación: 75 % para entrenar 25 % para testear)

        """)

        split_size = st.slider('', 10, 90, 80, 5)

        st.subheader("Variable que quiere predecir: ")
        selected_target = st.selectbox("", target_list)

        st.subheader("Selecciona el número de modelos que desea entrenar: ")
        number_of_models = st.radio('', [5, 10, 15, 20, 25])

        if st.button("Ejecutar AutoML"):
            df_train = df.loc[:int(df.shape[0]*(split_size/100)), :]
            df_test = df.loc[int(df.shape[0]*(split_size/100)):, :]
            h2o_train, h2o_test = load_h2o(df_train, df_test)
            y = selected_target
            # if x is defined as all columns except the response, then x is not required
            x = list(h2o_train.columns)
            x.remove(y)
            if model_type == "Clasificación":
                h2o_train[y] = h2o_train[y].asfactor()
                h2o_test[y] = h2o_test[y].asfactor()
            else:
                pass
            # Run AutoML for 30 seconds
            aml = H2OAutoML(max_runtime_secs=30, max_models=number_of_models)
            aml.train(x=x, y=y, training_frame=h2o_train)

            st.success(":rocket: ¡Se han entrenado los {} modelos correctamente! :rocket:".format(
                number_of_models))

            # PASO 3 Seleccionar el modelo que mejor precisión tiene y poder hacer predicciones
            st.header("3. Modelos Entrenados :deciduous_tree:")

            st.subheader("Ranking de Modelos:")

            # Sacamos el ranking de los modelos que se han calculado con sus metricas

            lb = aml.leaderboard.as_data_frame()

            st.dataframe(lb)

            st.subheader("Modelo Ganador: :trophy:")
            st.dataframe(lb.iloc[1, :])

            # Se genera las predicciones sobre el test con el mejor modelo

            st.subheader("Predicciones del Dataframe Test :crystal_ball: ")

            preds = aml.leader.predict(h2o_test)

            pred_as_list = h2o.as_list(preds, use_pandas=True, header=True)

            df_preds = df_test.copy()

            df_preds.reset_index(inplace=True)

            df_preds = pd.concat([df_preds, pred_as_list],
                                 join="outer", axis=1)
            df_preds.drop(columns=['index'], inplace=True)

            st.write(df_preds)

            st.markdown(get_table_download_link(
                df_preds), unsafe_allow_html=True)

            # PASO 4 Exportar modelo y predicciones

            model_path = h2o.save_model(
                model=aml.leader, path="./trained_models/", force=True)

        else:
            st.warning("Esperando selección de parametros...")

    else:
        st.info("Esperando datos en formato CSV...")


# Remover el footer de made with streamlit

