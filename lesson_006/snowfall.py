import simple_draw as sd

#  Не проще ли хранить координаты в одном списке списков?
#  мы делали этот модуль на основе прошлых. Там были разные списки.
#  Для меня в этом есть логика. Мы работаем только с y: он меняется, выходит за экран, x не меняется.
#  Надо переделать все работающие функции. Мне кажется, проще оставить как есть.
#  TODO Если вам так удобнее, то ваше право, но гораздо удобнее работать с общей структурой
#   потому что снежинки обычно не падают ровно вниз, соответственно изменять придется и координаты "х"
#   Например:
#   _snowflakes_coords = []
#   .
#   def create_snow(n):
#       global _snowflakes_coords
#       for c in range(n):
#           x = sd.random_number(0, sd.resolution[0])
#           y = sd.random_number(sd.resolution[1], sd.resolution[1] * 2)
#           _snowflakes_coords.append([x, y, ])
#   .
#   def move_snow():
#      global _snowflakes_coords
#      for snow in _snowflakes_coords:
#          snow[1] -= sd.random_number(5, 8)
#          snow[0] += sd.random_number(-2, 2)
x_snowflakes = []
y_snowflakes = []
off_screen_flakes = []


def get_snowflakes(number=10):
    #  global поддерживает перечисление через запятую
    #  global x_snowflakes, y_snowflakes
    # TODO исправил
    global x_snowflakes, y_snowflakes
    x_new_list = [sd.random_number(20, sd.resolution[0] - 20) for _ in range(number)]
    y_new_list = [sd.random_number(sd.resolution[1], sd.resolution[1] + 300) for _ in range(number)]
    x_snowflakes += x_new_list
    y_snowflakes += y_new_list


# "range - len" нужно убрать
#  Стоит запомнить - если вы написали range(len(list)  - вы что-то делаете не так
#  исправил
def draw_snowflakes(color):
    global x_snowflakes, y_snowflakes
    for ind, x_flake in enumerate(x_snowflakes):
        point = sd.get_point(x_flake, y_snowflakes[ind])
        sd.snowflake(center=point, length=20, color=color)

# TODO в этих функциях также стоит поправить
def shift_snowflakes():
    global x_snowflakes, y_snowflakes
    for ind in range(len(x_snowflakes)):
        y_snowflakes[ind] -= 10
        # x_snowflakes[ind] += sd.random_number(-10, 10)


def off_screen_snowflakes():
    global x_snowflakes, y_snowflakes, off_screen_flakes
    off_screen_flakes.clear()
    for ind in range(len(x_snowflakes)):
        if y_snowflakes[ind] < -30:
            off_screen_flakes.append(ind)
    if off_screen_flakes:
        return True
    else:
        return False


def removing_snowflakes():
    global x_snowflakes, y_snowflakes, off_screen_flakes
    need_new_flakes = 0
    for index in off_screen_flakes:
        del x_snowflakes[index]
        del y_snowflakes[index]
        need_new_flakes += 1
    # Для очистки списка используйте .clear()
    # TODO исправил
    off_screen_flakes.clear()
    return need_new_flakes
