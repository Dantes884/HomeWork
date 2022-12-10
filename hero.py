# we are the heroes

class SuperHero:
    people = 'people'                                                                          #1
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower                                                           #2
        self.health_points = health_points
        self.catchphrase = catchphrase
    def run(self):
        print(f'The real name is {self.name}.')                                                #3
    def hp(self):
        self.health_points *= 2                                                                #4
    def __str__(self):
        return (f'Known as {self.nickname} \n'
                f'His Superpower - {self.superpower} \n'                                       #5
                f'HP - {self.health_points}')
    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Shen', 'The eye of Twilight', 'Twilight sword', 610, 'Demonstration of superior jugdment.')
hero.run()
hero.hp()
print(hero)
print(len(hero))

class TreeHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def hp(self):
        self.health_points **= 2
        self.fly = True
    def fly_phrase(self):
        print('fly in the True_phrase')

tree = TreeHero('Maokai', 'The Twisted Treant', "Nature's Grasp", 635, 'The islands will bloom again.')
tree.run()
tree.hp()
print(tree)
print(len(tree))
tree.fly_phrase()
class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def hp(self):
        self.health_points **= 2
        self.fly = True
    def fly_phrase(self):
        print(f'fly in the {self.fly}_phrase')

earth = EarthHero('Sett', 'The Boss', 'Haymaker', 670, "I'm undisputed.")
earth.run()
earth.hp()
print(earth)
print(len(earth))
earth.fly_phrase()

class Villian(EarthHero):
    people = 'monster'
    def gen_x(self):...
    def crit(self):
        print(f'crit damage {self ** 3}')

drake = Villian('Dragon', 'Cloud drake', 'Cloud', 5730, 'I am the dragon!')
Villian.crit(earth.damage)