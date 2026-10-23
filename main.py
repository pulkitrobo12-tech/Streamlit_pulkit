import streamlit as st

st.title('PASSWORD STRENGTH CHECKER')
st.write('By Pulkit Nagar 9-F')
a=st.text_input('enter your password')
sta=0
lowercase=0
uppercase=0
digit=0
specialcharacters=0


if len(a)>8:
  sta=sta+1

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
    digit=-1
    break

for k in a:
  if k in '!,@,#,$,%,^,&,*,(,),<,>,?,/,:,",;,[,],-,+,_,=,~,`':
    sta= sta+1
    specialcharacters=1
    break
  


if st.button('check strength'):


  st.write('final strength',sta)

  if sta==4:
    st.write("Congratulations, your password is strong")
  elif sta==3:
    st.write("Your password is moderate but it can be made stronger")
    if uppercase==0:
      st.write('You need atleast 1 uppercase letter to make it stronger')
    if lowercase==0:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    if digit==0:
      st.write('You need atleast 1 digit to make it stronger')
    if specialcharacters==0:
       st.write('You need atleast 1 special character to make it stronger')
  else:
    st.write('Your Password is weak')
    if uppercase==0:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    if lowercase==0:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    if digit==0:
      st.write('You need atleast 1 digit to make it stronger')
    if specialcharacters==0:
       st.write('You need atleast 1 special character to make it stronger')
  
  



