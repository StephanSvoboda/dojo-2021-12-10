import json


class TodoApp:

    def __init__(self, todos=None):
        if todos is None:
            todos = []
        self.__todos = todos

    def get_todos(self):
        return self.__todos

    def add(self, todo):
        self.__todos.append(todo)
        self.__persist()

    def __persist(self):
        with open("todo_app.db", "w") as todo_db:
            json.dump(self.get_todos(), todo_db)

    def load(self):
        with open("todo_app.db", "r") as todo_db:
            self.__todos = json.load(todo_db)
