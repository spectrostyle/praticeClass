import scenes.main_menu as main_menu
from battle import *
from char_gen import *

from scenes.main_menu import *

from Classes.Display import *


def main():
    window = Display()

    main_menu(window)

    window.run()

    """player = get_char()
    enemy = get_char()
    contestants = [player, enemy]
    battle(contestants)"""


if __name__ == '__main__':
    main()
