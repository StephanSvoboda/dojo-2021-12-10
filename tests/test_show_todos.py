import subprocess


def test_test():
    expected = "Hello World"
    proc = subprocess.run(["startup.cmd", expected], stdout=subprocess.PIPE, check=True, universal_newlines=True)
    actual = proc.stdout.replace("\x1b[0m", "")
    assert actual == f"{expected}\n", f"Should {expected=} have been {actual=}"
