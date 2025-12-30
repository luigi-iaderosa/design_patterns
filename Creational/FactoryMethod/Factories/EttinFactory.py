from Creational.FactoryMethod.Characters.Character import Character
from Creational.FactoryMethod.Characters.Ettin import Ettin
from Creational.FactoryMethod.Factories.CharacterFactory import CharacterFactory


class EttinFactory(CharacterFactory):
    def create_character(self,name: str) -> Character:
        return Ettin(name)