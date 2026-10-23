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
    break
  else:
    uppercase=1

for y in a:
  if y.islower():
    sta= sta+1
    break
  else:
    lowercase=1
    

for j in a:
  if j.isdigit():
    sta= sta+1
    break
  else:
    digit=1

for k in a:
  if k in '!,@,#,$,%,^,&,*,(,),<,>,?,/,:,",;,[,],-,+,_,=,~,`':
    sta= sta+1
    break
  else:
    specialcharacters=1
  


if st.button('check strength'):


  st.write('final strength',sta)

  if sta==5:
    st.write("Congratulations, your password is strong")
  elif sta>=3 and sta <5:
    st.write("Your password is moderate but it can be made stronger")
    if uppercase==1:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    elif lowercase==1:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    elif digit==1:
      st.wrtite('You need atleast 1 digit to make it stronger')
    else:
       st.wrtite('You need atleast 1 special character to make it stronger')
  else:
    st.write('Your Password is weak')
    if uppercase==1:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    elif lowercase==1:
      st.write('You need atleast 1 lowercase letter to make it stronger')
    elif digit==1:
      st.wrtite('You need atleast 1 digit to make it stronger')
    else:
       st.wrtite('You need atleast 1 special character to make it stronger')
  
  



