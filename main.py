# from functions import get_todos, write_todos # this can be used in the case of having fewer functions
 
import functions 
import time 

now = time.strftime("%b %d,%Y ; %H:%M:%S")
print("It is now", now)

# if the function file is in a different folder,
# from folder_name.file_name import function_name

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        
        # file = open('todos.txt', 'r')               # will read whatever is in the file
        # todos = file.readlines()                    # will save previous lines in the said file in a list - todos
        # file.close()                                # will close the file

        todos = functions.get_todos()
    
        todos.append(todo + '\n')

        functions.write_todos(todos)

        todos.append(todo)  # appends the new user input in the list

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]  #LIST COMPREHENSION - will strip out the '\n' from the
        # list items and save it in a new list

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)


    elif user_action.startswith('edit'):
            
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid!")
            continue
            # continue will skip the rest of the code in the loop and go back to the beginning of the loop
            # which means that the very first two lines of the loop will be executed again

    elif user_action.startswith('complete'):
            
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)  # pop takes index as argument

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)

        except IndexError:
            print("There is no todo with that number!")
            continue


    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid!')

print("Goodbye")
