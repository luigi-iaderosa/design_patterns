import string
from random import randint
from Structural.Adapter.Weapons.Weapon import Weapon


class Helmet(Weapon):
    def __init__(self, name='Helmet'):
        super().__init__(name)

    def provide_damage(self):
        classes = string.ascii_lowercase[0:10]
        return classes[randint(0,10)]