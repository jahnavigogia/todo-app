import functions
import time
import PySimpleGUI as sg

clock = sg.Text('', key='clock')
label = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
window = sg.Window("My to-do App",
                   layout=[[clock], [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                           font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todo'].update(value=values['todos'][0])
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(value=todos)
            window['todo'].update(values= '')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
