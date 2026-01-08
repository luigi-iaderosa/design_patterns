from random import randint

from Creational.Singleton.Characters.Character import Character


class Boss (Character):
    boss = None
    def ____init__(self,name):

        super().__init__(name)

    def attack(self):
        return self.health/5


    def defense(self):
        base_step = super().defense()

    @classmethod
    def get_instance(self):
        if self.boss is None:
            self.boss = Boss('Korax')
        return self.boss
