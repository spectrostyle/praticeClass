from Classes import Menu


def save_menu(mainWindow):
    title = "Save Menu"

    saved_games = [1, 2, 3, 4]
    options = []

    navigable = True

    for x in saved_games:
        options.append(x)

    saveMenu = Menu.Menu(title, options, mainWindow, navigable)
    saveMenu.display_this_menu()
