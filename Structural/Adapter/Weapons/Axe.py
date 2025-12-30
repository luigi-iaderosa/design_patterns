from Structural.Adapter.Weapons.Weapon import Weapon
from random import randint

class Axe(Weapon):
    def __init__(self, name='Axe'):
        super().__init__(name)

    def provide_damage(self):
        return randint(1, 10)