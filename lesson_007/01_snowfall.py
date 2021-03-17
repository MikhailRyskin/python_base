# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.random_number(sd.resolution[1], sd.resolution[1] * 2)
        self.point = sd.get_point(self.x, self.y)
        self.length = 20
        self.color = sd.COLOR_WHITE

    def move(self):
        self.y -= sd.random_number(5, 10)
        self.x += sd.random_number(-3, 3)
        self.point = sd.get_point(self.x, self.y)

    def draw(self):
        sd.snowflake(center=self.point, length=self.length, color=self.color)

    def clear_previous_picture(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)
        # sd.clear_screen()

    def can_fall(self):
        if self.y > -20:
            return True


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
flakes = []
fallen_flakes = []


def get_flakes(count=10):
    global flakes
    for flake in range(count):
        flake = Snowflake()
        flakes.append(flake)


def get_fallen_flakes():
    global flakes, fallen_flakes
    count_fallen_flakes = 0
    for ind, flake in enumerate(flakes):
        if not flake.can_fall():
            fallen_flakes.append(ind)
            count_fallen_flakes += 1
    return count_fallen_flakes


def append_flakes(count):
    global flakes, fallen_flakes
    for ind in fallen_flakes:
        del flakes[ind]
    fallen_flakes.clear()
    get_flakes(count=count)


get_flakes(count=20)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    count_fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if count_fallen_flakes:
        append_flakes(count=count_fallen_flakes)  # добавить еще сверху

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
