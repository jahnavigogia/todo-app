import streamlit as st
import functions

todos = functions.get_todos()
st.title("My to-do app")
st.subheader("This is a to-do app.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label= "", placeholder= Add new todo)
st.date_input()