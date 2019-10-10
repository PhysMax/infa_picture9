from geometry import *
from graph import *

width, height = windowSize()

# Colors in RGB
wtr_clr = 22, 80, 68  # Pool's water
sky_clr = 0, 255, 255  # Sky
dgr_clr = 77, 77, 77  # Dark-grey
fgr_clr = 191, 203, 200  # Fish's grey
frd_clr = 221, 166, 166  # Fish's red
feye_clr = 121, 121, 242  # Fish's eye
sun_clr = 161, 249, 228  # Sun's yellow
ice_clr = 230, 230, 230  # Ice's grey


def draw_fish(x_start, y_start, x_size, y_size, angle):
    """ (x_start, y_start) - upper lef corner,x_size - horizontal size where 1 = 100% of the length of picture,
    y_size - vertical size where 1 = 100% of length,to mirror you should take x_size < 0 where -1 = 100% of the length,
    angle - angle of rotate, a - major seim axis, b - minor seim axis"""
    a = 0.08 * width
    b = 0.028 * height

    # Body
    penColor('black')
    brushColor(fgr_clr)
    points_triangle = [(a / 2, b), (0, 0), (0, 2 * b)]
    points_rotated_oval = rotated_oval(a / 2, 0, 1, 1, a, b, math.pi)
    points = points_triangle + points_rotated_oval
    make_rotation(points, x_start, y_start, x_size, y_size, angle)

    # Bottom left fin
    brushColor(frd_clr)
    penColor('black')
    points = [(a / 2 + 10, b + 11), (a / 2 + 20, b + 14), (a / 2 + 18, b + 25), (a / 2, b + 20)]
    make_rotation(points, x_start, y_start, x_size, y_size, angle)

    # Bottom right fin
    points = [(a * 9 / 4 - 10, b + 14), (a * 9 / 4 - 20, b + 16), (a * 9 / 4 - 18, b + 28), (a * 9 / 4, b + 23)]
    make_rotation(points, x_start, y_start, x_size, y_size, angle)

    # Upper fin
    points = [(a * 9 / 4 - 17, b - 16), (a * 9 / 4 - 37, b - 17), (a * 9 / 4 - 55, b - 30), (a * 9 / 4 - 10, b - 26)]
    make_rotation(points, x_start, y_start, x_size, y_size, angle)

    # Eye
    brushColor(feye_clr)
    points = rotated_oval(a * 7 / 4, b - 10, 1, 1, 5, 5, math.pi)
    make_rotation(points, x_start, y_start, x_size, y_size, angle)

    # White dot in eye
    penColor('white')
    brushColor('white')
    points = rotated_oval(a * 7 / 4 + 1, b - 7, 1, 1, 3, 1, math.pi * 5 / 3)
    make_rotation(points, x_start, y_start, x_size, y_size, angle)


def draw_pool(x_start, y_start, x_size, y_size):
    """ (x_start, y_start) - upper lef corner of rectangle in which inscribed oval of pool,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror you should take x_size < 0 where -1 = 100% of the length"""
    # Ice
    brushColor(dgr_clr)
    draw_oval(x_start, y_start, x_size, y_size, 0.15 * width, 0.05 * height)
    # Water
    brushColor(wtr_clr)
    draw_oval(x_start + 0.02 * width * x_size, y_start + 0.026 * height * y_size, x_size, y_size,
              0.15 * width - 0.02 * width, 0.05 * height - 0.013 * height)


def draw_rod(x_start, y_start, x_size, y_size):
    """ (x_start, y_start) - lower end of fishing rod stick,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror you should take x_size < 0 where -1 = 100% of length, endRod - end of rod, from this point throw starts,
    pointsThrow - list of two tuples described throw of rod """
    penSize(2)
    end_rod = draw_curve(x_start, y_start, x_size, y_size, 0.2 * width, 0.5 * height, math.pi,
                         math.pi * 4 / 3, math.pi / 6)
    penSize(1)
    points_throw = [end_rod, (end_rod[0], end_rod[1] + 0.5 * height * y_size)]
    polyline(points_throw)


def draw_bear(x_start, y_start, x_size, y_size, number):
    """ (x_start, y_start) - upper lef corner of rectangle in which inscribed oval of head,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror you should take x_size < 0 where -1 = 100% of the length, if number = 1 then draw picture 9.1, else -
    picture 9.2"""

    # Pool
    penColor('black')
    draw_pool(x_start + 0.3 * width * x_size, y_start + 0.38 * height * y_size, x_size, y_size)

    # Fish
    if number == 1:
        draw_fish(x_start + 0.38 * width * x_size, y_start + 0.55 * height * y_size, x_size, 0.8 * y_size,
                  -math.pi / 10)
    else:
        draw_fish(x_start + 0.34 * width * x_size, y_start + 0.53 * height * y_size, x_size, 0.8 * y_size,
                  -math.pi / 10)
        draw_fish(x_start + 0.74 * width * x_size, y_start + 0.55 * height * y_size, x_size * (-1), 0.8 * y_size,
                  -math.pi / 10)
        draw_fish(x_start + 0.74 * width * x_size, y_start + 0.43 * height * y_size, x_size * (-1), 0.8 * y_size,
                  math.pi / 10)
        draw_fish(x_start + 0.3 * width * x_size, y_start + 0.35 * height * y_size, x_size * 0.7 * (-1),
                  y_size * 0.8 * 0.7, -math.pi * 21 / 20)
        draw_fish(x_start + 0.58 * width * x_size, y_start + 0.35 * height * y_size, x_size * 0.7 * (-1),
                  y_size * 0.8 * 0.7, -math.pi * 1 / 6)
        draw_fish(x_start + 0.68 * width * x_size, y_start + 0.37 * height * y_size, x_size * 0.7, y_size * 0.8 * 0.7,
                  math.pi * 21 / 20)

    # Rod
    penColor('black')
    draw_rod(x_start + 0.15 * width * x_size, y_start - 0.15 * height * y_size, x_size, y_size)

    # Head
    brushColor('white')
    draw_oval(x_start, y_start, x_size, y_size, 0.1 * width, 0.05 * height)

    # Mouse
    draw_curve(x_start + 0.007 * width * x_size, y_start + 0.038 * height * y_size, x_size, y_size, 0.1 * width,
               0.02 * height, math.pi / 6, math.pi / 2, 0)

    # Body
    draw_oval(x_start - 0.15 * width * x_size, y_start + 0.08 * height * y_size, x_size, y_size, 0.16 * width,
              0.22 * height)

    # Arm
    draw_oval(x_start + 0.13 * width * x_size, y_start + 0.17 * height * y_size, x_size, y_size, 0.06 * width,
              0.03 * height)

    # Leg
    draw_oval(x_start + 0.04 * width * x_size, y_start + 0.4 * height * y_size, x_size, y_size, 0.11 * width,
              0.07 * height)

    # Foot
    draw_oval(x_start + 0.18 * width * x_size, y_start + 0.51 * height * y_size, x_size, y_size, 0.09 * width,
              0.025 * height)

    # Ear
    draw_part_rotated_oval(x_start + 0.01 * width * x_size, y_start + 0.01 * height * y_size, x_size, y_size, 15, 9,
                           math.pi / 2, math.pi * 3 / 2, math.pi / 4)

    # Nose
    brushColor('black')
    draw_oval(x_start + 0.2 * width * x_size, y_start + 0.04 * height * y_size, x_size, y_size, 3, 3)

    # Eye
    draw_oval(x_start + 0.09 * width * x_size, y_start + 0.03 * height * y_size, x_size, y_size, 3, 3)
