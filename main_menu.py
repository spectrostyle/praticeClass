from Menu import *


def main_menu(display):
    title = "Main Menu"
    options = ["New Game", "Load Game", "Help", "Exit"]
    navigatable = True

    menu = Menu(title, options, display, navigatable)

    menu.display_this_menu()
