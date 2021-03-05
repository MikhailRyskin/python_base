# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def triangle(point, angle=0, length=200, color=sd.COLOR_YELLOW):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=color)


def square(point, angle=0, length=200, color=sd.COLOR_YELLOW):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color=color)


def pentagon(point, angle=0, length=200, color=sd.COLOR_YELLOW):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw(color=color)


def hexagon(point, angle=0, length=200, color=sd.COLOR_YELLOW):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=color)

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw(color=color)


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)


print('Возможные фигуры:\n'
      '   0 : треугольник\n   1 : квадрат\n   2 : пятиугольник\n   3 : шестиугольник')

point_center = sd.get_point(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100)

while True:
    figure_number = int(input('Введите желаемую фигуру: '))
    if figure_number == 0:
        triangle(point=point_center)
    elif figure_number == 1:
        square(point=point_center)
    elif figure_number == 2:
        pentagon(point=point_center)
    elif figure_number == 3:
        hexagon(point=point_center)
    else:
        print('Вы ввели некорректный номер!')
        continue
    break

sd.pause()
