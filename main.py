import streamlit as st
a=st.text_input('enter your password')
sta=0

if len(a)>8:
  sta=sta+1

for x in a:
  if x.isupper():
    sta= sta+1
    break

for y in a:
  if y.islower():
    sta= sta+1
    break

for j in a:
  if j.isdigit():
    sta= sta+1
    break
  

for k in a:
  if k in '!,@,#,$,%,^,&,*,(,),<,>,?,/,:,",;,[,],-,+,_,=,~,`':
    sta= sta+1
    break
  


if st.button('check strength'):


  st.write('final strength',sta)

  if sta==5:
    st.write("Congratulations, your password is strong")
  elif sta>=3 and sta <5:
    st.write("Your password is not weak but it can be made stronger")
  else:
    st.write('Your Password needs improvement')
  
  



