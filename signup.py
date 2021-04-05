import streamlit as st
from utils import add_userdata,create_usertable,login_user,make_hashes,check_hashes

st.subheader("Crear nueva cuenta")
new_user = st.text_input("Username")
new_password = st.text_input("Password",type='password')

if st.button("Signup"):
	create_usertable()
	add_userdata(new_user,make_hashes(new_password))
	st.success("You have successfully created a valid Account")
	st.info("Go to Login Menu to login")