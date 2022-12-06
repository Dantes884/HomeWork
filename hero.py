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