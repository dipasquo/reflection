""" Some useful test helpers.
"""
import random


def random_point():
    """ Random (x, y) """
    point = (random.randint(-20, 20), random.randint(-20, 20))
    return point
