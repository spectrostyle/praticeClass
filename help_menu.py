from main_menu import *


def help_menu(display):
    title = "Help Menu"

    help_text = "PLACE HOLDER"

    options = [f"{help_text}", "exit"]
    navigable = False

    def handle_selection(choice):
        pass

    menu = Menu(title, options, display, navigable, when_selected=handle_selection)
    menu.display.print(f"{help_text}")
