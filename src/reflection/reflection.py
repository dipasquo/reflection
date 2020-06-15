""" reflection.reflection
"""
from typing import List

import reflection.core


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

    candidate_lors = reflection.core.find_candidate_lors(points)

    lors = candidate_lors

    return lors
