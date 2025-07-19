import battle
import char_gen


def main():
    me = char_gen.get_char()
    enemy = char_gen.get_char()

    contestants = [me, enemy]

    battle.battle(contestants)


if __name__ == '__main__':
    main()
