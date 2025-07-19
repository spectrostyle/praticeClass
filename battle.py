def battle(contestants):
    attacker = contestants[0]
    target = contestants[1]

    while attacker.alive or target.alive:
        fight(attacker, target)

        if attacker.alive is False or target.alive is False:
            print(f"Battle ended, with {attacker.name} as victor")
            break
        else:
            contestants.reverse()


def fight(attacker, target):
    attacker.attack(target)
