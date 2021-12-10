from src.todo.todo_app import TodoApp


def test_retrieve_empty_list_of_todos():
    todo_app = TodoApp()
    assert [] == todo_app.get_todos()


def test_retrieve_list_with_todos():
    todo_app = TodoApp(todos=["first"])
    assert ["first"] == todo_app.get_todos()


def test_add_one_todo():
    todo_app = TodoApp()
    todo = "some todo"
    todo_app.add(todo)
    todo_list = todo_app.get_todos()
    assert todo in todo_list
    assert 1 == len(todo_list)


def test_add_many_todos():
    todo_app = TodoApp()
    todo = "some todo"
    todo_app.add(todo)
    todo2 = "stephan"
    todo_app.add(todo2)
    todo_list = todo_app.get_todos()
    assert todo in todo_list
    assert todo2 in todo_list
    assert 2 == len(todo_list)


def test_write_todos():
    """
    This is an integration test
    :return:
    """
    todo_app = TodoApp()
    todo = "persist 1"
    todo_app.add(todo)
    todo_app2 = TodoApp()
    todo_app2.load()
    todo_app3 = TodoApp()
    todo_app3.load()
    todo_app3.add("persist 2")
    todo_app2.load()
    assert len(todo_app2.get_todos()) == 2

