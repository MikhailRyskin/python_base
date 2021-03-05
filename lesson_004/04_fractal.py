# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length, width=1)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length, width=1)
    v2.draw()
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    next_angle_1 = angle - 30
    next_angle_2 = angle + 30
    next_length = length * .75
    draw_branches(start_point=next_point_1, angle=next_angle_1, length=next_length)
    draw_branches(start_point=next_point_2, angle=next_angle_2, length=next_length)


def draw_branches_random(start_point, angle, length):
    if length < 6:
        return
    branch_rejection = sd.random_number(18, 42)
    v1 = sd.get_vector(start_point=start_point, angle=angle - branch_rejection, length=length, width=1)
    # v1.draw()
    v1.draw(color=sd.random_color())
    v2 = sd.get_vector(start_point=start_point, angle=angle + branch_rejection, length=length, width=1)
    # v2.draw()
    v2.draw(color=sd.random_color())
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    next_angle_1 = angle - branch_rejection
    next_angle_2 = angle + branch_rejection
    next_length = length * sd.random_number(60, 90) / 100
    draw_branches_random(start_point=next_point_1, angle=next_angle_1, length=next_length)
    draw_branches_random(start_point=next_point_2, angle=next_angle_2, length=next_length)


sd.resolution = (800, 600)

root_point = sd.get_point(400, 50)
point_0 = sd.get_point(400, 0)

sd.line(point_0, root_point, width=2)
draw_branches(start_point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# sd.sleep(seconds=3)
sd.clear_screen()

sd.line(point_0, root_point, width=2)
draw_branches_random(start_point=root_point, angle=90, length=100)

sd.pause()
