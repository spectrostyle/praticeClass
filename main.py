import battle
import char_gen


def main():
    player = char_gen.get_char()
    enemy = char_gen.get_char()

    contestants = [player, enemy]

    battle.battle(contestants)


if __name__ == '__main__':
    main()
