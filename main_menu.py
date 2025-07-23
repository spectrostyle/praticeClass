from Menu import *


def main_menu(display):
    title = "Main Menu"
    options = ["New Game", "Load Game", "Help", "Exit"]
    navigable = True

    def handle_selection(choice):
        if choice == "New Game":
            display.print("Starting a new game...")
        elif choice == "Load Game":
            display.print("Loading game...")
        elif choice == "Help":
            display.print("Here's some help text.")
        elif choice == "Exit":
            exit()

    menu = Menu(title, options, display, navigable, when_selected=handle_selection)
    menu.display_this_menu()
