from rich import console
from datetime import datetime


k_console = console.Console(highlight=False)

# overriding builtin print function with rich print
print = k_console.print


def warn(content):
    string = f"[{datetime.now()}] {content}"
    with open("server.log", "a") as f:
        f.write(string + "\n")
    styled = f"[yellow][{datetime.now()}] {content}[/]"
    print(styled)


def error(content):
    string = f"[{datetime.now()}] {content}"
    with open("server.log", "a") as f:
        f.write(string + "\n")
    styled = f"[red][{datetime.now()}] {content}[/]"
    print(styled)


def log(content):
    string = f"[{datetime.now()}] {content}"
    with open("server.log", "a") as f:
        f.write(string + "\n")
    styled = f"[white][{datetime.now()}] {content}[/]"
    print(styled)


def success(content):
    string = f"[{datetime.now()}] {content}"
    with open("server.log", "a") as f:
        f.write(string + "\n")
    styled = f"[green][{datetime.now()}] {content}[/]"
    print(styled)


def message(content):
    string = f"[{datetime.now()}] {content}"
    with open("server.log", "a") as f:
        f.write(string + "\n")
    styled = f"[blue][{datetime.now()}] {content}[/]"
    print(styled)
