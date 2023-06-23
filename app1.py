from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add,edit,delete,show or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos("todos.txt")
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            td = get_todos()
            number = number - 1
            print(td[number])

            todos = get_todos("todos.txt")
            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for index,item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("complete"):
            number = (user_action[9:])
            number = int(number)

            todos = get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed."
            (message)

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is invalid.")
