""" Expectations for finding lines of reflection.
"""
from math import sqrt

import pytest

from reflection import reflection, shapes


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

    one_point_set = [shapes.random_point()]
    with pytest.raises(Exception) as e:
        reflection.find_lines_of_reflection(one_point_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    one_point_set = [shapes.random_point(), shapes.random_point()]
    with pytest.raises(Exception) as e:
        reflection.find_lines_of_reflection(one_point_set)
    assert e.type == ValueError
    assert "invalid" in str(e.value)

    minimum_valid_set = [shapes.random_point(), shapes.random_point(), shapes.random_point()]
    reflection.find_lines_of_reflection(minimum_valid_set)
    assert True, "expected that three points is valid minimum input set"


def test_find_candidate_lors():
    square = [(0, 0), (0, 2), (2, 2), (2, 0)]
    shape = square
    candidate_lors = reflection.find_candidate_lors(shape)
    assert len(candidate_lors) == 4

    shape = shapes.rectangle()
    candidate_lors = reflection.find_candidate_lors(shape)
    assert len(candidate_lors) == 4

    shape = shapes.regular_polygon(n=6)
    candidate_lors = reflection.find_candidate_lors(shape)
    assert len(candidate_lors) == 6


def test_rectangle_lines_of_reflection():
    rectangle = [(-4, -2), (-4, 2), (4, 2), (4, -2)]
    computed_lors = reflection.find_lines_of_reflection(rectangle)

    assert len(computed_lors) == 2
    assert ((0, 2), (0, -2)) in computed_lors
    assert ((-4, 0), (4, 0)) in computed_lors


def test_square_lines_of_reflection():
    square = [(-2, -2), (-2, 2), (2, 2), (2, -2)]
    computed_lors = reflection.find_lines_of_reflection(square)

    assert len(computed_lors) == 4
    assert ((0, 2), (0, -2)) in computed_lors
    assert ((-2, 0), (2, 0)) in computed_lors
    assert ((-2, -2), (2, 2)) in computed_lors
    assert ((-2, 2), (2, -2)) in computed_lors


def test_triangle_lines_of_reflection():
    isosceles_triangle = [(-2, 0), (0, 4), (2, 0)]
    computed_lors = reflection.find_lines_of_reflection(isosceles_triangle)
    assert len(computed_lors) == 1
    assert ((0, 4), (0, 0)) in computed_lors

    line_length = 4
    A = (-2, 0)
    B = (0, sqrt(3) * line_length / 2)
    C = (2, 0)
    equilateral_triangle = [A, B, C]
    computed_lors = reflection.find_lines_of_reflection(equilateral_triangle)
    assert len(computed_lors) == 3
