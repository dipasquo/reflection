""" reflection.reflection
"""
from typing import List


def get_lines_of_reflection(points: List[tuple] = None) -> List[tuple]:
    """ Derive set of lines of reflection / lines of symmetry for a set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        list of lines as ((x1, y1), (x2, y2)) tuples specifying points on a bounding box
    Raises:
        ValueError: on invalid set of points
    """
    if points is None or len(points) < 2:
        raise ValueError("invalid input, expecting at least two points")

    return []


def find_center(points: List[tuple] = None) -> tuple:
    """ Find the center of a set of points.

    Args:
        points: list of tuples, (x, y) point coordinates
    Returns:
        (x, y) coordinates of center of set of points
    """
    x_min = min([p[0] for p in points])
    x_max = max([p[0] for p in points])

    y_min = min([p[1] for p in points])
    y_max = max([p[1] for p in points])

    center = ((x_min + x_max) / 2, (y_min + y_max) / 2)

    return center
