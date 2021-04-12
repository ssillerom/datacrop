import sqlite3
import hashlib
import streamlit as st
import base64
import uuid
import re
import pandas as pd
from h2o.automl import H2OAutoML
from bokeh.models.widgets import Div



## Funciones necesarias para crear la base de datos de los usuarios con sqlite3 y la encriptacion de la contraseña
def create_usertable():
    conn = sqlite3.connect('datacrop_users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tablaUsuarios(username TEXT,password TEXT)')

def add_userdata(username,password):
    conn = sqlite3.connect('datacrop_users.db')
    c = conn.cursor()
    c.execute('INSERT INTO tablaUsuarios(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    conn = sqlite3.connect('datacrop_users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tablaUsuarios WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data


def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

###########

## Algunas funciones de utilidad

def open_link(url, new_tab=True):
    if new_tab:
        js = f"window.open('{url}')"  # New tab or window
    else:
        js = f"window.location.href = '{url}'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_csv(upload_file):
        csv = pd.read_csv(upload_file)
        return csv





    
