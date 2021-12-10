import subprocess

import pytest


def test_show_empty_list():
    parameter = "list"
    expected = "[]"
    actual = execute_todo_app(parameter)
    assert actual == f"{expected}\n", f"Should {expected=} have been {actual=}"


def execute_todo_app(parameter):
    proc = subprocess.run(["startup.cmd", parameter], stdout=subprocess.PIPE, check=True, universal_newlines=True)
    actual = proc.stdout.replace("\x1b[0m", "")
    return actual
