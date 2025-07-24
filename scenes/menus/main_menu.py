from Classes import Menu
from scenes import sceneManager


def main_menu(mainWindow):
    title = "Main Menu"

    options = ["New Game", "Load Game", "Help", "Exit"]

    navigable = True


    mainMenu = Menu.Menu(title, options, mainWindow, navigable)
    mainMenu.display_this_menu()
