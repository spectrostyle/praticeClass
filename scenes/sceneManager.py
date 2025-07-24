from scenes.menus import main_menu, help_menu, save_menu

scene_registry = {
    "main_menu": main_menu.main_menu,
    "help": help_menu.help_menu,
    "load_game": save_menu.save_menu,
    "exit": "exit"
}


def start(mainWindow):
    starting_menu = main_menu.main_menu(mainWindow)
    return starting_menu


def switch_scenes(text, mainWindow):
    mainWindow.clear()
    selected_scene = scene_registry[text]

    if selected_scene is "exit":
        exit()

    return selected_scene(mainWindow)
    