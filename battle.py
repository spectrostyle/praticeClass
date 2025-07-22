def battle(contestants):
    att_round = 0
    attacker = contestants[0]
    target = contestants[1]

    print("Battle starting!")

    while attacker.alive or target.alive:

        if attacker.name == contestants[0].name:
            att_round += 1
            print("*" * 20)
            print(f"Round: {att_round}")
            print("")

            input("Press to continue...")
            select_options()

        print(f"{contestants[0].name} is attacking...")

        fight(contestants[0], contestants[1])

        if attacker.alive is False or target.alive is False:
            print("----")
            print(f"Battle ended, with {attacker.name} as victor")
            print("----")
            break
        else:
            contestants.reverse()


def fight(attacker, target):
    attacker.attack(target)


def select_options():
    options = ["fight", "run"]
    while True:
        for x in options:
            print(x)
        input()
    pass
