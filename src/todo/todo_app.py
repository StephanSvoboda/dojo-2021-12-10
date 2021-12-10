class TodoApp:

    def __init__(self, todos=list()):
        self.__todos = todos

    def get_todos(self):
        return self.__todos
