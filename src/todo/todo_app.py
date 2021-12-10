class TodoApp:

    def __init__(self, todos=None):
        if todos is None:
            todos = []
        self.__todos = todos

    def get_todos(self):
        return self.__todos

    def add(self, todo):
        self.__todos.append(todo)
