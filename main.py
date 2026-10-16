import streamlit as st
a=st.text_input('enter your password')
sta=0

if len(a)>8:
  sta=sta+1

for x in a:
  if x.isupper():
    sta= sta+1

for y in a:
  if y.islower():
    sta= sta+1

st.write('final strength',sta)
  



