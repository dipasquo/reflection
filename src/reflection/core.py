""" Functions that help derive lines of reflection.
"""
import itertools
from typing import List

from shapely.geometry import Point, LineString, MultiPoint


def find_edges(points: List[tuple]) -> List[tuple]:
    """ Derive a set of edges from set of points.

    Args:
        points: list of points as (x, y) tuples

    Returns:
        list of tuples of (x, y) edge endpoints
    """
    sorted_points = sorted(points)
    return list(itertools.combinations(sorted_points, 2))


def find_center(points: List[tuple]) -> tuple:
    """ Find the center of a set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        (x, y) coordinates of center of set of points
    """
    mp = MultiPoint(points)

    center = (mp.centroid.x, mp.centroid.y)

    return center


def is_point_on_line(point: tuple, line: tuple) -> bool:
    """ Check if point falls on a line.

    Args:
        point: (x, y) tuple
        line: tuple of (x, y) tuples specifying endpoints
    Returns:
        bool: point is on line, within some tolerance
    """
    assert len(line) == 2, "line should be specified as two (x, y) tuples"

    float_precision = 1e-15
    return Point(point).distance(LineString(line)) < float_precision


def find_candidate_lors(points: List[tuple]) -> List[tuple]:
    """ Derive a set of potential lines of reflection.

    For a line to be a possible line of reflection, it connects one of:
    * vertex to vertex
    * vertex to edge midpoint
    * edge midpoint to edge midpoint
    And inherently must pass through center of the geometry.

    Args:
        points: list of points as (x, y) tuples
    Returns:
        list of (x, y) tuples representing edge endpoints
    """
    center = find_center(points)
    edges = find_edges(points)
    edge_midpoints = list(map(lambda edge: find_center(list(edge)), edges))

    all_connecting_lines = list(itertools.combinations(points + edge_midpoints, 2))

    lines_on_center = list(
        filter(lambda line: is_point_on_line(center, line), all_connecting_lines)
    )

    non_overlapping_lines = distill_overlapping_lines(lines_on_center)

    return non_overlapping_lines


def distill_overlapping_lines(lines: List[tuple]) -> List[tuple]:
    """ Find longest unique non-overlapping lines from a set.

    Args:
        lines: list of (x, y) tuples representing line endpoints
    Returns:
        list of (x, y) tuples representing line endpoints
    """
    containing_lines = []

    for line in lines:
        is_contained_line = False
        replaced_contained_line = False
        for i, l in enumerate(containing_lines):
            if LineString(line).contains(LineString(l)):
                containing_lines[i] = line
                replaced_contained_line = True
            if LineString(l).contains(LineString(line)):
                is_contained_line = True
        if not replaced_contained_line and not is_contained_line:
            containing_lines.append(line)

    return containing_lines
