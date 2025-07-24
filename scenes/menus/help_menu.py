from Classes import Menu


def help_menu(mainWindow):
    title = "Help Menu"

    help_text = "PLACE HOLDER"
    options = [f"{help_text}", "exit"]

    navigable = False
    

    helpMenu = Menu.Menu(title, options, mainWindow, navigable)
    helpMenu.mainWindow.print(f"{help_text}")
