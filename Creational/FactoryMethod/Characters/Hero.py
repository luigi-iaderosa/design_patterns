from random import randint

from Creational.FactoryMethod.Characters.Character import Character


class Hero (Character):
    def __init__(self,name):
        super().__init__(name)

    def attack(self):
        return self.health/5


    def defense(self):
        base_step = super().defense()
        super().restore_partially_just_because()
