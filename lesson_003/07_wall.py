# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x_start = -50
y_start = 0
x_end = 50
y_end = 50
number_rows = 1
while y_start < 600:
    while x_start < 600:
        left_bottom = sd.get_point(x_start, y_start)
        right_top = sd.get_point(x_end, y_end)
        sd.rectangle(left_bottom, right_top, color=sd.COLOR_YELLOW, width=1)
        x_start += 100
        x_end += 100
    number_rows += 1
    y_start += 50
    y_end += 50
    if number_rows % 2 == 0:
        x_start = 0
        x_end = 100
    else:
        x_start = -50
        x_end = 50

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
