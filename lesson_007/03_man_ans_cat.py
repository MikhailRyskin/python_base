# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buying_cat_food(self):
        if self.house.money >= 50:
            cprint('{} купил кошачий корм'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning_house(self):
        cprint('{} сделал уборку в доме'.format(self.name), color='blue')
        self.house.dirt -= 100
        self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat, house):
        # TODO КОгда человек берет кота он должен привязать его к себе.
        cat.house = house
        cprint('Кот появился в доме', color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.buying_cat_food()
        elif self.house.dirt > 100:
            self.cleaning_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class Cat:
    # TODO В дом лучше добавить список жителей
    def __init__(self):
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Это кот, его сытость {}'.format(self.fullness)

    def cat_eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот поел', color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('Нет кошачьей еды', color='red')

    def cat_sleep(self):
        cprint('Кот спал', color='yellow')
        self.fullness -= 10

    def tear_up_wallpaper(self):
        cprint('Кот драл обои!', color='yellow')
        self.fullness -= 10
        self.house.dirt += 5

    def cat_act(self):
        if self.fullness <= 0:
            cprint('Кот умер!!!', color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.cat_eat()
        elif dice == 1:
            self.tear_up_wallpaper()
        else:
            self.cat_sleep()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды коту осталось {}, грязь {}'.format(
            self.food, self.money, self.cat_food, self.dirt
        )


petya = Man(name='Петя')
barsik = Cat()
my_sweet_home = House()
petya.go_to_the_house(house=my_sweet_home)
petya.pick_up_cat(cat=barsik, house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    petya.act()
    barsik.cat_act()
    print('--- в конце дня ---')
    print(petya)
    print(barsik)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
