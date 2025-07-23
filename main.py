import main_menu
from battle import *
from char_gen import *

from main_menu import *

from Display import *


def main():
    window = Display()

    main_menu(window)

    window.run()

    """player = get_char()
    enemy = get_char()
    contestants = [player, enemy]
    battle(contestants)"""

    window.run()


if __name__ == '__main__':
    main()
