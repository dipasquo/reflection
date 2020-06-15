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


def test_find_edges():
    edges = reflection.core.find_edges([(0, 0), (0, 2)])
    assert len(edges) == 1
    assert ((0, 0), (0, 2)) in edges

    edges = reflection.core.find_edges([(0, 2), (0, 0)])
    assert len(edges) == 1
    assert ((0, 0), (0, 2)) in edges

    edges = reflection.core.find_edges([(0, 2), (0, 0), (2, 0)])
    assert len(edges) == 3
    assert ((0, 0), (0, 2)) in edges
    assert ((0, 0), (2, 0)) in edges
    assert ((0, 2), (2, 0)) in edges


def test_is_point_on_line():
    assert False, "some tests needed"


def test_find_candidate_lors():
    square = [(0, 0), (0, 2), (2, 2), (2, 0)]
    candidate_lors = reflection.core.find_candidate_lors(square)
    assert len(candidate_lors) == 4

    rectangle = [(0, 0), (0, 2), (4, 2), (4, 0)]
    candidate_lors = reflection.core.find_candidate_lors(rectangle)
    assert len(candidate_lors) == 4


def test_distill_overlapping_lines():
    """ Initial candidate LORs contain overlapping segments, choose the longest one. """
    one_non_overlapping_line = [((0, 0), (0, 2)), ((0, 1), (0, 2))]
    assert reflection.core.distill_overlapping_lines(one_non_overlapping_line) == [
        ((0, 0), (0, 2)),
    ]

    one_non_overlapping_line = [((0, 1), (0, 2)), ((0, 0), (0, 2))]
    assert reflection.core.distill_overlapping_lines(one_non_overlapping_line) == [
        ((0, 0), (0, 2)),
    ]

    two_non_overlapping_lines = [((0, 0), (0, 2)), ((0, 0), (2, 0)), ((0, 0), (0, 4))]
    assert reflection.core.distill_overlapping_lines(two_non_overlapping_lines) == [
        ((0, 0), (0, 4)),
        ((0, 0), (2, 0)),
    ]
