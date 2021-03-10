import simple_draw as sd


x_snowflakes = []
y_snowflakes = []
off_screen_flakes = []


def get_snowflakes(number=10):
    global x_snowflakes
    global y_snowflakes
    x_new_list = [sd.random_number(20, sd.resolution[0] - 20) for _ in range(number)]
    y_new_list = [sd.random_number(sd.resolution[1], sd.resolution[1] + 300) for _ in range(number)]
    x_snowflakes += x_new_list
    y_snowflakes += y_new_list


def draw_snowflakes(color):
    global x_snowflakes
    global y_snowflakes
    for ind in range(len(x_snowflakes)):
        point = sd.get_point(x_snowflakes[ind], y_snowflakes[ind])
        sd.snowflake(center=point, length=20, color=color)


def shift_snowflakes():
    global x_snowflakes
    global y_snowflakes
    for ind in range(len(x_snowflakes)):
        y_snowflakes[ind] -= 10
        # x_snowflakes[ind] += sd.random_number(-10, 10)


def off_screen_snowflakes():
    global x_snowflakes
    global y_snowflakes
    global off_screen_flakes
    off_screen_flakes = []
    for ind in range(len(x_snowflakes)):
        if y_snowflakes[ind] < -30:
            off_screen_flakes.append(ind)
    if off_screen_flakes:
        return True
    else:
        return False


def removing_snowflakes():
    global x_snowflakes
    global y_snowflakes
    global off_screen_flakes
    need_new_flakes = 0
    for index in off_screen_flakes:
        del x_snowflakes[index]
        del y_snowflakes[index]
        need_new_flakes += 1
    off_screen_flakes = []
    return need_new_flakes
