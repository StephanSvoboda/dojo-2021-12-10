from src.todo.todo_app import TodoApp


def test_retrieve_empty_list_of_todos():
    todo_app = TodoApp()
    assert [] == todo_app.get_todos()

def test_retrieve_list_with_todos():
    todo_app = TodoApp(todos=["first"])
    assert ["first"] == todo_app.get_todos()
