import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] +'\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title(" TO~DO App ")
st.subheader("User friendly App for all age groups")
st.write("This App Increases Your Productivity")

for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add New Todo....",
              on_change=add_todo, key='new_todo')
