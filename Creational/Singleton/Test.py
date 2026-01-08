from Creational.Singleton.Characters.Boss import Boss
from Creational.Singleton.Characters.Hero import Hero


class Test:

    def play(self):
        heroes_number = 3
        heroes = []
        heroes_names = ['knight','cleric','mage']
        boss = None
        for i in range(heroes_number):
            heroes.append(Hero(heroes_names[i]))

        for i in range(heroes_number):
            boss = Boss.get_instance() #ragionevolmente sarà instanziato solo la prima volta, ma noi non gestiamo direttamente l'instanziazione né tantomeno ci frega qualcosa di vedere se stiamo o non stiamo creando altre istanze
            heroes[i].set_target(boss)
            boss.set_target(boss)
            boss.defense()
            heroes[i].defense()

        for i in range(heroes_number):
            heroes[i].print_status()
            boss.print_status()
            print(' ')






