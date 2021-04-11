
import streamlit as st
import h2o
import pandas as pd
from h2o.automl import H2OAutoML

h2o.init()

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_csv(upload_file):
    csv = pd.read_csv(upload_file)
    return csv


def load_h2o(train, test):
    h2o_train = h2o.H2OFrame(train)
    h2o_test = h2o.H2OFrame(test)
    return h2o_train, h2o_test


def app():

    test = False

    st.title('📈 Datacrop AutoML Advanced Service')

    st.markdown("""
    ¡Bienvenido a DAAS nuestro servicio de Machine Learning avanzado! 
    Donde podrá entrenar varios modelos a la vez y elegir cual se adapta mejor a sus datos de agricultura para hacer sus propias predicciones, de una forma fácil y sencilla.
    
    Versión: v0.1.1 Snapshot
    """)

    # PASO 1 - IMPORTAR DATOS

    st.header("1. Importar los datos :seedling:")

    uploaded_file = st.file_uploader(
        "Por favor, cargue los datos a analizar", type=["csv"])
    df_test = load_csv('./data/comercioExterior_Limpio.csv')


    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.subheader("Previsualización del Dataframe")
        st.dataframe(df)
        target_list = df.columns


        # PASO 2 - SELECCIONAR PARAMETROS

        st.header("2. Parametros de AutoML :herb:")

        st.subheader("Seleccione las variables que quiere incluir en su Dataframe")

        selected_columns = st.multiselect('Si no marca ninguna por defecto se incluira todas las features de su Dataframe',target_list)

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
        number_of_models = st.radio('', [5, 10, 15,20, 25])

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

            st.success(":rocket: ¡Se han entrenado los {} modelos correctamente! :rocket:".format(number_of_models))


            # PASO 3 Seleccionar el modelo que mejor precisión tiene y poder hacer predicciones
            st.header("3. Modelos Entrenados :deciduous_tree:")

            st.subheader("Ranking de Modelos:")

            lb = aml.leaderboard.as_data_frame()

            st.dataframe(lb)

            st.subheader("Modelo Ganador: :trophy:")
            st.dataframe(lb['model_id'][:1])

            # (Optional) Evaluate performance on a test set

            st.subheader("Performance obtenido con el mejor modelo")

            perf = aml.leader.model_performance(h2o_test).as_data_frame()
            st.write(perf)

            st.subheader("Predicciones del Dataframe Test :crystal_ball: ")

            preds = aml.leader.predict(h2o_test)

            pred_as_list = h2o.as_list(preds, use_pandas=True)

            st.write(pred_as_list)

            # PASO 4 Exportar modelo y predicciones

            st.header("4.Exportar modelo y predicciones")

            model_path = h2o.save_model(model=aml.leader, path="./datacrop/automl/trained_models/", force=True)
            st.write(model_path)


        else:
            st.warning("Esperando selección de parametros...")
    elif st.button('Usar datos de prueba'):
        test = True
        df_test = load_csv('./data/comercioExterior_Limpio.csv')
    if test is True :
        st.subheader("Previsualización del Dataframe")
        st.dataframe(df_test)
        target_list = df_test.columns


        # PASO 2 - SELECCIONAR PARAMETROS

        st.header("2. Parametros de AutoML :herb:")

        st.subheader("Seleccione las variables que quiere incluir en su Dataframe")

        selected_columns = st.multiselect('Si no marca ninguna por defecto se incluira todas las features de su Dataframe',target_list)

        if len(selected_columns) != 0:
            df_test = df_test.loc[:, df_test.columns.isin(selected_columns)] 
            st.dataframe(df_test)
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
        number_of_models = st.radio('', [5, 10, 15,20, 25])

        if st.button("Ejecutar AutoML"):
            df_train = df_test.loc[:int(df_test.shape[0]*(split_size/100)), :]
            df_test = df_test.loc[int(df_test.shape[0]*(split_size/100)):, :]
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

            st.success(":rocket: ¡Se han entrenado los {} modelos correctamente! :rocket:".format(number_of_models))


            # PASO 3 Seleccionar el modelo que mejor precisión tiene y poder hacer predicciones
            st.header("3. Modelos Entrenados :deciduous_tree:")

            st.subheader("Ranking de Modelos:")

            lb = aml.leaderboard.as_data_frame()

            st.dataframe(lb)

            st.subheader("Modelo Ganador: :trophy:")
            st.dataframe(lb['model_id'][:1])

            # (Optional) Evaluate performance on a test set

            st.subheader("Performance obtenido con el mejor modelo")

            perf = aml.leader.model_performance(h2o_test).as_data_frame()
            st.write(perf)

            st.subheader("Predicciones del Dataframe Test :crystal_ball: ")

            preds = aml.leader.predict(h2o_test)

            pred_as_list = h2o.as_list(preds, use_pandas=True)

            st.write(pred_as_list)

            # PASO 4 Exportar modelo y predicciones

            st.header("4.Exportar modelo y predicciones")

            model_path = h2o.save_model(model=aml.leader, path="./datacrop/automl/trained_models/", force=True)
            st.write(model_path)


        else:
            st.warning("Esperando selección de parametros...")


    else:
        st.info("Esperando datos...")

    

