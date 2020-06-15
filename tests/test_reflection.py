""" Expectations for finding lines of reflection.
"""
from math import sqrt
from statistics import mean

import pytest

import reflection
from tests.shapes import random_point


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

    one_point_set = [random_point(), random_point()]
    with pytest.raises(Exception) as e:
        reflection.find_lines_of_reflection(one_point_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    minimum_valid_set = [random_point(), random_point(), random_point()]
    reflection.find_lines_of_reflection(minimum_valid_set)
    assert True, "expected that three points is valid minimum input set"


def test_rectangle_lines_of_reflection():
    rectangle = [(-4, -2), (-4, 2), (4, 2), (4, -2)]
    derived_lors = reflection.find_lines_of_reflection(rectangle)

    assert len(derived_lors) == 2
    assert ((0, 2), (0, -2)) in derived_lors
    assert ((-4, 0), (4, 0)) in derived_lors


def test_square_lines_of_reflection():
    square = [(-2, -2), (-2, 2), (2, 2), (2, -2)]
    derived_lors = reflection.find_lines_of_reflection(square)

    assert len(derived_lors) == 4
    assert ((0, 2), (0, -2)) in derived_lors
    assert ((-2, 0), (2, 0)) in derived_lors
    assert ((-2, -2), (2, 2)) in derived_lors
    assert ((-2, 2), (2, -2)) in derived_lors


def test_two_points_lines_of_reflection():
    # we'll expect that one line of reflection between two points will have same
    # length as distance between the points
    two_points = [(-2, 0), (2, 0)]
    derived_lors = reflection.find_lines_of_reflection(two_points)
    assert len(derived_lors) == 1
    assert ((0, 2), (0, -2)) in derived_lors

    two_points = [(0, 2), (0, -2)]
    derived_lors = reflection.find_lines_of_reflection(two_points)
    assert len(derived_lors) == 1
    assert ((-2, 0), (2, 0)) in derived_lors

    assert reflection.find_lines_of_reflection(
        [(-2, 0), (2, 0)]
    ) == reflection.find_lines_of_reflection(
        [(2, 0), (-2, 0)]
    ), "Order of points shouldn't matter."


def test_triangle_lines_of_reflection():
    isosceles_triangle = [(-2, 0), (0, 4), (2, 0)]
    derived_lors = reflection.find_lines_of_reflection(isosceles_triangle)
    assert len(derived_lors) == 1
    assert ((0, 4), (0, 0)) in derived_lors

    edge_length = 4
    A = (-2, 0)
    B = (0, sqrt(3) * edge_length / 2)
    C = (2, 0)
    equilateral_triangle = [A, B, C]
    derived_lors = reflection.find_lines_of_reflection(equilateral_triangle)
    assert len(derived_lors) == 3
    assert (B, 0) in derived_lors
    assert (mean([A[0], B[0]]), mean([A[1], B[1]])) in derived_lors
    assert (mean([B[0], C[0]]), mean([B[1], C[1]])) in derived_lors
