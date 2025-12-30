from Creational.FactoryMethod.Characters.Character import Character


class DarkBishop(Character):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        return self.health/4
