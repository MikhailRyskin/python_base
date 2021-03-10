# -*- coding: utf-8 -*-


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


import simple_draw as sd
from snowfall import get_snowflakes, draw_snowflakes, shift_snowflakes, off_screen_snowflakes, removing_snowflakes


sd.resolution = (1200, 600)

# создать_снежинки(N)
number_snowflakes = 20

get_snowflakes(number_snowflakes)
while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflakes(color=sd.background_color)
    #  сдвинуть_снежинки()
    shift_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    draw_snowflakes(color=sd.COLOR_WHITE)
    sd.finish_drawing()
    #  если есть номера_достигших_низа_экрана() то
    if off_screen_snowflakes():
        #  удалить_снежинки(номера)
        off_screen_count = removing_snowflakes()
        #  создать_снежинки(count)
        get_snowflakes(number=off_screen_count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
