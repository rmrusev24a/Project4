import streamlit as st

st.title("Логин система")
name = st.text_input("Въведи име")
age = st.number_input("Въведи години")
if st.button("Провери"):
    if name.strip() == "":
        st.warning("Моля въведи текст")
    elif not name.isalpha():
        st.warning("Името трябва да съдържа само букви")
     elif age < 18:
        st.error("Трябва да имаш навършени 18 години")
    else:
        st.success("Достъпът е разрешен. Добре дошъл!")
