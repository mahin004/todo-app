def get_todos(filepath = 'todos.txt'):
    """ Read the text file and return the list of 
        to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()  #todos_local is only a local variable, it is not the same as the global variable todos
    return todos_local


def write_todos(todos_arg, filepath = 'todos.txt'):
    """ Write the to-do  items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  
        # this function doesnt need a return statement as it modifies the txt file in the BG



if __name__ == "__main__":
    print("Hello from functions.py")
    ## this will only run if we run this file directly
    ## running this file from main.py will not run this print statement