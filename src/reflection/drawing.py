""" Present points, lines, etc.
"""
import matplotlib.pyplot as plt

from typing import List


def draw(title: str = None) -> None:
    """ Show the canvas. """
    if title:
        plt.title(title)
    plt.axis("equal")
    plt.show()


def draw_one_point(point: tuple, style: str = "bo") -> None:
    """ Draw a point.
    Args:
        point: (x, y) tuple
        style (str): drawing style e.g. "b-"
    """
    draw_multiple_points([point], style)


def draw_multiple_points(points: List[tuple], style: str = "bo") -> None:
    """ Draw a set of points.

    Args:
        points: list of (x, y) tuples
        style (str): drawing style e.g. "b-"
    """
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, style)


def draw_one_line(endpoints: tuple, style: str = "b-"):
    """ Draw a line connecting a list of exactly two endpoints.

    Args:
        endpoints (tuple): tuple of two (x, y) tuples
        style (str): drawing style e.g. "b-"
    """
    assert len(endpoints) == 2, "expected exactly two points to draw a line"

    x_coords, y_coords = zip(*endpoints)
    plt.plot(x_coords, y_coords, style)


def draw_multiple_lines(lines: List[tuple], style: str = "b-") -> None:
    """ Draw a set of lines.

    Args:
        lines (list): list of line endpoints
        style (str): drawing style e.g. "b-"
    """
    for line in lines:
        draw_one_line(line, style)
