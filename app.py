import streamlit as st

st.title("Логин система")
name = st.text_input("Въведи име")
if st.button("Провери"):
    if name.strip() == "":
        st.warning("Моля въведи текст")
    elif not name.isalpha():
        st.warning("Името трябва да съдържа само букви")
    else:
        st.success("Текстът е въведен правилно")
