from scenes.menus import main_menu, help_menu, save_menu

scene_registry = {
    "main_menu": main_menu.main_menu,
    "help_menu": help_menu.help_menu,
    "save_menu": save_menu.save_menu,
}


def start(mainWindow):
    starting_menu = main_menu.main_menu(mainWindow)
    return starting_menu
    

def load_scene_files():
    pass


def switch_scenes(text, mainWindow):
    mainWindow.clear()
    selected_scene = scene_registry[text]
    return selected_scene(mainWindow)
    
