def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file:
        to_do_s_local = file.readlines()
    return to_do_s_local

def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)