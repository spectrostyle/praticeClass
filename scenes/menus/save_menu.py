
def save_menu(display):
    title = "Save Menu"

    saved_games = [1, 2, 3, 4]
    options = []
    navigable = True

    for x in saved_games:
        options.append(x)

    def handle_selection(choice):
        main_menu(display)
        pass

    saveMenu = Menu(title, options, display, navigable, when_selected=handle_selection)
    saveMenu.display_this_menu()
