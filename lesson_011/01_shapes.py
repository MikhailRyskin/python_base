# -*- coding: utf-8 -*-


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.

import simple_draw as sd


def get_polygon(number_sides):
    def polygon(start_point, angle, side_length):
        start_point_0 = start_point
        for vector_angle in range(angle, angle + 360, 360 // number_sides):
            v = sd.get_vector(start_point=start_point, angle=vector_angle, length=side_length, width=3)
            v.draw()
            start_point = v.end_point
        sd.line(start_point, start_point_0, color=sd.COLOR_ORANGE, width=5)
    return polygon


draw_triangle_3 = get_polygon(number_sides=3)
draw_triangle_3(start_point=sd.get_point(100, 100), angle=13, side_length=100)

draw_triangle_4 = get_polygon(number_sides=4)
draw_triangle_4(start_point=sd.get_point(300, 300), angle=45, side_length=70)

draw_triangle_6 = get_polygon(number_sides=6)
draw_triangle_6(start_point=sd.get_point(500, 200), angle=39, side_length=50)

sd.pause()
