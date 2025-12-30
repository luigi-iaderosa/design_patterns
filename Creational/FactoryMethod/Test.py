from Creational.FactoryMethod.Characters.Character import Character
from Creational.FactoryMethod.Characters.DarkBishop import DarkBishop
from Creational.FactoryMethod.Factories.DarkBishopFactory import DarkBishopFactory
from Creational.FactoryMethod.Factories.EttinFactory import EttinFactory
from Creational.FactoryMethod.Factories.HeroFactory import HeroFactory


class Test:
    def play(self):
        hero_factory = HeroFactory()
        ettin_factory = EttinFactory()
        dark_bishop_factory = DarkBishopFactory()

        hero = hero_factory.create_character('knight')
        ettin = ettin_factory.create_character('bob')
        dark_bishop = dark_bishop_factory.create_character('marcus aurelius')

        hero.set_target(dark_bishop)
        dark_bishop.set_target(hero)
        while hero.health > 0 and dark_bishop.health > 0:
            dark_bishop.defense()
            hero.defense()
            print(hero.health)
            print(dark_bishop.health)
            print(dark_bishop.name+' vs '+hero.name+ ' end of turn')

        print(self.and_the_winner_is(hero,dark_bishop))
        hero.restore_partially_just_because()


        hero.set_target(ettin)
        ettin.set_target(hero)
        while hero.health > 0 and ettin.health > 0:
            ettin.defense()
            hero.defense()
            print(hero.health)
            print(ettin.health)
            print(ettin.name+' vs '+hero.name+ ' end of turn')

        print (self.and_the_winner_is(hero,ettin))

    def and_the_winner_is(self,opponent1:Character,opponent2:Character):
        if opponent1.health > 0:
            return opponent1.name + ' wins'
        else:
            return opponent2.name + ' wins'

