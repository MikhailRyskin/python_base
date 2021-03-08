import simple_draw as sd


def wall():
    house_dimensions = (300, 180)
    brick_size = sd.get_point(40, 20)
    row = 0
    for y in range(0, house_dimensions[1] + 1, brick_size.y):
        row += 1
        if row % 2 == 0:
            x_start = 400
        else:
            x_start = 400 - brick_size.x // 2
        for x in range(x_start, x_start + house_dimensions[0] + 1, brick_size.x):
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + brick_size.x, y + brick_size.y)
            sd.rectangle(left_bottom, right_top, color=sd.COLOR_YELLOW, width=1)
    facade_bottom = sd.get_point(380, 0)
    facade_top = sd.get_point(720, 180)
    sd.rectangle(facade_bottom, facade_top, color=sd.COLOR_YELLOW, width=1)


def roof():
    left_bottom = sd.get_point(420, 220)
    right_top = sd.get_point(440, 300)
    sd.rectangle(left_bottom, right_top, color=sd.COLOR_WHITE, width=0)
    point_list = [sd.get_point(340, 180), sd.get_point(760, 180), sd.get_point(500, 340)]
    sd.polygon(point_list, color=sd.COLOR_DARK_RED, width=0)


def building():
    wall()

    left_bottom_window = sd.get_point(500, 60)
    sd.square(left_bottom_window, side=80, color=sd.COLOR_DARK_CYAN, width=0)

    roof()
