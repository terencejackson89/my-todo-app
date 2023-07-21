import todo_functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as file:
        pass

sg.theme("DarkGreen3")

time_label = sg.Text(key='Time', font=13)
label = sg.Text("Enter a to-do")
input_box = sg.InputText(tooltip="Enter To-Do", key='to-do')
add_button = sg.Button("Add", size=5,
                       tooltip="Add a todo", key="Add")

list_box = sg.Listbox(values=todo_functions.read_tasks(), key='to-dos',
                      enable_events=True, size=(40, 10))

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit")

window = sg.Window("To-Do App",
                   layout=[[time_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    window['Time'].update(time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = todo_functions.read_tasks()
            new_todo = values['to-do'].capitalize() + '\n'
            todos.append(new_todo)
            todo_functions.write_tasks(todos)
            window['to-dos'].update(values=todos)
        case 'Edit':
            try:
                todos = todo_functions.read_tasks()
                list_todo = values['to-dos'][0]
                input_todo = values['to-do'].capitalize() + '\n'
                idx = todos.index(list_todo)
                todos[idx] = input_todo
                todo_functions.write_tasks(todos)
                window['to-dos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a task to edit", title="Message", font=("Times New Roman", 16))
        case 'Complete':
            try:
                todo = values['to-dos'][0]
                todos = todo_functions.read_tasks()
                todos.remove(todo)
                todo_functions.write_tasks(todos)
                window['to-dos'].update(values=todos)
                window['to-do'].update(value='')
            except IndexError:
                sg.popup("Please select a task to complete", title="Message", font=("Times New Roman", 16))
        case "Exit":
            break
        case 'to-dos':
            window['to-do'].update(value=values['to-dos'][0].strip())
        case sg.WIN_CLOSED:
            break

window.close()
