from Structural.Adapter.Characters.Ettin import Ettin
from Structural.Adapter.Characters.Hero import Hero
from Structural.Adapter.Weapons.Axe import Axe
from Structural.Adapter.Weapons.Helmet import Helmet


class Test:
    def play(self):
        hero = Hero('Knight')
        ettin = Ettin('Bob')
        print('Here')

        hero.weapon_primary = Axe()
        hero.weapon_secondary = Helmet()

        ettin.set_target(hero)
        hero.set_target(ettin)

        ettin.defense() # qui l'ettin si difende (innesca attacco da parte di hero e QUI ci sono potenziali problemi
        print(ettin.health)