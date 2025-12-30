from Creational.FactoryMethod.Characters.Character import Character
from Creational.FactoryMethod.Characters.DarkBishop import DarkBishop
from Creational.FactoryMethod.Factories.CharacterFactory import CharacterFactory


class DarkBishopFactory(CharacterFactory):
    def create_character(self,name: str) -> Character:
        return DarkBishop(name)
    