from random import randint


class Character:
    def __init__(self, name):
        self.name = name
        self.target = None
        self.health = 100
        self.attack_force = None

    def set_target(self,foe):
        self.target = foe
    def get_target(self):
        return self.target

    def attack(self):
        pass

    # banalmente, defense è il meccanismo con cui si scala dal bersaglio la salute relativa alla logica d'attacco
    def defense(self):
        self.health -= self.target.attack()
        return self.health

    def restore_partially_just_because(self):
        defence_bonus_seed = randint(5, 25)
        if self.health < 30:
            if defence_bonus_seed % 2 == 0:
                print(self.name + ' got def bonus!')
                self.health += defence_bonus_seed
            else:
                print(self.name + ' got no def bonus!')