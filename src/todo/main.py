import sys

from src.todo.todo_app import TodoApp

if __name__ == "__main__":
    if sys.argv[1] == "list":
        print(TodoApp().get_todos())