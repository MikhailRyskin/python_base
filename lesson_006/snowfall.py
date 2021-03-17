
#  Не проще ли хранить координаты в одном списке списков?
#  мы делали этот модуль на основе прошлых. Там были разные списки.
#  Для меня в этом есть логика. Мы работаем только с y: он меняется, выходит за экран, x не меняется.
#  Надо переделать все работающие функции. Мне кажется, проще оставить как есть.
#  Если вам так удобнее, то ваше право, но гораздо удобнее работать с общей структурой
#   потому что снежинки обычно не падают ровно вниз, соответственно изменять придется и координаты "х"
#   Например:
#   _snowflakes_coords = []
#   .
#   def create_snow(n):
#       global _snowflakes_coords
#       for c in range(n):
#           x = sd.random_number(0, sd.resolution[0])
#           y = sd.random_number(sd.resolution[1], sd.resolution[1] * 2)
#           _snowflakes_coords.append([x, y, ])
#   .
#   def move_snow():
#      global _snowflakes_coords
#      for snow in _snowflakes_coords:
#          snow[1] -= sd.random_number(5, 8)
#          snow[0] += sd.random_number(-2, 2)
#  переделал на список списков. Да, так, конечно, логичней и удобней.

import simple_draw as sd

_x_y_snowflakes = []
_off_screen_flakes = []


def get_snowflakes(number=10):
    global _x_y_snowflakes
    for c in range(number):
        x = sd.random_number(0, sd.resolution[0])
        y = sd.random_number(sd.resolution[1], sd.resolution[1] * 2)
        _x_y_snowflakes.append([x, y, ])


def draw_snowflakes(color):
    global _x_y_snowflakes
    for flake in _x_y_snowflakes:
        point = sd.get_point(flake[0], flake[1])
        sd.snowflake(center=point, length=20, color=color)


def shift_snowflakes():
    global _x_y_snowflakes
    for flake in _x_y_snowflakes:
        flake[1] -= sd.random_number(5, 10)
        flake[0] += sd.random_number(-3, 3)


def off_screen_snowflakes():
    global _x_y_snowflakes, _off_screen_flakes
    for ind, flake in enumerate(_x_y_snowflakes):
        if flake[1] < -30:
            _off_screen_flakes.append(ind)
        if _off_screen_flakes:
            return True
        else:
            return False


def removing_snowflakes():
    global _x_y_snowflakes, _off_screen_flakes
    need_new_flakes = 0
    for index in _off_screen_flakes:
        del _x_y_snowflakes[index]
        need_new_flakes += 1
    _off_screen_flakes.clear()
    return need_new_flakes
