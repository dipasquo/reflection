""" Basic reflection function expectations.
"""
from math import sqrt

import pytest

import reflection
from tests.helpers import random_point


def test_input_point_set():
    with pytest.raises(Exception) as e:
        reflection.get_lines_of_reflection()
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    null_set = []
    with pytest.raises(Exception) as e:
        reflection.get_lines_of_reflection(null_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    one_point_set = [random_point()]
    with pytest.raises(Exception) as e:
        reflection.get_lines_of_reflection(one_point_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    minimum_valid_set = [random_point(), random_point()]
    reflection.get_lines_of_reflection(minimum_valid_set)
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


@pytest.mark.skip
def test_triangle_lines_of_reflection():
    assert False


@pytest.mark.skip
def test_rectangle_lines_of_reflection():
    assert False
