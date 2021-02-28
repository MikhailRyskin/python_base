# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# работает верно, но надо улучшить. Создайте константы ширина и высота окна (обязательно посмотрите стиль констант
#  в PEP8). Используйте "sd.resolution = (ширина, высота)" (вы использовали эту функцию в 00_bubbles.py).
#  .
#  Затем создайте (переименуйте) константы ширина_кирпича, высота_кирпича. На основе этих 4 констант динамически
#  вычисляйте сколько уровней кладок нужно положить (первый цикл), и сколько кирпичей в 1 уровне (второй цикл).
#  .
#  Такой подход сделает ваш код гибким к размеру экрана и размеру кирпичика. Сейчас все захардкожено.
#  Пример создания константы:
#  BRICK_SIZE = sd.get_point(100, 50)
#  Это удобнее потому что к координатам можно обращаться через точку.
#  BRICK_SIZE.x - координата "х"
#  BRICK_SIZE.y - координата "y"
#  .
#  С циклом "for" вам будет проще.

#  Переделал c возможностью изменения параметров экрана и кирпича.
#  Я не совсем понял, какой тип данных возвращает sd.get_point(100, 50) и как мы к ним обращаемся.
#  return Point(x=x, y=y) ???
#  BRICK_SIZE - что это? - это был пример создания константы
#  BRICK_SIZE.x - что это? - это был пример, как можно сразу брать координаты из переменной
#  .
#  Point - класс точки экрана где "х" и "у" координаты.

# x_start = -50
# y_start = 0
# x_end = 50
# y_end = 50
# number_rows = 1
# while y_start < 600:
#     while x_start < 600:
#         left_bottom = sd.get_point(x_start, y_start)
#         right_top = sd.get_point(x_end, y_end)
#         sd.rectangle(left_bottom, right_top, color=sd.COLOR_YELLOW, width=1)
#         x_start += 100
#         x_end += 100
#     number_rows += 1
#     y_start += 50
#     y_end += 50
#     if number_rows % 2 == 0:
#         x_start = 0
#         x_end = 100
#     else:
#         x_start = -50
#         x_end = 50
# sd.sleep(seconds=5)
# sd.clear_screen()


# SCREEN_WIDTH = 1020
# SCREEN_HEIGHT = 630
# sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
# BRICK_SIZE = sd.get_point(75, 30)
# number_rows = SCREEN_HEIGHT // BRICK_SIZE.y + 1
# number_bricks = SCREEN_WIDTH // BRICK_SIZE.x + 1
# y_start = 0
# y_end = BRICK_SIZE.y
# for rows in range(1, number_rows + 1):
#     if rows % 2 == 0:
#         x_start = 0
#         x_end = BRICK_SIZE.x
#     else:
#         x_start = -BRICK_SIZE.x / 2
#         x_end = BRICK_SIZE.x / 2
#     for brick in range(1, number_bricks + 1):
#         left_bottom = sd.get_point(x_start, y_start)
#         right_top = sd.get_point(x_end, y_end)
#         sd.rectangle(left_bottom, right_top, color=sd.COLOR_YELLOW, width=1)
#         x_start += BRICK_SIZE.x
#         x_end += BRICK_SIZE.x
#     y_start += BRICK_SIZE.y
#     y_end += BRICK_SIZE.y

#  Удобнее сразу на ходу рассчитывать данные
#  i = 0 # Счетчик рядов
#  # Циклы лучше взять в диапазоне экрана, а шагом будет размер кирпича
#  for y in range(0, sd.resolution[1] + 1, BRICK_SIZE.y):
#      i += 1
#      Если счетчик четный - смещения нет
#      В другом случае половина кирпича  BRICK_SIZE.x // 2
#      аналогичный цикл по "х", но у же с шагом "BRICK_SIZE.x"
#      for x in ...
#          Создаем переменные - точки
#          "левую_нижнюю" и "правую_верхнюю" и используем смещение и значения переменных цикла.
#          left_bottom_brick = ...
#          right_top_brick = ...
#          рисуем кирпич

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
sd.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
BRICK_SIZE = sd.get_point(100, 50)
row = 0
for y in range(0, sd.resolution[1] + 1, BRICK_SIZE.y):
    row += 1
    if row % 2 == 0:
        x_start = 0
    else:
        x_start = -BRICK_SIZE.x // 2
    for x in range(x_start, sd.resolution[0] + 1, BRICK_SIZE.x):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + BRICK_SIZE.x, y + BRICK_SIZE.y)
        sd.rectangle(left_bottom, right_top, color=sd.COLOR_YELLOW, width=1)

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
