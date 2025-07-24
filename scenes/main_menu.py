import Classes.Char as Char
from Classes.Menu import *
from scenes.save_menu import *
from scenes.help_menu import *
import char_gen


def main_menu(display):
    title = "Main Menu"
    options = ["New Game", "Load Game", "Help", "Exit"]
    navigable = True

    def handle_selection(choice):
        if choice == "New Game":
            display.print("Starting a new game...")
            char_gen.get_char(display)
        elif choice == "Load Game":
            save_menu(display)
        elif choice == "Help":
            help_menu(display)
        elif choice == "Exit":
            exit()

    mainMenu = Menu(title, options, display, navigable, when_selected=handle_selection)
    mainMenu.display_this_menu()
