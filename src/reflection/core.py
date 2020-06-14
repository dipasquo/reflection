""" Functions that help derive lines of reflection.
"""
from typing import List

from shapely.geometry import LineString, MultiPoint


def find_line_segment_length(points: List[tuple] = None) -> float:
    """ Good ole distance between two points.

    Args:
        points: list of two points as (x, y) tuples
    Returns:
        float
    """
    assert len(points) == 2, "Expected two points to define a line segment!"

    ls = LineString(points)

    return ls.length


def find_bounding_box(points: List[tuple] = None) -> tuple:
    """ Find the bounding box for set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        list of (x, y) coordinates of bounding box corners
        i.e. [lower left, upper left, upper right, lower right]
    """
    mp = MultiPoint(points)
    x_min, y_min, x_max, y_max = mp.bounds

    return (x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)


def find_center(points: List[tuple] = None) -> tuple:
    """ Find the center of a set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        (x, y) coordinates of center of set of points
    """
    mp = MultiPoint(points)

    center = (mp.centroid.x, mp.centroid.y)

    return center
