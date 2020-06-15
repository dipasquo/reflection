""" Some useful test helpers.
"""
import random
from math import pi, sin, cos
from typing import List


def random_point():
    """ Random (x, y) """
    point = (random.randint(-20, 20), random.randint(-20, 20))
    return point


def regular_polygon(n: int) -> List[tuple]:
    """ Derive the vertices of a regular polygon origin (0, 0)

    Args:
        n: number of vertices
    Returns:
        list of (x, y) vertex coordinates
    """
    r = 1

    points = []
    for k in range(n):
        point = (r * cos(k * 2 * pi / n), r * sin(k * 2 * pi / n))
        points.append(point)

    return points


def rectangle():
    return [(-2, 0), (-2, 2), (2, 2), (2, 0)]


def isosceles_triangle():
    return [(-1, 0), (0, 4), (1, 0)]


def flag():
    return [(-1, -4), (1, -4), (-4, 1), (-4, 4), (-1, 1), (1, 1), (4, 1), (4, 4)]


def butterfly():
    return [(0, -10), (-1, 1), (1, 1), (3, -1), (-3, -1), (-3, 3), (3, 3), (0, 12)]
