import streamlit as st
import h2o
import pandas as pd
from h2o.automl import H2OAutoML
from utils import load_csv


def load_h2o(train,test):
    h2o_train = h2o.H2OFrame(train)
    h2o_test = h2o.H2OFrame(test)
    return h2o_train, h2o_test

def app():

    h2o.init()

    uploaded_file = st.file_uploader("Por favor, cargue los datos a analizar", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
    else:
        st.info("suba un csv")


    st.dataframe(df)
    target_list = df.columns
    st.markdown("HOLA MUNDO")
    selected_target = st.selectbox("Por favor seleccione la variable target",target_list)
    
    if st.button("Entrenar Modelo"):

        df_train = df.loc[:int(df.shape[0]*0.8),:]
        df_test = df.loc[int(df.shape[0]*0.8):,:]
        
        h2o_train, h2o_test = load_h2o(df_train,df_test)

        y = selected_target
        x = list(h2o_train.columns)  #if x is defined as all columns except the response, then x is not required
        x.remove(y)
        # For binary classification
        # df_train[y] = train[y].asfactor()
        # # test[y] = test[y].asfactor()
        # Run AutoML for 30 seconds
        aml = H2OAutoML(max_runtime_secs = 30,max_models = 5)
        aml.train(x = x, y = y, training_frame = h2o_train)
        # Print Leaderboard (ranked by xval metrics)

        lb = aml.leaderboard.as_data_frame()

        st.dataframe(lb)

        # (Optional) Evaluate performance on a test set
        perf = aml.leader.model_performance(h2o_test)

        st.write(perf)

        lb = aml.leaderboard
        lb.head(rows=lb.nrows)

        aml.leader

        preds = aml.leader.predict(test)
    
        #get_aml = h2o.automl.get_automl(aml.project_name)

        st.write(get_aml.leader)
        
        # # Predict with top model from AutoML Leaderboard on a H2OFrame called 'test'
        # prediction = get_aml.predict(h2o_test)
        pred_as_list = h2o.as_list(preds, use_pandas = True)
        st.write(pred_as_list)
    else:
        st.warning("Esperando a que elija la variable target...")

if __name__ == '__main__':
    app()