import streamlit as st
a=st.number_input('enter your first number')
b=st.number_input('enter your second number')
st.title("My first Streamlit app")

st.write("Hello ! Creating a simple web app using streamlit.")
st.write('The sum is',a+b)



