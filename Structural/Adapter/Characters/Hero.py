from random import randint
from string import ascii_lowercase

from Structural.Adapter.Characters.Character  import Character
from Structural.Adapter.Weapons.Helmet import Helmet


class Hero (Character):
    def __init__(self,name):
        super().__init__(name)

    def attack(self):
        print('Hero Attack - Weapon Primary: '+ str(self.weapon_primary.provide_damage())+' Weapon Secondary: '+str(SecondaryWeaponAdapter(self.weapon_secondary).provide_damage()))
        return self.health/5 + self.weapon_primary.provide_damage() + SecondaryWeaponAdapter(self.weapon_secondary).provide_damage()


    def defense(self):
        base_step = super().defense()
        super().restore_partially_just_because()

class SecondaryWeaponAdapter(Helmet):
    def __init__(self,helmet):
        super().__init__()
        self.helmet = helmet
        
    def provide_damage(self):
        provided_damage = self.helmet.provide_damage()
        return ascii_lowercase.index(provided_damage)
