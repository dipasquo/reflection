""" View expectations.
"""
from reflection import drawing
from tests.helpers import random_point


def test_draw_points():
    drawing.draw_points(
        [(-2, -2), (-2, 2), (2, 2), (2, -2)]
    )

    drawing.draw_points(
        [random_point(), random_point(), random_point(), random_point()]
    )
