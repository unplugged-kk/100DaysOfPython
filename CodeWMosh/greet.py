from tkinter import W


def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("syler")
print(message)

file = open("content.txt", "w")
file.write(message)
