""" reflection.reflection
"""
from typing import List

from reflection.core import find_center, find_bounding_box, find_line_segment_length


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

    if len(points) == 2:
        x_center, y_center = find_center(points)
        offset = find_line_segment_length(points) / 2
        if lower_left == upper_left:  # horiz points, vert reflection line
            return [((x_center, y_center + offset), (x_center, y_center - offset))]
        elif lower_left == lower_right:  # vert points, horiz reflection line
            return [((x_center - offset, y_center), (x_center + offset, y_center))]

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
