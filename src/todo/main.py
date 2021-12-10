import sys

from src.todo.todo_app import TodoApp

if __name__ == "__main__":
    app = TodoApp()
    if sys.argv[1] == "list":
        print(app.get_todos())
    elif sys.argv[1] == "add":
        app.add(sys.argv[2])
        print(f"Todo added: {app.get_todos()[-1]}")
    elif sys.argv[1] == "init":
        app.init()