# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: координата X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(x, y, color):
    left_bottom = sd.get_point(x, y)
    right_top = sd.get_point(x + 90, y + 60)
    sd.ellipse(left_bottom, right_top, color, 2)
    left_eye = sd.get_point(x + 30, y + 40)
    sd.circle(left_eye, 3, color, 1)
    right_eye = sd.get_point(x + 60, y + 40)
    sd.circle(right_eye, 3, color, 1)
    mouth_left = sd.get_point(x + 40, y + 15)
    mouth_right = sd.get_point(x + 50, y + 15)
    sd.line(mouth_left, mouth_right, color, 1)


for _ in range(10):
    x = sd.random_number(50, 500)
    y = sd.random_number(50, 500)
    color = sd.random_color()
    smile(x, y, color)

sd.pause()

# зачет!
