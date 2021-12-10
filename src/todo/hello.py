import click


@click.command("hello")
def hello():
    print("Hello World!")


@click.command("hugo")
def hugo():
    print("Hello Hugo!")


if __name__ == "__main__":
    hello()