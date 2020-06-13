""" Present points, lines, etc.
"""
import matplotlib.pyplot as plt

from typing import List


def draw_points(points: List[tuple]) -> None:
    """ Draw a point.

    Args:
        points: list of (x, y) tuples
    """
    plt.title("Points")
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords)
    plt.show()
