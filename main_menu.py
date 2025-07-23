import Menu

def main_menu():
    title = "Main Menu"
    options = ["New Game", "Load Game", "Help", "Exit"]
    main_menu = Menu.Menu(title, options)

    main_menu.display()
