
import streamlit as st
from utils import add_userdata,create_usertable,login_user,make_hashes,check_hashes

# Clase constructora para poner todos los servicios en linea a la vez llama a app.py donde están registradas todas las "apps" que componen la plataforma
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):


        
        st.sidebar.image('./img/logo-02.png',width=200) 
        
        username = st.sidebar.text_input("Introduzca su usuario:")
        password = st.sidebar.text_input("Introduzca su contraseña:", type='password')
        #Se hashea la contraseña introducida y se comprueba que coincide con el hash registrado para ese usuario en la base de datos
        if st.sidebar.checkbox("Iniciar Sesión"):
            create_usertable()

            hash_passwd = make_hashes(password)

            result = login_user(username,check_hashes(password,hash_passwd))
        # Si el resultado es positivo, se muestra el menú principal con todos los servicios
            if result:

                st.success("¡Bienvenid@ de nuevo {}!".format(username))
                app = st.sidebar.selectbox(
                'Menú Principal',
                self.apps,
                format_func=lambda app: app['title'])
                app['function']()
            else:
                st.warning("Usuario/Contraseña incorrectos")

        else:
            st.info("Por favor, inicia sesión para ver el menú de usuario. Recuerde que tiene el usuario en el email")
            

        st.sidebar.warning("* Mantenga marcada la casilla para conservar la sesión.")


