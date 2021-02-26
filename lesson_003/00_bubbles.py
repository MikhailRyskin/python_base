# -*- coding: utf-8 -*-

import simple_draw as sd


def color_bubble(x, y, shift, color):
    center_point = sd.get_point(x, y)
    radius = 50
    for _ in range(3):
        sd.circle(center_point, radius, color)
        radius += shift


sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center_position = sd.get_point(200, 100)
radius = 50
for _ in range(3):
    sd.circle(center_position, radius)
    radius += 5
sd.sleep(seconds=5)
sd.clear_screen()

# Написать функцию рисования пузырька, принимающую 3 (или более) параметра: точка рисования, шаг и цвет
x = 400
y = 400
shift = 10
color = (255, 0, 255)
color_bubble(x, y, shift, color)
sd.sleep(seconds=5)
sd.clear_screen()
# Нарисовать 10 пузырьков в ряд
x = 100
y = 250
shift = 5
color = (255, 127, 0)
for _ in range(10):
    color_bubble(x, y, shift, color)
    x += 80
sd.sleep(seconds=5)
sd.clear_screen()
# Нарисовать три ряда по 10 пузырьков
for _ in range(3):
    x = 70
    for _ in range(10):
        color_bubble(x, y, shift, color)
        x += 80
    y += 120
sd.sleep(seconds=5)
sd.clear_screen()
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    x = sd.random_number(50, 1100)
    y = sd.random_number(50, 550)
    shift = sd.random_number(3, 10)
    color = sd.random_color()
    color_bubble(x, y, shift, color)

sd.pause()

# зачет!
