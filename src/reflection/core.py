""" Functions that help derive lines of reflection.
"""
import itertools
from typing import List

from shapely.geometry import Point, LineString, MultiPoint


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
    hull = find_hull(points)
    hull_midpoints = list(map(lambda edge: find_center(list(edge)), hull))

    all_connecting_lines = list(itertools.combinations(points + hull_midpoints, 2))

    lines_on_center = list(
        filter(lambda line: is_point_on_line(center, line), all_connecting_lines)
    )

    return lines_on_center
