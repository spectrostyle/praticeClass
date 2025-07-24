import Classes.Char as Char


def get_char(display):
    display.clear()
    display.print("test")
    name = input("name: ")
    return Char.Char(name)
