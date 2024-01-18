import time
import functions

to_do_s = []

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is", now)
while True:
    user_action = input("Type add, show or exit ")
    user_action = user_action.strip() + '\n'

    if user_action.startswith('add'):
        todo = user_action[4:]

        to_do_s = functions.get_todos()

        to_do_s.append(todo)

        functions.write_todos(to_do_s)

    elif user_action.startswith('show'):
        todo = user_action[5:]

        to_do_s = functions.get_todos()

        for index, item in enumerate(to_do_s):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('exit'):
        break
    else:
        print("Hey! You entered an unknown command. Try again, please.")