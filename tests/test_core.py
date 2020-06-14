""" Expectations for lower level functions that help derive lines of reflection.
"""
from math import sqrt
from statistics import mean

import reflection.core


def test_find_center():
    # "line"
    assert reflection.core.find_center([(-1, -1), (1, 1)]) == (0, 0)
    assert reflection.core.find_center([(0, 0), (2, 2)]) == (1, 1)

    # "square"
    assert reflection.core.find_center([(0, 0), (0, 2), (2, 2), (2, 0)]) == (1, 1)

    # "isosceles triangle"
    assert reflection.core.find_center([(-2, 0), (0, 4), (2, 0)]) == (
        mean([-2, 0, 2]),
        mean([0, 4, 0]),
    )

    # "equilateral triangle"
    a = 4
    h = a * sqrt(3) / 2
    assert reflection.core.find_center([(0, 0), (a / 2, h), (a, 0)]) == (
        mean([0, a / 2, a]),
        mean([0, h, 0]),
    )


def test_find_line_segment_length():
    assert reflection.core.find_line_segment_length([(-1, 0), (1, 0)]) == 2
    assert reflection.core.find_line_segment_length([(0, -1), (0, 1)]) == 2
    assert reflection.core.find_line_segment_length([(-1, -1), (1, 1)]) == sqrt(8)


def test_find_bounding_box():
    assert reflection.core.find_bounding_box([(-1, -1), (1, 1)]) == (
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    )

    assert reflection.core.find_bounding_box([(-3, -1), (1, 2), (2, 1), (1, -2)]) == (
        (-3, -2),
        (-3, 2),
        (2, 2),
        (2, -2),
    )
