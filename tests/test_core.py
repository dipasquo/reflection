""" Expectations for lower level functions that help compute lines of reflection.
"""
from math import sqrt
from statistics import mean

import pytest

import reflection
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


def test_find_hull():
    hull = reflection.core.find_hull([(0, 2), (0, 0), (2, 0)])
    assert len(hull) == 3
    assert ((0, 0), (0, 2)) in hull
    assert ((0, 2), (2, 0)) in hull
    assert ((0, 2), (2, 0)) in hull

    hull = reflection.core.find_hull([(0, 0), (0, 2), (2, 2), (2, 0)])
    assert len(hull) == 4
    assert ((0, 0), (0, 2)) in hull
    assert ((0, 2), (2, 2)) in hull
    assert ((2, 2), (2, 0)) in hull
    assert ((2, 0), (0, 0)) in hull

    hull = reflection.core.find_hull([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0)])
    assert len(hull) == 4
    assert ((0, 0), (0, 2)) in hull
    assert ((0, 2), (2, 2)) in hull
    assert ((2, 2), (2, 0)) in hull
    assert ((2, 0), (0, 0)) in hull


def test_is_point_on_line():
    assert reflection.core.is_point_on_line((1, 1), ((0, 0), (2, 2)))
    assert reflection.core.is_point_on_line((0, 0), ((-1, -1), (1, 1)))
    assert reflection.core.is_point_on_line((0, 0), ((0, 0), (1, 1)))
    assert reflection.core.is_point_on_line((1, 1), ((0, 0), (1, 1)))

    assert not reflection.core.is_point_on_line((2, 2), ((0, 0), (1, 1)))
    assert not reflection.core.is_point_on_line((1e-8, 0), ((-1, -1), (1, 1)))


def test_find_distance_from_line_to_point():
    # horizontal line
    assert (
        reflection.core.find_distance_from_line_to_point(((0, 0), (1, 0)), (0, 1))
        == 1.0
    )

    # vertical line
    assert (
        reflection.core.find_distance_from_line_to_point(((0, 0), (0, 1)), (1, 0))
        == 1.0
    )

    # unit angle
    assert (
        reflection.core.find_distance_from_line_to_point(((0, 0), (1, 1)), (1, 0))
        == sqrt(2) / 2,
        8,
    )

    # point on line
    assert (
        reflection.core.find_distance_from_line_to_point(((0, 0), (1, 1)), (0.5, 0.5))
        == 0.0
    )


def test_find_angle_from_line_to_point():
    # 45 degrees (counterclockwise)
    assert reflection.core.find_angle_from_line_to_point(
        ((0, 0), (1, 0)), (1, 1)
    ) == pytest.approx(45)

    # 45 degrees (clockwise)
    assert reflection.core.find_angle_from_line_to_point(
        ((0, 0), (1, 0)), (1, -1)
    ) == pytest.approx(-45)

    # 90 degrees (counterclockwise)
    assert reflection.core.find_angle_from_line_to_point(
        ((0, 0), (1, 0)), (0, 1)
    ) == pytest.approx(90)

    # 90 degrees (clockwise)
    assert reflection.core.find_angle_from_line_to_point(
        ((0, 0), (1, 0)), (0, -1)
    ) == pytest.approx(-90)
