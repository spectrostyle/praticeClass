import Menu

def main_menu(display):
    title = "Main Menu"
    options = ["New Game", "Load Game", "Help", "Exit"]

    main_menu = Menu.Menu(title, options, display)

    main_menu.display_this_menu()
