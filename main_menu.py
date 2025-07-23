from Menu import *
from save_menu import *
from help_menu import *


def main_menu(display):
    title = "Main Menu"
    options = ["New Game", "Load Game", "Help", "Exit"]
    navigable = True

    def handle_selection(choice):
        if choice == "New Game":
            display.print("Starting a new game...")

        elif choice == "Load Game":
            save_menu(display)
        elif choice == "Help":
            help_menu(display)
        elif choice == "Exit":
            exit()

    menu = Menu(title, options, display, navigable, when_selected=handle_selection)
    menu.display_this_menu()
