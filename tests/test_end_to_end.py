import subprocess


def test_show_list():
    parameter = "list"
    expected = "There are no todos!"
    proc = subprocess.run(["startup.cmd", parameter], stdout=subprocess.PIPE, check=True, universal_newlines=True)
    actual = proc.stdout.replace("\x1b[0m", "")
    assert actual == f"{expected}\n", f"Should {expected=} have been {actual=}"
