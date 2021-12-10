import subprocess


def test_show_empty_list():
    parameter = "list"
    expected = "[]"
    actual = execute_todo_app(parameter)
    assert actual == expected, f"Should {expected=} have been {actual=}"


def test_add_todo_to_list():
    parameter = "add"
    todo = "first"
    expected = f"Todo added: {todo}"
    actual = execute_todo_app(parameter, todo)
    assert actual == expected, f"Should {expected=} have been {actual=}"


def execute_todo_app(parameter, element=""):
    proc = subprocess.run(["startup.cmd", parameter, element], stdout=subprocess.PIPE, check=True, universal_newlines=True)
    return proc.stdout.replace("\x1b[0m", "")[:-1]
