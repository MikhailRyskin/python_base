# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x_start = 50
y_start = 50
x_end = 350
y_end = 450
for color in rainbow_colors:
    start_point = sd.get_point(x_start, y_start)
    end_point = sd.get_point(x_end, y_end)
    sd.line(start_point, end_point, color, 4)
    x_start += 5
    x_end += 5
sd.sleep(seconds=5)
sd.clear_screen()
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x_start = 300
y_start = -100
radius = 500
center_position = sd.get_point(x_start, y_start)
for color in rainbow_colors:
    sd.circle(center_position, radius, color, 20)
    radius -= 20

sd.pause()
