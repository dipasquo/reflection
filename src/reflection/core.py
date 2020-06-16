""" Functions that help derive lines of reflection.
"""
import itertools
from math import asin, degrees
from typing import List

from shapely.geometry import Point, LineString, MultiPoint, LinearRing


def find_hull(points: List[tuple]) -> List[tuple]:
    """ Find the edges of the outer hull of the point set.

    Args:
        points: list of tuples, (x, y) point coordinates
    """
    mp = MultiPoint(points)
    hull_vertices = list(mp.convex_hull.boundary.coords)

    # hull_vertices looks like [A, B, C, A] from which we want to derive three edges
    # AB, BC, CA

    hull = []
    for i in range(len(hull_vertices) - 1):
        hull.append((hull_vertices[i], hull_vertices[i + 1]))

    return hull


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
    * two points on the outer hull of geometry
    * two edge midpoints on outer hull
    * one point and one edge midpoint from outer hull

    And must pass through the center of the geometry.

    Args:
        points: list of points as (x, y) tuples
    Returns:
        list of (x, y) tuples representing edge endpoints
    """
    hull = find_hull(points)

    points_on_hull = []
    for point in points:
        if any(map(lambda edge: is_point_on_line(point, edge), hull)):
            points_on_hull.append(point)

    hull_midpoints = list(map(lambda edge: find_center(list(edge)), hull))

    all_connecting_lines = list(
        itertools.combinations(points_on_hull + hull_midpoints, 2)
    )

    center = find_center(points)
    lines_on_center = list(
        filter(lambda line: is_point_on_line(center, line), all_connecting_lines)
    )

    return lines_on_center


def find_distance_from_edge_to_point(edge: tuple, point: tuple) -> float:
    """ Distance from a line to a point.

    Args:
        edge (tuple): tuple of (x, y) edge endpoints
        point (tuple): (x, y) point coords
    Returns:
        float
    """
    assert len(edge) == 2, "line should be specified as two (x, y) tuples"

    return LineString(edge).distance(Point(point))


def find_angle_from_line_to_point(line: tuple, point: tuple) -> float:
    """ Derive angle AC from line AB and point C.

    Args:
        line (tuple): line AB, pair of (x, y) endpoints
        point (tuple): point C, (x, y) coord
    Returns:
        float: angle in degrees, <0 when ABC is clockwise, >0 when ABC is CCW
    """
    A = line[0]
    B = line[1]
    C = point
    path = LinearRing([A, B, C])
    sign = 1 if path.is_ccw else -1

    hypotenuse = Point(A).distance(Point(C))
    opposite = LineString(line).distance(Point(C))

    float_precision = 8

    return sign * round(degrees(asin(opposite / hypotenuse)), float_precision)
