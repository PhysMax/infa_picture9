import math
from graph import *


def make_rotation(points, x_start, y_start, x_size, y_size, angle):
    """ points - points of object, (x_start, y_start) - starting point, x_size - horizontal size where 1 = 100%
    of the length, y_size - vertical size where 1 = 100% of length, angle - angle of rotate"""
    cos = math.cos(angle)
    sin = math.sin(angle)
    rot_points = []
    for it in range(0, len(points)):
        x = points[it][0] * cos - points[it][1] * sin
        y = points[it][0] * sin + points[it][1] * cos
        rot_points.append((x_start + x * x_size, y_start + y * y_size))
    polygon(rot_points)


def draw_rotated_triangle(x_start, y_start, points, angle):
    """ (x_start, y_start) - starting point about which the others points are turning,
    points - coordinates in the basis x_start, y_start of the vertices of the triangle [(x1,x2), (x2,y2), (x3, y3)],
    angle - angle of rotate"""
    rot_points = []
    s = math.sin(angle)
    c = math.cos(angle)
    for it in range(3):
        x = points[it][0] * c - points[it][1] * s
        y = points[it][0] * s + points[it][1] * c
        rot_points.append((x_start + x, y_start + y))
    polygon(rot_points)


def draw_oval(x_start, y_start, x_size, y_size, a, b):
    """ (x_start, y_start) - upper lef corner of rectangle in which inscribed oval,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror bear you should take x_size < 0 where -1 = 100%,
    a - major seim axis, b - minor seim axis, returns link to oval"""
    points = []
    for phi in range(0, 628):
        x0 = a * math.cos(phi / 100)
        y0 = b * math.sin(phi / 100)
        points.append((x_start + (x0 + a) * x_size, y_start + (y0 + b) * y_size))
    polygon(points)
    return points


def rotated_oval(x_start, y_start, x_size, y_size, a, b, angle):
    """ (x_start, y_start) - upper lef corner of rectangle in which inscribed non-rotations oval,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror bear you should take x_size < 0 where -1 = 100%,
    a - major seim axis, b - minor seim axis, returns link to oval, angle - angle of rotate,
    DOESN'T DRAW OVAL BUT RETURNS ITS POINTS"""
    points = []
    sin = math.sin(angle)
    cos = math.cos(angle)
    for phi in range(0, 628):
        x0 = a * math.cos(phi / 100)
        y0 = b * math.sin(phi / 100)
        xr = x0 * cos + y0 * sin
        yr = -x0 * sin + y0 * cos
        points.append((x_start + (xr + a) * x_size, y_start + (yr + b) * y_size))
    return points


def draw_part_rotated_oval(x_start, y_start, x_size, y_size, a, b, phi1, phi2, angle):
    """ (x_start, y_start) - upper lef corner of rectangle in which inscribed non-rotations oval,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror bear you should take x_size < 0 where -1 = 100%,
    a - major seim axis, b - minor seim axis, returns link to oval, phi1 - starting point on the oval,
    phi2 - ending point on the oval, angle - angle of rotate"""
    points = []
    sin = math.sin(angle)
    cos = math.cos(angle)
    for phi in range(int(abs(phi1 * 100)), int(abs(phi2 * 100)) + 1):
        x0 = a * math.cos(phi / 100)
        y0 = b * math.sin(phi / 100)
        xr = x0 * cos - y0 * sin
        yr = x0 * sin + y0 * cos
        points.append((x_start + (xr + a) * x_size, y_start + (yr + b) * y_size))
    polygon(points)


def draw_curve(x_start, y_start, x_size, y_size, a, b, phi1, phi2, angle):
    """ (x_start, y_start) - upper lef corner of rectangle in which inscribed non-rotations oval,
    x_size - horizontal size where 1 = 100% of the length, y_size - vertical size where 1 = 100% of length,
    to mirror bear you should take x_size < 0 where -1 = 100%,
    a - major seim axis, b - minor seim axis, returns link to oval, phi1 - starting point on the oval,
    phi2 - ending point on the oval, angle - angle of rotate"""
    points = []
    sin = math.sin(angle)
    cos = math.cos(angle)
    for phi in range(int(abs(phi1 * 100)), int(abs(phi2 * 100)) + 1):
        x0 = a * math.cos(phi / 100)
        y0 = b * math.sin(phi / 100)
        xr = x0 * cos - y0 * sin
        yr = x0 * sin + y0 * cos
        points.append((x_start + (xr + a) * x_size, y_start + (yr + b) * y_size))
    polyline(points)
    return points[int(phi2 * 100) - int(phi1 * 100)]
