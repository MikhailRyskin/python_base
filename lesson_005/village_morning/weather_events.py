import simple_draw as sd


def snowfall():
    n = 20
    x_list = [x for x in range(0, 201, 10)]
    y_list = [sd.random_number(500, 800) for _ in range(n)]
    beam_length = [sd.random_number(10, 40) for _ in range(n)]
    while True:
        sd.start_drawing()
        for ind in range(n):
            point = sd.get_point(x_list[ind], y_list[ind])
            if point.y > 30:
                sd.snowflake(center=point, length=beam_length[ind], color=sd.background_color)
            y_list[ind] -= 10
            x_list[ind] += sd.random_number(-3, 6)
            point = sd.get_point(x_list[ind], y_list[ind])
            sd.snowflake(center=point, length=beam_length[ind])
        sd.finish_drawing()
        sd.sleep(0.1)
        # if sd.user_want_exit():
        if point.y < -200:
            break


def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    x_start = 450
    y_start = 0
    radius = 870
    center_position = sd.get_point(x_start, y_start)
    for color in rainbow_colors:
        sd.circle(center_position, radius, color, 15)
        radius -= 15


def sun():
    center_position = sd.get_point(380, 480)
    sd.circle(center_position, radius=50, color=sd.COLOR_ORANGE, width=0)
    for vector_angle in range(0, 360, 45):
        v = sd.get_vector(start_point=center_position, angle=vector_angle, length=100, width=5)
        v.draw(color=sd.COLOR_ORANGE)
