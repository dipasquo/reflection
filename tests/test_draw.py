""" View expectations.
"""
from reflection import drawing
from tests.shapes import random_point


def test_draw_multiple_points():
    drawing.draw_multiple_points([(-2, -2), (-2, 2), (2, 2), (2, -2)])
    drawing.draw()

    drawing.draw_multiple_points(
        [random_point(), random_point(), random_point(), random_point()]
    )
    drawing.draw()


def test_draw_line():
    drawing.draw_one_line(((-2, -2), (2, 2)))
    drawing.draw()

    drawing.draw_one_line(((-2, -2), (2, 2)), style="g--")
    drawing.draw()


def test_draw_lines():
    drawing.draw_multiple_lines([((0, -2), (0, 2)), ((-2, 0), (2, 0))])
    drawing.draw()
