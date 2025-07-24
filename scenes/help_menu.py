from scenes.main_menu import *


def help_menu(display):
    title = "Help Menu"

    help_text = "PLACE HOLDER"

    options = [f"{help_text}", "exit"]
    navigable = False

    def handle_selection(choice):
        pass

    helpMenu = Menu(title, options, display, navigable, when_selected=handle_selection)

    helpMenu.display.print(f"{help_text}")
