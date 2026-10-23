#Pulkit Nagar 9-F
#Agenda- Password strength checker using streamlit

import streamlit as st

st.title('PASSWORD STRENGTH CHECKER')
st.write('By Pulkit Nagar 9-F')
a=st.text_input('enter your password')
sta=0
lowercase=0
uppercase=0
digit=0
specialcharacters=0
length=0


if len(a)>=8:
  sta=sta+1
  length=1

for x in a:
  if x.isupper():
    sta= sta+1
    uppercase=1
    break

for y in a:
  if y.islower():
    sta= sta+1
    lowercase=1
    break
    

for j in a:
  if j.isdigit():
    sta= sta+1
    digit=1
    break

for k in a:
  if k in '!@#$%^&*()<>?/:;[]-+_=~`':
    sta= sta+1
    specialcharacters=1
    break
  


if st.button('check strength'):
  
  
  if a=='':
        st.warning('Please enter a password first')
  else:
        st.subheader('Password Strength Meter')
  st.progress(sta / 5)
  st.write('Strength:', sta, '/5')
  st.write('Progress:', int(sta / 5 * 100), '%')

  if sta==5:
    st.success("Congratulations, your password is strong")
  elif sta >= 3: 
    st.warning("Your password is moderate and can be made stronger")
  else:
    st.error('Your Password is weak')


  st.subheader('Suggestions')
  if uppercase==0:
      st.write('You need atleast 1 uppercase letter to make it stronger')
  if lowercase==0:
      st.write('You need atleast 1 lowercase letter to make it stronger')
  if digit==0:
      st.write('You need atleast 1 digit to make it stronger')
  if specialcharacters==0:
       st.write('You need atleast 1 special character to make it stronger')
  if length==0:
       st.write('You need atleast 8 letters in your password')

  
 


