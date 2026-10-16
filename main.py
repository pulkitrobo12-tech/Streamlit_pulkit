import streamlit as st
a=st.text_input('enter your password')
st=0

if len(a)>8:
  st=st+1

for x in a:
  if x.isupper():
    st= st+1


st.write('final strength',st)
  



