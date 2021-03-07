# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle_0(point, angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


def square_0(point, angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()


def pentagon_0(point, angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw()


def hexagon_0(point, angle=0, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)

# point_01 = sd.get_point(150, 200)
# triangle_0(point=point_01, angle=45, length=180)
#
# point_02 = sd.get_point(400, 200)
# square_0(point=point_02, angle=15, length=150)
#
# point_03 = sd.get_point(700, 200)
# pentagon_0(point=point_03, angle=30, length=100)
#
# point_04 = sd.get_point(900, 200)
# hexagon_0(point=point_04, angle=0, length=150)

# sd.pause()

# зачет 1 части!
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

sd.sleep(seconds=3)
sd.clear_screen()


def polygon(start_point, number_sides, angle, side_length):
    #  Угол для векторов нужно рассчитать, а если нужно будет восьмиугольник?
    #  будете править код получается добавлять еще условия
    #  .
    #  Угол для рисования векторов нужно вычислить.
    #  Сделать это можно просто. Создаем переменную где вычисляем значение угла - 360 / Количество сторон
    #  .
    #  Далее в цикле используем это, как шаг.
    #  Начало цикла в нуле, но т.к у нас есть параметр угла наклона фигуры,
    #  то нужно сделать так называемую поправку на ветер :)
    #  т.е начало цикла - это параметр угла "angle"
    #  Конец цикла в 360, но опять же нужно прибавить к 360 параметр угла - 360 + angle
    #  Шаг для цикла мы рассчитали заранее, в переменной значения угла
    #  Остается только нарисовать вектора.
    #
    start_point_0 = start_point
    for vector_angle in range(angle, angle + 360, 360 // number_sides):
        v = sd.get_vector(start_point=start_point, angle=vector_angle, length=side_length, width=3)
        v.draw()
        start_point = v.end_point
    sd.line(v.end_point, start_point_0, color=sd.COLOR_ORANGE, width=5)


def triangle(point, angle=0, length=200):
    polygon(start_point=point, number_sides=3, angle=angle, side_length=length)


def square(point, angle=0, length=200):
    polygon(start_point=point, number_sides=4, angle=angle, side_length=length)


def pentagon(point, angle=0, length=200):
    polygon(start_point=point, number_sides=5, angle=angle, side_length=length)


def hexagon(point, angle=0, length=200):
    polygon(start_point=point, number_sides=6, angle=angle, side_length=length)


point_01 = sd.get_point(150, 200)
triangle(point=point_01, angle=15, length=200)

point_02 = sd.get_point(450, 200)
square(point=point_02, angle=30, length=150)

point_03 = sd.get_point(700, 200)
pentagon(point=point_03, angle=25, length=80)

point_04 = sd.get_point(950, 200)
hexagon(point=point_04, angle=30, length=100)


sd.pause()
