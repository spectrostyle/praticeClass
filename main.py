import Char


def get_char():
    name = input("name: ")
    return Char.Char(name)


def fight(attacker, target):
    attacker.attack(target)


def main():
    me = get_char()
    enemy = get_char()

    contestants = [me, enemy]

    while me.alive or enemy.alive:
        fight(contestants[0], contestants[1])
        if me.alive is False or enemy.alive is False:
            print("over")
            break
        else:
            contestants.reverse()


if __name__ == '__main__':
    main()
