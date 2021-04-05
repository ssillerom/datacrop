
import streamlit as st
from utils import add_userdata,create_usertable,login_user,make_hashes,check_hashes


class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.image('./logo-02.png',width=200)
        
        username = st.sidebar.text_input("Introduzca su usuario:")
        password = st.sidebar.text_input("Introduzca su contraseña:", type='password')
        
        if st.sidebar.checkbox("Iniciar Sesión"):
            create_usertable()

            hash_passwd = make_hashes(password)

            result = login_user(username,check_hashes(password,hash_passwd))

            if result:

                st.info("¡Bienvenid@ de nuevo {}!".format(username))
                app = st.sidebar.selectbox(
                'Menú Principal',
                self.apps,
                format_func=lambda app: app['title'])
                app['function']()
            else:
                st.warning("Usuario/Contraseña incorrectos")

        else:
            st.info("Por favor, inicia sesión para ver el menú de usuario")
            st.info("Recuerde que tiene el usuario en el email")

        st.sidebar.warning("Por favor mantenga marcada la casilla para conservar la sesión")


