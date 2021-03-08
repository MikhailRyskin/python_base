import simple_draw as sd


def draw_branches(start_point, angle, length):
    if length < 4:
        return
    color = sd.COLOR_DARK_ORANGE
    if length < 10:
        color = sd.COLOR_GREEN
    v1 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length, width=1)
    v1.draw(color=color)
    v2 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length, width=1)
    v2.draw(color=color)
    next_point_1 = v1.end_point
    next_point_2 = v2.end_point
    next_angle_1 = angle - 30
    next_angle_2 = angle + 30
    next_length = length * .75
    draw_branches(start_point=next_point_1, angle=next_angle_1, length=next_length)
    draw_branches(start_point=next_point_2, angle=next_angle_2, length=next_length)


def tree():
    root_point = sd.get_point(950, 90)
    point_0 = sd.get_point(950, 0)

    sd.line(point_0, root_point, color=sd.COLOR_DARK_ORANGE, width=2)
    draw_branches(start_point=root_point, angle=90, length=60)


def smile(x, y, color):
    left_bottom = sd.get_point(x, y)
    right_top = sd.get_point(x + 60, y + 30)
    sd.ellipse(left_bottom, right_top, color, 2)
    left_eye = sd.get_point(x + 20, y + 20)
    sd.circle(left_eye, 3, color, 1)
    right_eye = sd.get_point(x + 40, y + 20)
    sd.circle(right_eye, 3, color, 1)
    mouth_left = sd.get_point(x + 25, y + 10)
    mouth_right = sd.get_point(x + 35, y + 10)
    sd.line(mouth_left, mouth_right, color, 1)


def human():
    color = sd.COLOR_WHITE
    smile(502, 70, color)
