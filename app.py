import streamlit as st
st.title("Логин система")
name = st.text_input("Въведи име")
  if st.button("Провери")
    if name.strip ()=="":
      st.warning("Моля въведи текст")
  elif not name is alpha():
  st.warning("----")
    else st.success("Текстът е въведен правилно")
