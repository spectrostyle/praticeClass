# add commands fight/run
from main import *


def battle(contestant):
    contestants = [contestant[0], contestant[1]]

    attacker = contestant[0]
    target = contestant[1]

    print("Battle starting!")
    while attacker.alive or target.alive:

        print(f"{contestants[0].name} is attacking...")

        if attacker.name == contestants[0].name:
            input("Press to continue...")

        fight(attacker, target)

        if attacker.alive is False or target.alive is False:
            #func 'win message'?
            print("----")
            print(f"Battle ended, with {attacker.name} as victor")
            print("----")
            break
        else:
            contestants.reverse()


def fight(attacker, target):
    attacker.attack(target)
