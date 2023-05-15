import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do: ')
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font = ('Helvetica', 11))
# layout expects a list parameter
# items put in the inner sq brackets in 'layout' will be placed in a single row'

while True:
    event, values  = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()   # list of todos
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos((todos))

        case sg.WIN_CLOSED:
            break

window.close()
