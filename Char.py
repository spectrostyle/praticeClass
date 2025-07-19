import random


class Char:
    def __init__(self, name):
        self.name = name

        self.health = 10
        self.damage = 1

        self.accuracy = 50
        self.avoidance = 10

        self.alive = True

    def info(self):
        print(f"Character: {self.name}")
        print(f"HP: {self.health}")

    def gen_acc(self):
        return random.randint(0, self.accuracy)

    def attack(self, target):

        if self.gen_acc() > target.avoidance:
            target.health -= self.damage
            print(f"{self.name} hit {target.name}!")
        else:
            print(f"{self.name} missed {target.name}!")

        print(f"{self.name}'s Health: {self.health}")
        print(f"{target.name}'s Health: {target.health}")

        if target.health <= 0:
            target.alive = False
            print(f"{target.name} has died!")
