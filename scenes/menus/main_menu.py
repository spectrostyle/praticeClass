from Classes import Menu
from scenes import sceneManager


def main_menu(mainWindow):
    title = "Main Menu"

    options = ["New Game", "Load Game", "Help", "Exit"]

    navigable = True

    def handle_selection(choice):
        if choice == "New Game":
            """display.print("Starting a new game...")
            char_gen.get_char(display)"""
        elif choice == "Load Game":
            """save_menu(display)"""
        elif choice == "Help":
            sceneManager.switch_scenes("help_menu", mainWindow)
        elif choice == "Exit":
            exit()

    mainMenu = Menu.Menu(title, options, mainWindow, navigable, when_selected=handle_selection)
    mainMenu.display_this_menu()
