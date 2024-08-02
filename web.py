import streamlit as st
import functions

todos = functions.get_todos()

st.title("my todo app")
st.subheader("To-do App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:",placeholder="Add New Todo....")