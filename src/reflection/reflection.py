""" reflection.reflection
"""
import itertools
from typing import List

from reflection.core import (
    find_hull,
    find_center,
    is_point_on_line,
    find_distance_from_line_to_point,
    find_angle_from_line_to_point,
)


def find_lines_of_reflection(points: List[tuple] = None) -> List[tuple]:
    """ Compute set of lines of reflection / lines of symmetry for a set of points.

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

    lors = list(
        filter(lambda line: line_reflects_all_points(line, points), candidate_lors)
    )

    return lors


def find_candidate_lors(points: List[tuple]) -> List[tuple]:
    """ Compute a set of potential lines of reflection.

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


def line_reflects_all_points(line: tuple, points: List[tuple]) -> bool:
    """ Determine whether a line reflects a set of points.

    We compute a distance, angle (d, a) from the line to all points not on the line.
    The line satisfactorily reflects the points if each point has a mirror image, i.e.
    for each (d, a) there exists (d, -a).

    Args:
        line: tuple of (x, y) tuples specifying endpoints
        points: list of (x, y) coordinates
    Returns:
        bool
    """
    clockwise_from_line = []
    ccw_from_line = []
    for point in points:
        if is_point_on_line(point, line):
            continue
        distance = find_distance_from_line_to_point(line, point)
        angle = find_angle_from_line_to_point(line, point)
        if angle < 0:
            clockwise_from_line.append((distance, -1 * angle))
        else:
            ccw_from_line.append((distance, angle))

    clockwise_from_line = sorted(clockwise_from_line)
    ccw_from_line = sorted(ccw_from_line)

    return clockwise_from_line == ccw_from_line
