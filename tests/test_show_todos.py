import sys
from io import StringIO


def test_test():
    sys.stdout = StringIO()
    expected = "Hello World"
    print("Hello World", end="")
    actual = sys.stdout.getvalue()
    assert expected == actual, f"Should {expected=} have been {actual=}"
