import streamlit as st
import todo_functions as td


todos = td.read_tasks()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.capitalize() + '\n')
    td.write_tasks(todos)


st.title("My Todo App")
st.subheader("Here you can view, edit, and complete todo tasks!")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Default label", label_visibility="hidden",
              placeholder="Add new task", on_change=add_todo,
              key='new_todo')


st.session_state