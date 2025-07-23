import main_menu
from main_menu import *


def save_menu(display):
    title = "Save Menu"

    saved_games = [1, 2, 3, 4]
    options = []
    navigable = True

    for x in saved_games:
        options.append(x)

    def handle_selection(choice):
        main_menu.main_menu(display)
        pass

    menu = Menu(title, options, display, navigable, when_selected=handle_selection)
    menu.display_this_menu()
