import streamlit as st
from utils import add_userdata,create_usertable,login_user,make_hashes,check_hashes

st.image("./img/logo-02.png")

st.subheader("Intranet: Crear nuevo usuario para Datacrop Agro-Analytics Advanced Platform")
new_user = st.text_input("Usuario")
new_password = st.text_input("Contraseña",type='password')

if st.button("Registrar"):
	create_usertable()
	add_userdata(new_user,make_hashes(new_password))
	st.success("Se ha creado satisfactoriamente tu cuenta {} !".format(new_user))
