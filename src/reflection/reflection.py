""" reflection.reflection
"""
import itertools
from typing import List

from reflection.core import find_hull, find_center, is_point_on_line


def find_lines_of_reflection(points: List[tuple] = None) -> List[tuple]:
    """ Derive set of lines of reflection / lines of symmetry for a set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        list of line segments as [((x11, y11), (x21, y21)), ((x12, y12), (x22, y22))]
    Raises:
        ValueError: on invalid set of points
    """
    if points is None or len(points) < 3:
        raise ValueError("invalid input, expecting at least three points")

    candidate_lors = find_candidate_lors(points)

    lors = candidate_lors

    return lors


def find_candidate_lors(points: List[tuple]) -> List[tuple]:
    """ Derive a set of potential lines of reflection.

    For a line to be a possible line of reflection, it connects one of:
    * two points on the outer hull of geometry
    * two line midpoints on outer hull
    * one point and one line midpoint from outer hull

    And must pass through the center of the geometry.

    Args:
        points: list of points as (x, y) tuples
    Returns:
        list of (x, y) tuples representing line endpoints
    """
    hull = find_hull(points)

    points_on_hull = []
    for point in points:
        if any(map(lambda line: is_point_on_line(point, line), hull)):
            points_on_hull.append(point)

    hull_midpoints = list(map(lambda line: find_center(list(line)), hull))

    all_connecting_lines = list(
        itertools.combinations(points_on_hull + hull_midpoints, 2)
    )

    center = find_center(points)
    lines_on_center = list(
        filter(lambda line: is_point_on_line(center, line), all_connecting_lines)
    )

    return lines_on_center
