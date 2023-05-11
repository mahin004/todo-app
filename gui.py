import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do: ')
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# layout expects a list parameter
# items put in the inner sq brackets in 'layout' will be placed in a single row'


window.read()
window.close()
