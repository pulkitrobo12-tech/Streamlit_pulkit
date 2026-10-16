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
    break

for x in a:
  if x.isdigit():
    sta= sta+1
    break

for x in a:
  if x in '!,@,#,$,%,^,&,*,(,),<,>,?,/,:,",;,[,],-,+,_,=,~,`':
    sta= sta+1
    break


st.write('final strength',sta)

if sta==5:
  sta="Congratulations"
  



