from Classes.Display import *
from scenes import sceneManager


def main():
    mainWindow = Display()

    starting_menu = sceneManager.start(mainWindow)
    
    mainWindow.run()


if __name__ == '__main__':
    main()
