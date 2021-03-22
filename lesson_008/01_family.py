# -*- coding: utf-8 -*-

# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.


from termcolor import cprint
from random import randint


class House:
    total_food_eaten = 0
    total_money_earned = 0
    total_fur_coats = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30
        self.house_cat = None
        self.resident = []

    def __str__(self):
        return 'В доме: еда  {}, деньги  {}, грязь  {}, кошачий корм {}'.format(
            self.food, self.money, self.dirt, self.cat_food
        )


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return '{}, сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self, portion_food):
        if self.house.food >= portion_food:
            cprint('{} - приём пищи'.format(self.name), color='green')
            self.fullness += portion_food
            self.house.food -= portion_food
            House.total_food_eaten += portion_food
        else:
            #  Если еды нет, то голод также нужно отнять
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        house.resident.append(self)
        cprint('{} - заселение в дом'.format(self.name), color='green')

    def pick_up_cat(self, cat, house):
        self.house.house_cat = cat
        cat.house = house
        house.resident.append(cat)
        cprint('{}: У нас есть кот! Зовут {}'.format(self.name, cat.name), color='cyan')

    def petting_cat(self, cat):
        self.fullness -= 10
        self.happiness += 5
        cprint('{} - ласки кота! Кот {}'.format(self.name, cat.name), color='green')

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        self.house.dirt += 5


class Husband(Man):

    def __str__(self):
        return 'Муж - ' + super().__str__()

    def act(self):
        super().act()
        if self.fullness <= 0 or self.happiness < 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat(30)
        elif self.house.money < 60:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat(30)
        else:
            self.gaming()

    def work(self):
        self.fullness -= 10
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        House.total_money_earned += 150

    def gaming(self):
        cprint('{} играл в "Танки" целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 10


class Wife(Man):

    def __str__(self):
        return 'Жена - ' + super().__str__()

    def act(self):
        super().act()
        if self.fullness <= 0 or self.happiness < 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 7)
        if self.fullness < 30:
            self.eat(30)
        elif self.house.food <= 60:
            self.shopping()
        elif self.house.cat_food <= 20:
            self.buying_cat_food()
        elif dice == 1:
            self.buy_fur_coat()
        elif dice == 2:
            self.petting_cat(self.house.house_cat)
        else:
            self.clean_house()

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 60:
            cprint('{} сходила в магазин за едой'.format(self.name), color='blue')
            self.house.money -= 60
            self.house.food += 60
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buying_cat_food(self):
        self.fullness -= 10
        if self.house.money >= 20:
            cprint('{} купила кошачий корм'.format(self.name), color='blue')
            self.house.money -= 20
            self.house.cat_food += 20
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            cprint('{} купила шубу!!!'.format(self.name), color='cyan')
            self.house.money -= 350
            self.fullness -= 10
            self.happiness += 60
            House.total_fur_coats += 1
        else:
            cprint('{} "Нет денег на шубу!"'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} сделала уборку в доме'.format(self.name), color='blue')
        if self.house.dirt > 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0


class Cat:

    def __init__(self, name):
        self.fullness = 30
        self.house = None
        self.name = name

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(self.name, self.fullness)

    def cat_eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот поел', color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('Нет кошачьей еды', color='red')
            self.fullness -= 10

    def cat_sleep(self):
        cprint('Кот спал', color='yellow')
        self.fullness -= 10

    def tear_up_wallpaper(self):
        cprint('Кот драл обои!', color='yellow')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
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

    def __add__(self, other):
        if isinstance(other, Husband):
            cprint('{} и {} стали родителями! Надо придумать имя ребёнка.'.format(
                self.name, other.name), color='cyan')
            return Child(name=None)
        else:
            return None


class Child(Man):

    def __str__(self):
        return 'Ребёнок - ' + super().__str__()

    def act(self):
        self.house.dirt += 5
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 15:
            self.eat(10)
        else:
            self.sleep()

    def sleep(self):
        self.fullness -= 10
        cprint('{} спал'.format(self.name), color='green')


serge = Husband(name='Сережа')
masha = Wife(name='Маша')
my_sweet_home = House()
serge.go_to_the_house(my_sweet_home)
masha.go_to_the_house(my_sweet_home)
barsik = Cat(name='Барсик')
masha.pick_up_cat(barsik, my_sweet_home)

kid = masha + serge
kid.name = 'Петя'
kid.go_to_the_house(my_sweet_home)

print('В доме живут:')
for roomer in my_sweet_home.resident:
    cprint(roomer.name, color='yellow')
print(my_sweet_home)
print()

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='magenta')
    for roomer in my_sweet_home.resident:
        roomer.act()
    cprint('---------------- в конце дня ----------------', color='magenta')
    for roomer in my_sweet_home.resident:
        print(roomer)
    print(my_sweet_home)

cprint('\nВсего съедено еды {}'.format(House.total_food_eaten), color='magenta')
cprint('Всего заработано денег {}'.format(House.total_money_earned), color='magenta')
cprint('Всего куплено шуб {}'.format(House.total_fur_coats), color='magenta')

# зачет 1 части!
# зачет 2 части!
#  после реализации первой части - отдать на проверку учителю

# ####################################################### Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#

# ####################################################### Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#

# после реализации второй части - отдать на проверку учителем две ветки


# ####################################################### Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
