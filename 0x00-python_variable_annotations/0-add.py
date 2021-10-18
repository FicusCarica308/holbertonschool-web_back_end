#!/usr/bin/env python3
"""
[summary]
Contains a single python function definition using Basic python
annotations
"""


def add(a: float, b: float) -> float:
    """
    [summary]
    Takes a float a and a float b as arguments and returns their sum as a float
    (type-annotated)

    Args:
        a (float): number to be added
        b (float): number to be added

    Returns:
        [float]: sum of a + b
    """
    return (a + b)
