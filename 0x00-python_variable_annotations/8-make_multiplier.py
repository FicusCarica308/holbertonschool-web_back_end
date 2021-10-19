#!/usr/bin/env python3
"""[summary]
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[summary]

    Args:
        multiplier (float): A constant factor we are gonna multiply
        every number that is called to 'function'

    Returns:
        Callable[[float], float]: A function is returned that
        multiples the given factor 'multiplier' by and number passed
        once function is returned
    """
    def function(number: float):
        return multiplier * number
    return function
