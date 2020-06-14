""" Basic reflection function expectations.
"""
from math import sqrt

import pytest

import reflection
from tests.helpers import random_point


def test_input_point_set():
    with pytest.raises(Exception) as e:
        reflection.find_lines_of_reflection()
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    null_set = []
    with pytest.raises(Exception) as e:
        reflection.find_lines_of_reflection(null_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    one_point_set = [random_point()]
    with pytest.raises(Exception) as e:
        reflection.find_lines_of_reflection(one_point_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    minimum_valid_set = [random_point(), random_point()]
    reflection.find_lines_of_reflection(minimum_valid_set)
    assert True, "expected that two points is valid minimum input set"


def test_find_center():
    assert reflection.reflection.find_center([(-1, -1), (1, 1)]) == (0, 0)
    assert reflection.reflection.find_center([(0, 0), (2, 2)]) == (1, 1)
    assert reflection.reflection.find_center([(-2, 0), (0, 2), (2, 0)]) == (0, 1)
    assert reflection.reflection.find_center([(0, 0), (0.5, 1), (1, 0)]) == (0.5, 0.5)
    assert reflection.reflection.find_center([(0, 0), (0, 2), (2, 0), (2, 2)]) == (1, 1)

    # equilateral triangle
    a = 4
    h = a * sqrt(3) / 2
    assert reflection.reflection.find_center([(0, 0), (a / 2, h), (a, 0)]) == (
        a / 2,
        h / 2,
    )


def test_find_line_segment_length():
    assert reflection.reflection.find_line_segment_length([(-1, 0), (1, 0)]) == 2
    assert reflection.reflection.find_line_segment_length([(0, -1), (0, 1)]) == 2
    assert reflection.reflection.find_line_segment_length([(-1, -1), (1, 1)]) == sqrt(8)


def test_find_bounding_box():
    assert reflection.reflection.find_bounding_box([(-1, -1), (1, 1)]) == (
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1),
    )

    assert reflection.reflection.find_bounding_box(
        [(-3, -1), (1, 2), (2, 1), (1, -2)]
    ) == ((-3, -2), (-3, 2), (2, 2), (2, -2))


def test_rectangle_lines_of_reflection():
    rectangle = [(-4, -2), (-4, 2), (4, 2), (4, -2)]
    derived_lof = reflection.find_lines_of_reflection(rectangle)

    assert len(derived_lof) == 2
    assert ((0, 2), (0, -2)) in derived_lof
    assert ((-4, 0), (4, 0)) in derived_lof


def test_square_lines_of_reflection():
    square = [(-2, -2), (-2, 2), (2, 2), (2, -2)]
    derived_lof = reflection.find_lines_of_reflection(square)

    assert len(derived_lof) == 4
    assert ((0, 2), (0, -2)) in derived_lof
    assert ((-2, 0), (2, 0)) in derived_lof
    assert ((-2, -2), (2, 2)) in derived_lof
    assert ((-2, 2), (2, -2)) in derived_lof


@pytest.mark.skip
def test_two_points_lines_of_reflection():
    assert False


@pytest.mark.skip
def test_triangle_lines_of_reflection():
    assert False
