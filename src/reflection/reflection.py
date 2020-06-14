""" reflection.reflection
"""
from shapely.geometry import LineString, MultiPoint

from typing import List


def find_lines_of_reflection(points: List[tuple] = None) -> List[tuple]:
    """ Derive set of lines of reflection / lines of symmetry for a set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        list of line segments as [((x11, y11), (x21, y21)), ((x12, y12), (x22, y22))]
    Raises:
        ValueError: on invalid set of points
    """
    if points is None or len(points) < 2:
        raise ValueError("invalid input, expecting at least two points")

    lower_left, upper_left, upper_right, lower_right = find_bounding_box(points)

    horiz = (
        find_center([lower_left, upper_left]),
        find_center([lower_right, upper_right]),
    )
    vert = (
        find_center([upper_left, upper_right]),
        find_center([lower_left, lower_right]),
    )
    lof = [horiz, vert]

    width = find_line_segment_length([lower_left, lower_right])
    height = find_line_segment_length([lower_left, upper_left])
    if width == height:
        lof.append((lower_left, upper_right))
        lof.append((upper_left, lower_right))

    return lof


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
    x_min, y_min, x_max, y_max = mp.bounds

    center = ((x_min + x_max) / 2, (y_min + y_max) / 2)

    return center
