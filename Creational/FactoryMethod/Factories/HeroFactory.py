from Creational.FactoryMethod.Characters.Character import Character
from Creational.FactoryMethod.Factories.CharacterFactory import CharacterFactory
from Creational.FactoryMethod.Characters.Hero import Hero

class HeroFactory (CharacterFactory):

    def create_character(self,name) -> Character:
        return Hero(name)