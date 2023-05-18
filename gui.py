import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do: ')
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key = 'todos',
                      enable_events = True, size = [45,10])
# .ListBox takes a list as parameter
edit_button = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font = ('Helvetica', 11))
# layout expects a list parameter
# items put in the inner sq brackets in 'layout' will be placed in a single row'

while True:
    event, values  = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()   # list of todos
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos((todos))
            window['todos'].update(values = todos)
            # will update the listbox in real time
            window['todo'].update(value='')
            # will clear the input box


        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            # will update the todos list
            functions.write_todos(todos)

            window['todos'].update(values = todos)
            # will update the listbox in real time

        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = '')

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
